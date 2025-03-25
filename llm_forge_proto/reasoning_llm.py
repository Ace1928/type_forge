#!/usr/bin/env python
import json
import logging
import re
import sys

# ------------------------------
# Additional Libraries
# ------------------------------
import nltk
from jinja2 import Template
from transformers import pipeline

# Attempt to ensure NLTK 'punkt' is available
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

# ------------------------------
# Logging Configuration
# ------------------------------
try:
    from colorlog import ColoredFormatter

    handler = logging.StreamHandler()
    formatter = ColoredFormatter(
        "%(log_color)s%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        },
    )
    handler.setFormatter(formatter)
    logging.basicConfig(level=logging.DEBUG, handlers=[handler])
except ImportError:
    logging.basicConfig(
        level=logging.DEBUG,
        stream=sys.stdout,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
    )

logger = logging.getLogger(__name__)

# ------------------------------
# Initialize the text-generation pipeline for CPU (Qwen2.5-0.5B-Instruct)
# ------------------------------
logger.info(
    "Initializing text-generation pipeline with Qwen/Qwen2.5-0.5B-Instruct for CPU...",
)
generator = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct",
    device=-1,  # CPU only
)
logger.info("Pipeline initialized successfully.")


# ------------------------------
# Jinja Template for Final Output
# ------------------------------
SECTION_TEMPLATE = """
[SECTION: {{ section_name }}]
{{ content }}

Word Count: {{ word_count }}
"""


# ------------------------------
# Component 1: Input Parser & Validator
# ------------------------------
def parse_input(prompt: str) -> dict:
    """
    Parses a raw user prompt into a structured dictionary.
    {
      "task": <task description>,
      "models": [list of model names],
      "sections": [list of required sections]
    }
    """
    logger.debug("Starting input parsing.")
    if "Provide details on:" not in prompt:
        logger.error(
            "The prompt does not contain the required 'Provide details on:' marker.",
        )
        raise ValueError("Prompt must contain 'Provide details on:'")

    parts = prompt.split("Provide details on:")
    task_part = parts[0].strip()
    details_part = parts[1].strip()
    logger.debug("Extracted task part and details part.")

    # Extract models from the text after the last colon in 'task_part'.
    if ":" in task_part:
        models_str = task_part.split(":")[-1].strip().rstrip(".")
        # remove leading "and " if present
        models = [
            m.strip().replace("and ", "") for m in models_str.split(",") if m.strip()
        ]
        logger.debug(f"Extracted models: {models}")
    else:
        models = []
        logger.warning("No models found in the task part.")

    # Extract sections: each line that starts with a number and a dot.
    sections = []
    for line in details_part.splitlines():
        line = line.strip()
        if line:
            match = re.match(r"\d+\.\s*(.*)", line)
            if match:
                section = match.group(1).strip()
                sections.append(section)
                logger.debug(f"Found section: {section}")

    structured_input = {"task": task_part, "models": models, "sections": sections}
    logger.info("Input parsing complete.")
    return structured_input


# ------------------------------
# Refinement & Post-Processing
# ------------------------------
def refine_section_output(
    model_name: str,
    section: str,
    content: str,
    attempt: int = 1,
    max_attempts: int = 2,
) -> str:
    """
    Uses NLTK to do a simple check (e.g. word count).
    If the content is too short, we re-prompt the model for more detail.
    This lets the AI "act on" its own output before finalizing.
    """
    tokens = nltk.word_tokenize(content)
    word_count = len(tokens)

    logger.debug(
        f"Refinement check for {model_name} - '{section}': word_count={word_count}",
    )

    # Simple example: if < 30 words, attempt to refine.
    if word_count < 30 and attempt <= max_attempts:
        logger.warning(
            f"Content for {model_name} - '{section}' is quite short ({word_count} words). Attempting refinement...",
        )
        refine_prompt = (
            f"Refine and expand the following content about {model_name} "
            f"for the section '{section}'. Please add more detail:\n\n"
            f"{content}\n\n"
        )
        try:
            result = generator(
                refine_prompt,
                max_length=250,
                do_sample=True,
                temperature=0.7,
                truncation=True,
            )
            new_text = result[0]["generated_text"]
            # Remove the refine_prompt portion if present
            if new_text.startswith(refine_prompt):
                new_text = new_text[len(refine_prompt) :].strip()
            logger.info(
                f"Refinement attempt {attempt} completed. Re-checking word count...",
            )
            return refine_section_output(
                model_name,
                section,
                new_text,
                attempt + 1,
                max_attempts,
            )
        except Exception as e:
            logger.error(f"Error during refinement generation: {e}")
            return content  # fallback to original content
    else:
        logger.debug(f"No further refinement needed for {model_name} - '{section}'.")
        return content


def apply_jinja_template(section_name: str, content: str) -> str:
    """
    Applies a Jinja2 template to finalize the section output,
    including a word count or other metadata.
    """
    tokens = nltk.word_tokenize(content)
    word_count = len(tokens)
    template = Template(SECTION_TEMPLATE.strip())
    rendered = template.render(
        section_name=section_name,
        content=content,
        word_count=word_count,
    )
    return rendered


# ------------------------------
# Component 2: AI Response Evaluator & Formatter
# ------------------------------
def generate_section_for_model(
    model_name: str,
    section: str,
    task: str,
    attempt: int = 1,
    max_attempts: int = 3,
) -> str:
    """
    Uses the text-generation model to generate content for a given model and section.
    Retries (recursively) up to max_attempts if no text is generated.
    """
    logger.info(
        f"Generating content for model '{model_name}' - Section: '{section}' (Attempt {attempt})",
    )
    prompt_text = f"{task}\n\nProvide details for {model_name} regarding {section}:"
    logger.debug(f"Prompt for generation: {prompt_text}")

    try:
        result = generator(
            prompt_text,
            max_length=150,
            do_sample=True,
            temperature=0.7,
            truncation=True,  # to avoid warnings
        )
        generated_text = result[0]["generated_text"]
        logger.debug("Raw generated text received.")
    except Exception as e:
        logger.error(f"Error during text generation: {e}")
        generated_text = ""

    # If the model copied the prompt verbatim, remove it from the start
    if generated_text.startswith(prompt_text):
        generated_text = generated_text[len(prompt_text) :].strip()
        logger.debug("Removed prompt text from generated output.")

    # If empty, attempt again
    if not generated_text:
        logger.warning(f"No content generated for {model_name} - '{section}'.")
        if attempt < max_attempts:
            logger.info("Retrying generation...")
            return generate_section_for_model(
                model_name,
                section,
                task,
                attempt + 1,
                max_attempts,
            )
        logger.error(
            f"Max attempts reached for {model_name} - '{section}'. Returning empty string.",
        )
        return ""
    logger.info(f"Successfully generated content for {model_name} - '{section}'.")

    # 1) Refine if needed
    refined_text = refine_section_output(model_name, section, generated_text)
    # 2) Apply Jinja template
    final_text = apply_jinja_template(section, refined_text)

    return final_text


def generate_initial_response(structured_input: dict) -> dict:
    """
    Iterates over each model and each required section,
    generating a response using the language model.
    """
    logger.info("Starting initial response generation.")
    response = {}
    task = structured_input["task"]
    models = structured_input["models"]
    sections = structured_input["sections"]

    for model in models:
        logger.info(f"Generating responses for model: {model}")
        response[model] = {}
        for section in sections:
            section_output = generate_section_for_model(model, section, task)
            response[model][section] = section_output
            logger.debug(
                f"Generated + refined text for {model} - '{section}':\n{section_output[:80]}...",
            )
    logger.info("Initial response generation complete.")
    return response


# ------------------------------
# Component 3: Recursive Correction & Feedback Mechanism
# ------------------------------
def complete_response(response: dict, structured_input: dict) -> dict:
    """
    Checks each model's response for missing (empty) sections and regenerates content as needed.
    """
    logger.info("Starting recursive completion check for response.")
    expected_sections = structured_input["sections"]
    task = structured_input["task"]

    for model, sections_dict in response.items():
        for section in expected_sections:
            content = sections_dict.get(section, "")
            # If still empty, regenerate
            if not content.strip():
                logger.warning(
                    f"Missing content for {model} - '{section}'. Regenerating...",
                )
                new_text = generate_section_for_model(model, section, task)
                response[model][section] = new_text
                logger.info(f"Updated {model} - '{section}' with new content.")
            else:
                logger.debug(f"Section '{section}' for model '{model}' is non-empty.")
    logger.info("Response completion check finished.")
    return response


# ------------------------------
# Main: Putting it all together
# ------------------------------
def main():
    logger.info("Program started.")
    # Example user prompt
    user_prompt = (
        "Compare three different LLM architectures: GPT, Claude, and Mistral. Provide details on:\n"
        "1. Model architecture\n"
        "2. Training data and methodology\n"
        "3. Strengths & Weaknesses\n"
        "4. Real-world use cases"
    )

    # Step 1: Parse the prompt
    logger.info("Parsing user prompt...")
    structured_input = parse_input(user_prompt)
    logger.debug("Structured Input:\n" + json.dumps(structured_input, indent=2))

    # Step 2: Generate an initial response (with refinement & Jinja templating)
    logger.info("Generating initial AI response...")
    initial_response = generate_initial_response(structured_input)
    logger.debug("Initial Response:\n" + json.dumps(initial_response, indent=2))

    # Step 3: Recursively check and fill in any missing sections
    logger.info("Validating and completing AI response...")
    final_response = complete_response(initial_response, structured_input)
    logger.debug("Final Completed Response:\n" + json.dumps(final_response, indent=2))

    logger.info("Program finished. Final response:")
    print(json.dumps(final_response, indent=2))


if __name__ == "__main__":
    main()

"""Type Forge: Advanced type manipulation and verification system.

This module initializes the forge submodule of the type_forge package,
providing a comprehensive toolkit for type operations with mathematical precision.

The forge module offers capabilities for:
    * Type creation - Generate new types with precise constraints
    * Type validation - Verify values against type specifications
    * Type transformation - Convert between compatible types
    * Type introspection - Analyze type structures recursively
    * Type normalization - Standardize type representations
    * Type mapping - Apply transformations across type hierarchies
    * Type naming - Generate consistent, readable type identifiers
    * Type deduplication - Eliminate redundant type definitions
    * Type verification - Ensure type structure integrity
    * Type standardization - Convert types to canonical forms

Examples:
    Basic type validation::

        >>> from type_forge.forge import validate_type
        >>> result = validate_type(42, int)
        >>> assert result.valid

    Type conversion with verification::

        >>> from type_forge.forge import convert_type
        >>> converted = convert_type("42", int)
        >>> assert converted == 42

    Creating composite types::

        >>> from type_forge.forge import composite_type
        >>> OptionalInt = composite_type([int, type(None)])
        >>> assert is_type_of(None, OptionalInt)

    Analyzing type structure::

        >>> from type_forge.forge import inspect_type
        >>> type_info = inspect_type(dict[str, list[int]])
        >>> assert type_info.structure.component_types[1].component_types[0] == int

Notes:
    All functionality follows Eidosian principles of precision,
    recursive optimization, and perfect integration. The system
    maintains type safety at all abstraction levels while providing
    flexibility through well-defined transformation paths.

Attributes:
    __version__ (str): Version number following semantic versioning.
    __author__ (str): Package author and maintainer details.

See Also:
    - :mod:`type_forge.core`: Core type system components
    - :mod:`type_forge.typing`: Extended typing utilities
    - :mod:`type_forge.validators`: Validation framework
"""

from __future__ import annotations

from typing import List

from ..typing.variables import (
    R,  # Result type for operations
    S,  # Source type for conversions
    T,  # Generic invariant type
    T_co,  # Covariant type (produces values)
    T_contra,  # Contravariant type (consumes values)
    TypeVar,  # Import TypeVar which is used to define type variables
)

# Import core functionality with explicit imports grouped by functionality domain
# Import version information from the type_forge module
# Import the TypeForge class which is the main entry point for the forge module
from .type_forge import TypeForge, __author__, __version__

# Import public functionality from the TypeForge class and give it module-level access
# This provides a cleaner API while keeping the implementation details encapsulated
validate_type = TypeForge.validate_type
validate_dict_schema = TypeForge.validate_dict_schema
validate_recursive = TypeForge.validate_recursive

# Create instance of TypeForge for module-level access to instance methods
_forge = TypeForge()
create_type = _forge.create_type
validate = _forge.validate
validate_and_convert = _forge.validate_and_convert
check_type = _forge.check_type
assert_type = _forge.assert_type
convert_value = _forge.convert_value
safe_convert = _forge.safe_convert

# Public API with precise categorization and documentation
__all__: List[str] = [
    # Type creation - Generate new types with precise constraints
    "create_type",  # Create new types with specified attributes
    # Type validation - Verify values against type specifications
    "validate_type",  # Validate values against type specifications
    "validate",  # Verify that an object is an instance of a registered type
    "validate_dict_schema",  # Validate dictionary against schema
    "validate_recursive",  # Recursively validate complex structures
    "check_type",  # Simple type checking with boolean result
    "assert_type",  # Assert type with exception raising
    # Type conversion - Convert between compatible types
    "validate_and_convert",  # Validate and convert in one operation
    "convert_value",  # Convert with detailed result object
    "safe_convert",  # Convert with default fallback value
    # Version information - Package metadata
    "__version__",  # Package version following semantic versioning
    "__author__",  # Package author and maintainer details
    "R",  # Result type for operations
    "S",  # Source type for conversions
    "T",  # Generic invariant type
    "T_co",  # Covariant type (produces values)
    "T_contra",  # Contravariant type (consumes values)
    "TypeVar",  # Import TypeVar which is used to define type variables
]

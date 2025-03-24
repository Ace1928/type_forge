type_forge.core
===============

.. py:module:: type_forge.core

.. autoapi-nested-parse::

   Core module for the TypeForge type validation system.

   This module provides the essential components for runtime type validation,
   dynamic type creation, and structural type checking. It forms the backbone
   of the TypeForge framework, enabling precise control over data structures
   with minimal runtime overhead.

   The components in this module follow composition patterns with strict
   typing to ensure type safety throughout the validation pipeline. Each
   component has a single responsibility and communicates through well-defined
   interfaces.

   Architecture:
       TypeForgeBase: The root class establishing the type identity system
       BaseValidator: Validation interface with pure functional core
       ValidationResult: Immutable result structure with strict guarantees
       Exceptions: Specialized error hierarchy for precise error handling

   Exports:
       BaseValidator: Abstract base class defining the validator interface
           with validate() and is_valid() methods
       TypeForgeBase: Root class for all TypeForge objects providing common
           functionality and type identity
       ValidationResult: Immutable container for validation outcomes with
           status, value, and violation details
       ValidationError: Exception raised when validation fails with
           detailed violation information
       TypeForgeException: Base exception class for all TypeForge errors
           to enable specific error handling
       TypeCreationError: Exception raised when type construction fails
           due to invalid parameters or configuration
       ConfigurationError: Exception for invalid TypeForge configuration
           typically raised during initialization
       TypeViolation: Detailed information about a specific type violation
           including path, value, and violation kind
       TypeViolationKind: Enumeration of possible violation categories
           (e.g., type mismatch, missing field, extra field)

   .. admonition:: Example

      >>> from type_forge.core import ValidationResult, TypeForgeBase, TypeViolation, TypeViolationKind
      >>>
      >>> # Create a validation result for a successful validation
      >>> result = ValidationResult(valid=True, value=42, violations=[])
      >>> assert isinstance(result, TypeForgeBase)
      >>>
      >>> # Example with validation failure
      >>> violations = [TypeViolation(
      ...     path="age",
      ...     expected="int",
      ...     received="str",
      ...     value="twenty",
      ...     kind=TypeViolationKind.TYPE_MISMATCH
      ... )]
      >>> failed_result = ValidationResult(valid=False, value=None, violations=violations)
      >>> assert not failed_result.valid
      >>>
      >>> # Accessing violation details
      >>> if not failed_result.valid:
      ...     for violation in failed_result.violations:
      ...         print(f"Error at {violation.path}: Expected {violation.expected, got {violation.received}")

   .. admonition:: Notes

      All components maintain strict immutability to ensure thread safety and
      prevent side-effects during validation operations.

   .. seealso::

      type_forge.validators: Higher-level validation components
      type_forge.types: Type definition and construction utilities



Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/type_forge/core/base/index
   /autoapi/type_forge/core/exceptions/index


Exceptions
----------

.. autoapisummary::

   type_forge.core.ConfigurationError
   type_forge.core.TypeCreationError
   type_forge.core.TypeForgeException
   type_forge.core.ValidationError


Classes
-------

.. autoapisummary::

   type_forge.core.BaseValidator
   type_forge.core.TypeForgeBase
   type_forge.core.TypeViolation
   type_forge.core.TypeViolationKind
   type_forge.core.ValidationResult


Package Contents
----------------

.. py:exception:: ConfigurationError(message)

   Bases: :py:obj:`TypeForgeException`


   Exception raised for configuration-related errors.

   Raised when TypeForge is configured with invalid, incompatible,
   or missing configuration parameters.

   :param message: Descriptive error message explaining the configuration issue.

   .. rubric:: Examples

   ```python
   raise ConfigurationError("Invalid serialization format specified")
   ```

   Initialize with error message.

   :param message: Detailed description of the configuration error.


.. py:exception:: TypeCreationError(message)

   Bases: :py:obj:`TypeForgeException`


   Exception raised for errors during type creation.

   Raised when attempting to create a type definition fails due to
   invalid parameters, conflicting constraints, or other type
   construction issues.

   :param message: Descriptive error message explaining the type creation failure.

   .. rubric:: Examples

   ```python
   raise TypeCreationError("Cannot create recursive type without base case")
   ```

   Initialize with error message.

   :param message: Detailed description of the type creation error.


.. py:exception:: TypeForgeException

   Bases: :py:obj:`Exception`


   Base class for all exceptions raised by the TypeForge module.

   All exceptions in this library inherit from this class, enabling
   targeted exception handling for TypeForge-specific errors.

   .. rubric:: Examples

   ```python
   try:
       # Some TypeForge operation
       pass
   except TypeForgeException as e:
       # Handle any TypeForge-related error
       pass
   ```

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: ValidationError(message)

   Bases: :py:obj:`TypeForgeException`


   Exception raised for data validation errors.

   Raised when data fails to meet validation constraints defined
   in a type schema or validation rule.

   :param message: Descriptive error message explaining the validation failure.

   .. rubric:: Examples

   ```python
   raise ValidationError("Age must be greater than 0")
   ```

   Initialize with error message.

   :param message: Detailed description of the validation error.


.. py:class:: BaseValidator

   Base class for all validators in the type_forge framework.

   Provides the fundamental validation interface that all validators must implement,
   with support for both simple boolean validation and detailed validation results.

   Validators form the core of the type forge validation process, each implementing
   specific validation logic while adhering to a common interface that enables
   composition and chaining. This follows the "Composition Over Inheritance"
   principle from Eidosian design.

   The class follows the Template Method pattern, providing a default implementation
   of validate_with_detail that builds upon the abstract validate method
   that subclasses must implement.


   .. py:method:: validate(value)

      Validate the given value.

      This is the simplified validation interface that returns only a boolean result.
      Subclasses must implement this method to define specific validation logic.

      :param value: The value to validate
      :type value: object

      :returns: True if the value is valid, False otherwise
      :rtype: bool

      :raises NotImplementedError: If the subclass doesn't implement this method



   .. py:method:: validate_with_detail(value)

      Validate the given value with detailed results.

      Provides comprehensive validation information including specific violations
      and an optionally converted value. This implementation relies on the simple
      validate method, but subclasses may override for more detailed reporting.

      This method demonstrates the recursive refinement principle by building
      detailed validation upon the simpler boolean validation. It also implements
      the "Errors as Values" principle by encapsulating failures in the return
      type rather than through exceptions.

      :param value: The value to validate
      :type value: object

      :returns: Detailed validation results with type preservation
      :rtype: ValidationResult[object]

      :raises No direct exceptions, but captures exceptions from validate() and:
      :raises converts them to ValidationResult with appropriate violations:



.. py:class:: TypeForgeBase

   Base class for the type forging process.

   Orchestrates validation through multiple validators, providing both
   simple boolean validation and detailed validation results with proper
   type preservation.

   The TypeForgeBase implements the composition pattern, allowing multiple
   validators to be combined while maintaining a consistent interface
   and preserving type information throughout the validation process.
   This embodies the Eidosian principle of "Fractal Coherence" where
   complex validation logic emerges from simpler components in a
   consistent manner.

   .. rubric:: Attributes

   validators (List[BaseValidator]): List of validators to apply during validation

   Initialize with an empty validators list.

   Creates a new TypeForgeBase instance with no validators.
   Validators must be added using the add_validator method.
   This follows the "Data Before Behavior" principle by establishing
   the core data structure before defining operations on it.


   .. py:method:: add_validator(validator)

      Add a validator to the type forging process.

      Appends a validator to the internal list of validators that will
      be applied during validation operations. This method implements
      the builder pattern for constructing validation chains.

      :param validator: An instance of a validator
      :type validator: BaseValidator

      :raises TypeError: If validator is not an instance of BaseValidator



   .. py:method:: validate(value)

      Validate a value against all registered validators.

      Performs sequential validation using all registered validators,
      implementing the fail-fast principle by short-circuiting on the first failure
      for efficient validation.

      This method provides a simplified boolean interface to the validation
      process, while maintaining full compatibility with the type registration
      and validation system used throughout TypeForge.

      :param value: The value to validate against the validators
                    in this TypeForgeBase instance
      :type value: object

      :returns: True if the value passes all validators, False otherwise
      :rtype: bool

      .. rubric:: Examples

      >>> validator = TypeForgeBase()
      >>> validator.add_validator(IntegerValidator())
      >>> validator.validate(42)
      True
      >>> validator.validate("not an integer")
      False



   .. py:method:: validate_with_detail(value)

      Validate with detailed results from all validators.

      Aggregates validation results from all validators, maintaining a comprehensive
      record of any violations that occur while preserving type safety.

      Unlike the simple validate method, this continues to run all validators
      even after failures to collect complete violation information.
      This implementation balances efficiency with completeness, providing
      full failure details for better debugging and error reporting.

      :param value: The value to validate
      :type value: object

      :returns: Aggregated validation details with type preservation
      :rtype: ValidationResult[object]



   .. py:attribute:: validators
      :type:  List[BaseValidator]
      :value: []



.. py:class:: TypeViolation

   Immutable record of a type violation with path tracking.

   Provides a structured representation of a type violation with
   context information for precise error reporting and diagnosis.
   The frozen dataclass ensures immutability for safer error handling.

   .. rubric:: Attributes

   path: JSON path to the location of the violation.
   expected: Description of expected type or value.
   found: Description of actual type or value found.
   kind: Category of violation from TypeViolationKind.

   .. rubric:: Examples

   ```python
   violation = TypeViolation(
       path="user.address.zipcode",
       expected="string of 5 digits",
       found="'ABC123'",
       kind=TypeViolationKind.INVALID_VALUE
   )
   ```


   .. py:method:: __str__()

      Generate human-readable representation of the violation.

      :returns: Formatted string with violation details including path,
                expected value, found value, and violation kind.



   .. py:attribute:: expected
      :type:  str


   .. py:attribute:: found
      :type:  str


   .. py:attribute:: kind
      :type:  TypeViolationKind


   .. py:attribute:: path
      :type:  str


.. py:class:: TypeViolationKind(*args, **kwds)

   Bases: :py:obj:`enum.Enum`


   Enumeration of possible type violation categories.

   Provides a structured taxonomy of type violations for precise
   error categorization and handling.

   .. rubric:: Attributes

   WRONG_TYPE: Value has incorrect type.
   MISSING_KEY: Required key is absent.
   INVALID_VALUE: Value fails validation constraints.
   SCHEMA_MISMATCH: Value structure doesn't match schema.
   CONVERSION_ERROR: Type conversion failed.

   .. rubric:: Examples

   ```python
   if isinstance(value, str):
       return TypeViolationKind.WRONG_TYPE
   ```


   .. py:method:: __str__()

      Generate string representation of the violation kind.

      :returns: The string value of the enumeration.



   .. py:attribute:: CONVERSION_ERROR
      :value: 'conversion_error'



   .. py:attribute:: INVALID_VALUE
      :value: 'invalid_value'



   .. py:attribute:: MISSING_KEY
      :value: 'missing_key'



   .. py:attribute:: SCHEMA_MISMATCH
      :value: 'schema_mismatch'



   .. py:attribute:: WRONG_TYPE
      :value: 'wrong_type'



.. py:class:: ValidationResult

   Bases: :py:obj:`Generic`\ [\ :py:obj:`type_forge.typing.definitions.T`\ ]


   Result of type validation with possible conversion.

   This class encapsulates the outcome of a validation operation, including
   whether validation passed, any violations that occurred, and an optional
   converted value that maintains its type through generic constraints.

   The ValidationResult maintains type safety through covariant generics,
   ensuring that type information flows correctly through validation chains
   and transformations. It acts as both a container for validation status
   and a monad-like structure that can be composed and transformed while
   preserving the validation context.

   .. rubric:: Attributes

   valid (bool): Boolean indicating if validation succeeded
   violations (List[TypeViolation]): List of specific type violations encountered
   converted_value (Optional[T]): Optional transformed value that maintains
       its type through generics

   .. rubric:: Examples

   >>> result = ValidationResult[int](valid=True, converted_value=42)
   >>> bool(result)
   True
   >>> result.with_converted_value("string")
   ValidationResult(valid=True, violations=[], converted_value='string')


   .. py:method:: __bool__()

      Boolean conversion returns validation status.

      Allows ValidationResult objects to be used directly in boolean contexts
      for streamlined conditional logic, implementing the "errors as values"
      pattern in an elegant, composable way.

      :returns: True if validation passed, False otherwise
      :rtype: bool



   .. py:method:: merge(other)

      Merge another validation result into this one.

      This maintains the type of the original result while incorporating
      the validation status and violations from another result. The converted
      value remains that of the original result, preserving type integrity.

      This method enables recursive composition of validation results,
      allowing complex validation logic to be built from simpler components
      while maintaining full type safety.

      :param other: Another validation result to merge with this one
      :type other: ValidationResult[object]

      :returns: Self with merged validation status and violations
      :rtype: ValidationResult[T]



   .. py:method:: with_converted_value(value)

      Create a new ValidationResult with the same validation status but a different value.

      This method preserves the validation state while transforming the result
      to contain a new value of potentially different type, properly maintaining
      type safety through generics. This enables validation pipelines that
      transform data while maintaining error context.

      The implementation follows the principle of "Pure Core, Effects at Edges"
      by returning a new instance rather than modifying the current one,
      maintaining immutability for better compositional properties.

      :param value: The converted value to set
      :type value: S

      :returns: A new ValidationResult with the same validation status but different value
      :rtype: ValidationResult[S]



   .. py:attribute:: converted_value
      :type:  Optional[type_forge.typing.definitions.T]
      :value: None



   .. py:attribute:: valid
      :type:  bool


   .. py:attribute:: violations
      :type:  List[type_forge.core.exceptions.TypeViolation]
      :value: []




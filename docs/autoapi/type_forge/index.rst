type_forge
==========

.. py:module:: type_forge

.. autoapi-nested-parse::

   Type Forge: A module for dynamic type validation and transformation with recursive precision.

   This module serves as the entry point for the Type Forge framework,
   providing a unified interface for dynamic type creation, validation,
   and transformation with structural integrity and recursive precision.

   The TypeForge framework enables:
       - Dynamic type creation with strict validation guarantees
       - Recursive schema validation with elegant error handling
       - Type conversion with compile-time and runtime safety
       - Structural integrity verification through composable validators

   Modules:
       core: Contains base classes, protocols, and exceptions for type validation
       forge: Implements the main TypeForge class and associated functionality
       validators: Provides specialized validators for comprehensive type checking
       typing: Type definitions, protocols, and type-related utilities
       utils: General utility functions for type manipulation and formatting

   Classes:
       TypeForge: Main entry point for dynamic type creation and validation
       BasicValidator: Foundation validator for simple type validation
       CompositeValidator: Combines multiple validators for complex validation
       ValidationResult: Immutable result of a validation operation
       TypeViolation: Precisely describes a type violation with context
       TypeViolationKind: Enumeration of possible validation failure types
       ValidatorFactory: Creates specialized validators for diverse scenarios

   Functions:
       format_validation_error(violation: TypeViolation) -> str:
           Formats type violations as human-readable error messages
       deduplicate_violations(violations: Sequence[TypeViolation]) -> List[TypeViolation]:
           Removes duplicate violations while preserving order and context
       is_valid_type_descriptor(value: Any) -> bool:
           Determines if a value can serve as a valid type descriptor

   Typical usage example:
       >>> from type_forge import TypeForge
       >>> forge = TypeForge()
       >>> UserSchema = forge.create({
       ...     "name": str,
       ...     "age": int,
       ...     "email": forge.Email()
       ... })
       >>> user = UserSchema(name="Alice", age=30, email="alice@example.com")



Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/type_forge/core/index
   /autoapi/type_forge/forge/index
   /autoapi/type_forge/typing/index
   /autoapi/type_forge/utils/index
   /autoapi/type_forge/validators/index


Attributes
----------

.. autoapisummary::

   type_forge.ValidationContext


Classes
-------

.. autoapisummary::

   type_forge.TypeViolation
   type_forge.TypeViolationKind
   type_forge.ValidationResult


Package Contents
----------------

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



.. py:data:: ValidationContext

   Context for validation process with shared state.

   Environmental information affecting validation decisions.


type_forge.validators
=====================

.. py:module:: type_forge.validators

.. autoapi-nested-parse::

   This module initializes the validators submodule of the type_forge package.

   It provides a centralized interface for importing various validators, allowing for
   modular design and easy access to validation functionalities.

   Available Validators:
   - Basic Validators
   - Composite Validators
   - Validator Factory



Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/type_forge/validators/basic/index
   /autoapi/type_forge/validators/composite/index
   /autoapi/type_forge/validators/factory/index


Attributes
----------

.. autoapisummary::

   type_forge.validators.DictSchemaT
   type_forge.validators.ParentSpecType
   type_forge.validators.SchemaTypeT
   type_forge.validators.T
   type_forge.validators.T
   type_forge.validators.T
   type_forge.validators.T
   type_forge.validators.V
   type_forge.validators.version


Classes
-------

.. autoapisummary::

   type_forge.validators.BaseValidator
   type_forge.validators.BaseValidator
   type_forge.validators.BasicValidator
   type_forge.validators.BasicValidator
   type_forge.validators.CompositeValidator
   type_forge.validators.CompositeValidator
   type_forge.validators.SupportsBoolConversion
   type_forge.validators.SupportsFloat
   type_forge.validators.SupportsFloatConversion
   type_forge.validators.SupportsInt
   type_forge.validators.SupportsIntConversion
   type_forge.validators.TypeViolation
   type_forge.validators.TypeViolation
   type_forge.validators.TypeViolation
   type_forge.validators.TypeViolationKind
   type_forge.validators.TypeViolationKind
   type_forge.validators.TypeViolationKind
   type_forge.validators.ValidationIssue
   type_forge.validators.ValidationReport
   type_forge.validators.ValidationResult
   type_forge.validators.ValidationResult
   type_forge.validators.ValidationResult
   type_forge.validators.ValidatorFactory


Functions
---------

.. autoapisummary::

   type_forge.validators.are_types_compatible
   type_forge.validators.has_attributes
   type_forge.validators.is_callable
   type_forge.validators.is_collection
   type_forge.validators.is_compatible_with_type
   type_forge.validators.is_function
   type_forge.validators.is_in_range
   type_forge.validators.is_instance_of_any
   type_forge.validators.is_method
   type_forge.validators.is_non_empty_string
   type_forge.validators.is_not_empty
   type_forge.validators.is_numeric
   type_forge.validators.is_positive
   type_forge.validators.is_protocol_instance
   type_forge.validators.is_subclass_safe
   type_forge.validators.is_valid_identifier
   type_forge.validators.is_valid_length


Package Contents
----------------

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



.. py:class:: BasicValidator

   Bases: :py:obj:`type_forge.core.base.BaseValidator`


   A class for basic data type validators.


   .. py:method:: safe_bool_convert(value)
      :staticmethod:


      Safely convert a value to bool with semantic interpretation.

      :param value: Any value that might be convertible to bool

      :returns: A bool representation of the value, with common string patterns
                like "yes"/"no" properly handled



   .. py:method:: safe_float_convert(value)
      :staticmethod:


      Safely convert a value to float or return None if invalid.

      :param value: Any value that might be convertible to float

      :returns: A float value or None if conversion is not possible



   .. py:method:: safe_int_convert(value)
      :staticmethod:


      Safely convert a value to int or return None if invalid.

      :param value: Any value that might be convertible to int

      :returns: An int value or None if conversion is not possible



   .. py:method:: safe_str_convert(value)
      :staticmethod:


      Safely convert a value to string with proper handling of various types.

      :param value: Any value to convert to string

      :returns: String representation of the value



   .. py:method:: validate(value)

      Base validation method for the BasicValidator.

      :param value: The value to validate

      :returns: True if validation succeeds, False otherwise



   .. py:method:: validate_boolean(value)
      :staticmethod:


      Validate that the value is a boolean.

      :param value: The value to validate

      :returns: The validated boolean

      :raises ValueError: If the value is not a boolean



   .. py:method:: validate_dict(value, key_type, value_type)
      :staticmethod:


      Validate that the value is a dictionary with specific key and value types.

      :param value: The value to validate
      :param key_type: The expected type of keys in the dictionary
      :param value_type: The expected type of values in the dictionary

      :returns: The validated dictionary

      :raises ValueError: If the value is not a dictionary or contains keys/values of the wrong type



   .. py:method:: validate_float(value)
      :staticmethod:


      Validate that the value is a float.

      :param value: The value to validate

      :returns: The validated float

      :raises ValueError: If the value is not a float



   .. py:method:: validate_integer(value)
      :staticmethod:


      Validate that the value is an integer.

      :param value: The value to validate

      :returns: The validated integer

      :raises ValueError: If the value is not an integer



   .. py:method:: validate_list(value, item_type)
      :staticmethod:


      Validate that the value is a list of a specific item type.

      :param value: The value to validate
      :param item_type: The expected type of items in the list

      :returns: The validated list

      :raises ValueError: If the value is not a list or contains items of the wrong type



   .. py:method:: validate_string(value)
      :staticmethod:


      Validate that the value is a string.

      :param value: The value to validate

      :returns: The validated string

      :raises ValueError: If the value is not a string



   .. py:method:: validate_with_detail(value)

      Validate with detailed information.

      :param value: The value to validate

      :returns: ValidationResult with detailed information



.. py:class:: BasicValidator

   Bases: :py:obj:`type_forge.core.base.BaseValidator`


   A class for basic data type validators.


   .. py:method:: safe_bool_convert(value)
      :staticmethod:


      Safely convert a value to bool with semantic interpretation.

      :param value: Any value that might be convertible to bool

      :returns: A bool representation of the value, with common string patterns
                like "yes"/"no" properly handled



   .. py:method:: safe_float_convert(value)
      :staticmethod:


      Safely convert a value to float or return None if invalid.

      :param value: Any value that might be convertible to float

      :returns: A float value or None if conversion is not possible



   .. py:method:: safe_int_convert(value)
      :staticmethod:


      Safely convert a value to int or return None if invalid.

      :param value: Any value that might be convertible to int

      :returns: An int value or None if conversion is not possible



   .. py:method:: safe_str_convert(value)
      :staticmethod:


      Safely convert a value to string with proper handling of various types.

      :param value: Any value to convert to string

      :returns: String representation of the value



   .. py:method:: validate(value)

      Base validation method for the BasicValidator.

      :param value: The value to validate

      :returns: True if validation succeeds, False otherwise



   .. py:method:: validate_boolean(value)
      :staticmethod:


      Validate that the value is a boolean.

      :param value: The value to validate

      :returns: The validated boolean

      :raises ValueError: If the value is not a boolean



   .. py:method:: validate_dict(value, key_type, value_type)
      :staticmethod:


      Validate that the value is a dictionary with specific key and value types.

      :param value: The value to validate
      :param key_type: The expected type of keys in the dictionary
      :param value_type: The expected type of values in the dictionary

      :returns: The validated dictionary

      :raises ValueError: If the value is not a dictionary or contains keys/values of the wrong type



   .. py:method:: validate_float(value)
      :staticmethod:


      Validate that the value is a float.

      :param value: The value to validate

      :returns: The validated float

      :raises ValueError: If the value is not a float



   .. py:method:: validate_integer(value)
      :staticmethod:


      Validate that the value is an integer.

      :param value: The value to validate

      :returns: The validated integer

      :raises ValueError: If the value is not an integer



   .. py:method:: validate_list(value, item_type)
      :staticmethod:


      Validate that the value is a list of a specific item type.

      :param value: The value to validate
      :param item_type: The expected type of items in the list

      :returns: The validated list

      :raises ValueError: If the value is not a list or contains items of the wrong type



   .. py:method:: validate_string(value)
      :staticmethod:


      Validate that the value is a string.

      :param value: The value to validate

      :returns: The validated string

      :raises ValueError: If the value is not a string



   .. py:method:: validate_with_detail(value)

      Validate with detailed information.

      :param value: The value to validate

      :returns: ValidationResult with detailed information



.. py:class:: CompositeValidator(validators)

   Bases: :py:obj:`type_forge.core.base.BaseValidator`, :py:obj:`Generic`\ [\ :py:obj:`T`\ ]


   A validator that combines multiple validators.

   Initialize a composite validator with a list of validator functions.

   :param validators: List of validator functions that take a value and return a boolean


   .. py:method:: __call__(value)

      Make the validator callable directly.

      :param value: The value to validate

      :returns: Result of validate(value)



   .. py:method:: add_validator(validator)

      Add a new validator to the composite.

      :param validator: A function that takes a value and returns a boolean



   .. py:method:: from_validators(validators)
      :staticmethod:


      Create a CompositeValidator from a sequence of BaseValidator instances.

      :param validators: A sequence of BaseValidator instances

      :returns: A new CompositeValidator that aggregates all the validators



   .. py:method:: validate(value)

      Validate a value using all validators in the composite.

      :param value: The value to validate

      :returns: True if all validators return True, False otherwise



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



   .. py:method:: validate_with_details(value, path = '$')

      Validate with detailed result information.

      :param value: The value to validate
      :param path: The path to report in case of violations

      :returns: A ValidationResult with detailed information



   .. py:attribute:: validators


.. py:class:: CompositeValidator(validators)

   Bases: :py:obj:`type_forge.core.base.BaseValidator`, :py:obj:`Generic`\ [\ :py:obj:`T`\ ]


   A validator that combines multiple validators.

   Initialize a composite validator with a list of validator functions.

   :param validators: List of validator functions that take a value and return a boolean


   .. py:method:: __call__(value)

      Make the validator callable directly.

      :param value: The value to validate

      :returns: Result of validate(value)



   .. py:method:: add_validator(validator)

      Add a new validator to the composite.

      :param validator: A function that takes a value and returns a boolean



   .. py:method:: from_validators(validators)
      :staticmethod:


      Create a CompositeValidator from a sequence of BaseValidator instances.

      :param validators: A sequence of BaseValidator instances

      :returns: A new CompositeValidator that aggregates all the validators



   .. py:method:: validate(value)

      Validate a value using all validators in the composite.

      :param value: The value to validate

      :returns: True if all validators return True, False otherwise



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



   .. py:method:: validate_with_details(value, path = '$')

      Validate with detailed result information.

      :param value: The value to validate
      :param path: The path to report in case of violations

      :returns: A ValidationResult with detailed information



   .. py:attribute:: validators


.. py:class:: SupportsBoolConversion

   Bases: :py:obj:`Protocol`


   Protocol for types that can be converted to bool.

   This protocol defines the interface for objects that support
   conversion to boolean values through the __bool__ method.

   .. rubric:: Examples

   >>> class CustomBoolean:
   ...     def __init__(self, value: bool) -> None:
   ...         self.value = value
   ...     def __bool__(self) -> bool:
   ...         return self.value
   >>> bool(CustomBoolean(True))  # True


   .. py:method:: __bool__()

      Convert to boolean.

      :returns: Boolean representation of the object.
      :rtype: bool



.. py:class:: SupportsFloat

   Bases: :py:obj:`Protocol`


   Protocol for objects that support conversion to float.


   .. py:method:: __float__()


.. py:class:: SupportsFloatConversion

   Bases: :py:obj:`Protocol`


   Protocol for types that can be converted to float.

   This protocol defines the interface for objects that support
   conversion to floating-point values through the __float__ method.

   .. rubric:: Examples

   >>> class CustomFloat:
   ...     def __init__(self, value: float) -> None:
   ...         self.value = value
   ...     def __float__(self) -> float:
   ...         return self.value
   >>> float(CustomFloat(3.14))  # 3.14


   .. py:method:: __float__()

      Convert to float.

      :returns: Floating-point representation of the object.
      :rtype: float



.. py:class:: SupportsInt

   Bases: :py:obj:`Protocol`


   Protocol for objects that support conversion to int.


   .. py:method:: __int__()


.. py:class:: SupportsIntConversion

   Bases: :py:obj:`Protocol`


   Protocol for types that can be converted to int.

   This protocol defines the interface for objects that support
   conversion to integer values through the __int__ method.

   .. rubric:: Examples

   >>> class CustomInteger:
   ...     def __init__(self, value: int) -> None:
   ...         self.value = value
   ...     def __int__(self) -> int:
   ...         return self.value
   >>> isinstance(CustomInteger(42), SupportsIntConversion)  # True at runtime


   .. py:method:: __int__()

      Convert to integer.

      :returns: Integer representation of the object.
      :rtype: int



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



.. py:class:: ValidationIssue(severity, message, path = None, context = None)

   Detailed representation of a validation issue with context and severity.

   This class encapsulates information about a validation issue, including
   its severity, location, message, and contextual information for debugging
   and correction.

   .. rubric:: Attributes

   severity (ValidationSeverity): The severity level of the issue
   message (str): Human-readable description of the issue
   path (Optional[str]): Path to the location of the issue (e.g., "user.address.city")
   context (Dict[str, object]): Additional contextual information about the issue

   .. rubric:: Examples

   >>> issue = ValidationIssue(ValidationSeverity.ERROR, "Invalid email format")
   >>> issue.severity.name
   'ERROR'
   >>> issue.message
   'Invalid email format'
   >>> detailed = ValidationIssue(
   ...     ValidationSeverity.WARNING,
   ...     "Value outside recommended range",
   ...     path="settings.timeout",
   ...     context={"value": 120, "recommended_max": 60}
   ... )
   >>> detailed.path
   'settings.timeout'

   Initialize a ValidationIssue.

   :param severity: The severity level of the issue
   :param message: Human-readable description of the issue
   :param path: Path to the location of the issue (e.g., "user.address.city")
   :param context: Additional contextual information about the issue


   .. py:method:: __str__()

      String representation of the validation issue.

      :returns: Formatted description of the issue
      :rtype: str

      .. rubric:: Examples

      >>> str(ValidationIssue(ValidationSeverity.ERROR, "Invalid data"))
      'ERROR: Invalid data'
      >>> str(ValidationIssue(ValidationSeverity.WARNING, "Unusual value", path="config.timeout"))
      'WARNING at config.timeout: Unusual value'



   .. py:method:: is_blocker()

      Check if this issue should block operation.

      :returns: True if this issue should prevent operation
      :rtype: bool

      .. rubric:: Examples

      >>> issue = ValidationIssue(ValidationSeverity.FATAL, "Security violation")
      >>> issue.is_blocker()
      True
      >>> warning = ValidationIssue(ValidationSeverity.ERROR, "Data inconsistency")
      >>> warning.is_blocker()
      False



   .. py:method:: is_error()

      Check if this issue is an error.

      :returns: True if this is an error or fatal issue
      :rtype: bool

      .. rubric:: Examples

      >>> issue = ValidationIssue(ValidationSeverity.ERROR, "Invalid input")
      >>> issue.is_error()
      True
      >>> warning = ValidationIssue(ValidationSeverity.WARNING, "Unusual value")
      >>> warning.is_error()
      False



   .. py:attribute:: context
      :type:  Dict[str, object]


   .. py:attribute:: message
      :type:  str


   .. py:attribute:: path
      :type:  Optional[str]
      :value: None



   .. py:attribute:: severity
      :type:  type_forge.typing.definitions.ValidationSeverity


.. py:class:: ValidationReport

   Comprehensive report of validation results including all issues found.

   This class collects and organizes validation issues, providing methods
   to query and analyze validation results in detail.

   .. rubric:: Attributes

   issues (List[ValidationIssue]): List of all validation issues found

   .. rubric:: Examples

   >>> report = ValidationReport()
   >>> report.add_error("Invalid email")
   >>> report.add_warning("Name unusually short", path="user.name")
   >>> report.is_valid()
   False
   >>> report.has_warnings()
   True
   >>> len(report.get_issues())
   2

   Initialize an empty ValidationReport.


   .. py:method:: __bool__()

      Boolean evaluation of validation success.

      :returns: True if validation passed (no errors), False otherwise
      :rtype: bool

      .. rubric:: Examples

      >>> report = ValidationReport()
      >>> bool(report)
      True
      >>> report.add_error("Problem found")
      >>> bool(report)
      False



   .. py:method:: __str__()

      String representation of the validation report.

      :returns: Summary of validation results
      :rtype: str

      .. rubric:: Examples

      >>> report = ValidationReport()
      >>> str(report)
      'Validation passed with 0 issues'
      >>> report.add_error("Problem 1")
      >>> report.add_warning("Minor issue")
      >>> str(report)
      'Validation failed with 2 issues (1 errors, 1 warnings)'



   .. py:method:: add_error(message, path = None, context = None)

      Add an error issue to the report.

      :param message: Description of the error
      :type message: str
      :param path: Path to the location of the error. Defaults to None.
      :type path: Optional[str], optional
      :param context: Additional contextual information. Defaults to None.
      :type context: Optional[Dict[str, object]], optional

      .. rubric:: Examples

      >>> report = ValidationReport()
      >>> report.add_error("Invalid email format", path="user.email")
      >>> report.issues[0].severity
      <ValidationSeverity.ERROR: 'error'>



   .. py:method:: add_info(message, path = None, context = None)

      Add an informational issue to the report.

      :param message: Informational message
      :type message: str
      :param path: Path related to the information. Defaults to None.
      :type path: Optional[str], optional
      :param context: Additional contextual information. Defaults to None.
      :type context: Optional[Dict[str, object]], optional

      .. rubric:: Examples

      >>> report = ValidationReport()
      >>> report.add_info("Using default value", path="config.timeout")
      >>> report.issues[0].severity
      <ValidationSeverity.INFO: 'info'>



   .. py:method:: add_issue(issue)

      Add a validation issue to the report.

      :param issue: The validation issue to add
      :type issue: ValidationIssue

      .. rubric:: Examples

      >>> report = ValidationReport()
      >>> report.add_issue(ValidationIssue(ValidationSeverity.ERROR, "Invalid data"))
      >>> len(report.issues)
      1



   .. py:method:: add_warning(message, path = None, context = None)

      Add a warning issue to the report.

      :param message: Description of the warning
      :type message: str
      :param path: Path to the location of the warning. Defaults to None.
      :type path: Optional[str], optional
      :param context: Additional contextual information. Defaults to None.
      :type context: Optional[Dict[str, object]], optional

      .. rubric:: Examples

      >>> report = ValidationReport()
      >>> report.add_warning("Unusual value", path="settings.timeout")
      >>> report.issues[0].severity
      <ValidationSeverity.WARNING: 'warning'>



   .. py:method:: can_proceed()

      Check if operation can proceed despite validation issues.

      :returns: True if there are no blocking issues, False otherwise
      :rtype: bool

      .. rubric:: Examples

      >>> report = ValidationReport()
      >>> report.add_error("Non-fatal issue")
      >>> report.can_proceed()  # Regular errors don't block
      True
      >>> report.add_issue(ValidationIssue(ValidationSeverity.FATAL, "Security violation"))
      >>> report.can_proceed()
      False



   .. py:method:: get_errors()

      Get all error issues (ERROR and FATAL).

      :returns: List of error issues
      :rtype: List[ValidationIssue]

      .. rubric:: Examples

      >>> report = ValidationReport()
      >>> report.add_error("Error 1")
      >>> report.add_issue(ValidationIssue(ValidationSeverity.FATAL, "Fatal error"))
      >>> report.add_warning("Warning 1")
      >>> len(report.get_errors())
      2



   .. py:method:: get_issues(severity = None)

      Get validation issues, optionally filtered by severity.

      :param severity: If provided, only return issues of this severity.
                       Defaults to None.
      :type severity: Optional[ValidationSeverity], optional

      :returns: List of matching issues
      :rtype: List[ValidationIssue]

      .. rubric:: Examples

      >>> report = ValidationReport()
      >>> report.add_error("Error 1")
      >>> report.add_warning("Warning 1")
      >>> report.add_info("Info message")
      >>> len(report.get_issues())
      3
      >>> len(report.get_issues(ValidationSeverity.ERROR))
      1



   .. py:method:: get_warnings()

      Get all warning issues.

      :returns: List of warning issues
      :rtype: List[ValidationIssue]

      .. rubric:: Examples

      >>> report = ValidationReport()
      >>> report.add_warning("Warning 1")
      >>> report.add_warning("Warning 2")
      >>> report.add_error("Error 1")
      >>> len(report.get_warnings())
      2



   .. py:method:: has_warnings()

      Check if the report contains any warnings.

      :returns: True if warnings were found, False otherwise
      :rtype: bool

      .. rubric:: Examples

      >>> report = ValidationReport()
      >>> report.has_warnings()
      False
      >>> report.add_warning("Potential issue")
      >>> report.has_warnings()
      True



   .. py:method:: is_valid()

      Check if the validation passed with no errors.

      :returns: True if no errors were found, False otherwise
      :rtype: bool

      .. rubric:: Examples

      >>> report = ValidationReport()
      >>> report.is_valid()
      True
      >>> report.add_warning("Minor issue")
      >>> report.is_valid()  # Warnings don't invalidate
      True
      >>> report.add_error("Serious problem")
      >>> report.is_valid()
      False



   .. py:attribute:: issues
      :type:  List[ValidationIssue]
      :value: []



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



.. py:class:: ValidatorFactory

   Factory class for creating validators dynamically with type safety.

   This class provides static methods for creating various types of validators
   and performing validation operations with comprehensive error reporting.

   The factory pattern enables consistent validator creation with proper
   configuration and composition, supporting both simple and complex
   validation scenarios.


   .. py:method:: _get_type_name(typ)
      :staticmethod:


      Get a human-readable name for a type or type collection.

      :param typ: A type, tuple of types, or list/sequence of types

      :returns: A string representation of the type(s)



   .. py:method:: _try_convert(value, target_type)
      :staticmethod:


      Try to convert a value to the target type.

      :param value: Value to convert
      :param target_type: Type to convert to

      :returns: Converted value or None if conversion failed

      .. note:: This is an internal method used by validate_type.



   .. py:method:: create_validator(validator_type, **kwargs)
      :staticmethod:


      Creates a validator based on the specified type.

      :param validator_type: The type of validator to create.
                             Must be one of the supported validator types ('basic', 'composite').
      :param \*\*kwargs: Additional parameters for the validator.
                         Passed directly to the validator constructor.

      :returns: An instance of the requested validator.

      :raises ValueError: If the validator type is unknown.

      .. rubric:: Examples

      >>> validator = ValidatorFactory.create_validator('basic')
      >>> validator(42)
      True



   .. py:method:: validate_dict(value, schema, path = '$', convert = False, require_all_keys = True)
      :staticmethod:


      Validate that a dictionary conforms to a schema.

      :param value: Dictionary to validate
      :param schema: Schema defining expected types for keys
      :param path: Current path for error reporting
      :param convert: Whether to attempt type conversion
      :param require_all_keys: Whether all schema keys must be present

      :returns: ValidationResult with validation status and converted dict if applicable

      .. rubric:: Examples

      >>> schema = {"name": str, "age": int}
      >>> data = {"name": "Alice", "age": 30}
      >>> result = ValidatorFactory.validate_dict(data, schema)
      >>> result.valid
      True

      >>> data = {"name": "Bob"}  # Missing 'age'
      >>> result = ValidatorFactory.validate_dict(data, schema)
      >>> result.valid
      False



   .. py:method:: validate_recursive(value, schema, path = '$', convert = False)
      :staticmethod:


      Recursively validate a value against a schema of arbitrary complexity.

      :param value: Value to validate
      :param schema: Schema to validate against (dict, list/sequence, or type)
      :param path: Current path for error reporting
      :param convert: Whether to attempt type conversion

      :returns: ValidationResult with validation status and details

      .. rubric:: Examples

      >>> schema = {"name": str, "age": int}
      >>> data = {"name": "Alice", "age": 30}
      >>> result = ValidatorFactory.validate_recursive(data, schema)
      >>> result.valid
      True

      >>> data = {"name": "Alice", "age": "30"}
      >>> result = ValidatorFactory.validate_recursive(data, schema, convert=True)
      >>> result.valid
      True
      >>> result.converted_value  # doctest: +SKIP
      {'name': 'Alice', 'age': 30}



   .. py:method:: validate_type(value, expected_type, path = '$', convert = False)
      :staticmethod:


      Validate that a value matches the expected type recursively.

      :param value: The value to check
      :param expected_type: Type or types to check against
      :param path: Current path in the validation (for error reporting)
      :param convert: Whether to attempt conversion to the expected type

      :returns: ValidationResult with validation status and details

      .. rubric:: Examples

      >>> result = ValidatorFactory.validate_type(42, int)
      >>> result.valid
      True

      >>> result = ValidatorFactory.validate_type("42", int, convert=True)
      >>> result.valid
      True
      >>> result.converted_value
      42



.. py:function:: are_types_compatible(source_type, target_type)

   Check if two types are compatible for conversion or assignment.

   Determines whether values of the source type can generally be
   converted to the target type without errors.

   :param source_type: The source type to check from
   :param target_type: The target type to check compatibility with

   :returns: True if the types are compatible, False otherwise
   :rtype: bool

   .. rubric:: Examples

   >>> are_types_compatible(int, float)
   True
   >>> are_types_compatible(float, int)
   True
   >>> are_types_compatible(list, tuple)
   True
   >>> are_types_compatible(dict, list)
   False

   .. note::

      This evaluates type compatibility at a general level without
      considering specific value constraints.


.. py:function:: has_attributes(obj, *attributes)

   Check if an object has all the specified attributes.

   :param obj: The object to check
   :param \*attributes: Attribute names to look for

   :returns: True if object has all attributes, False otherwise
   :rtype: bool

   .. rubric:: Examples

   >>> has_attributes([], "append", "extend")
   True
   >>> has_attributes({}, "update", "missing_attr")
   False
   >>> has_attributes("string", "upper", "lower")
   True
   >>> has_attributes(None, "any_attr")
   False

   .. note:: This checks for attribute existence, not their values or callability.


.. py:function:: is_callable(value)

   Check if a value is callable (function, method, callable object).

   Determines whether an object can be called like a function.

   :param value: The value to check

   :returns: True if the value is callable, False otherwise
   :rtype: bool

   .. rubric:: Examples

   >>> is_callable(lambda x: x)
   True
   >>> is_callable(print)
   True
   >>> is_callable("not_callable")
   False
   >>> is_callable(None)
   False

   .. note:: This is a type-safe wrapper around the built-in callable() function.


.. py:function:: is_collection(value)

   Check if a value is a collection (list, tuple, set, dict, etc.).

   Determines whether a value is a collection type that can contain
   multiple elements, excluding strings and bytes which are sequence
   types but not typically treated as collections.

   :param value: The value to check

   :returns: True if the value is a collection, False otherwise
   :rtype: bool

   .. rubric:: Examples

   >>> is_collection([1, 2, 3])
   True
   >>> is_collection((1, 2, 3))
   True
   >>> is_collection({"a": 1})
   True
   >>> is_collection("string")  # Strings are not considered collections
   False
   >>> is_collection(42)
   False

   .. note:: Strings and bytes are not considered collections despite being sequences.


.. py:function:: is_compatible_with_type(value, target_type)

   Check if a value can be converted to a target type without errors.

   Determines whether a value can be safely converted to the specified type
   without raising exceptions, allowing for type conversion safety checks.

   :param value: The value to check
   :param target_type: The target type to check compatibility with

   :returns: True if the value can be safely converted, False otherwise
   :rtype: bool

   .. rubric:: Examples

   >>> is_compatible_with_type("123", int)
   True
   >>> is_compatible_with_type("hello", int)
   False
   >>> is_compatible_with_type(42, str)
   True
   >>> is_compatible_with_type([1, 2, 3], tuple)
   True

   .. note::

      This performs actual conversion attempts and catches exceptions,
      making it suitable for runtime type compatibility checking.


.. py:function:: is_function(obj)

   Check if an object is a function.

   Determines whether an object is a function (not a method or builtin).

   :param obj: The object to check

   :returns: True if the object is a function, False otherwise
   :rtype: bool

   .. rubric:: Examples

   >>> def example_function(): pass
   >>> is_function(example_function)
   True
   >>> is_function(len)
   False
   >>> class Example:
   ...     def method(self): pass
   >>> obj = Example()
   >>> is_function(obj.method)  # doctest: +SKIP
   False
   >>> is_function(lambda x: x)
   True

   .. note:: This identifies pure functions, not methods or built-in functions.


.. py:function:: is_in_range(value, min_value, max_value)

   Check if an integer is within a specified range.


.. py:function:: is_instance_of_any(value, types)

   Check if a value is an instance of any of the specified types.

   Determines whether the value is an instance of at least one
   of the types in the provided tuple.

   :param value: The value to check
   :param types: Tuple of types to check against

   :returns: True if value is an instance of any type in types, False otherwise
   :rtype: bool

   .. rubric:: Examples

   >>> is_instance_of_any(42, (str, int, float))
   True
   >>> is_instance_of_any("hello", (list, tuple, dict))
   False
   >>> is_instance_of_any(None, (str, int, type(None)))
   True
   >>> is_instance_of_any([], (list, tuple))
   True

   .. note::

      More efficient than multiple isinstance() calls when checking
      against many types.


.. py:function:: is_method(obj)

   Check if an object is a method.

   Determines whether an object is a method bound to a class instance.

   :param obj: The object to check

   :returns: True if the object is a method, False otherwise
   :rtype: bool

   .. rubric:: Examples

   >>> class Example:
   ...     def method(self): pass
   ...     @classmethod
   ...     def class_method(cls): pass
   ...     @staticmethod
   ...     def static_method(): pass
   >>> obj = Example()
   >>> is_method(obj.method)  # doctest: +SKIP
   True
   >>> is_method(Example.method)  # doctest: +SKIP
   False
   >>> is_method(obj.class_method)  # doctest: +SKIP
   True
   >>> is_method(obj.static_method)  # doctest: +SKIP
   False

   .. note:: This distinguishes between bound methods and regular functions.


.. py:function:: is_non_empty_string(value)

   Verify if a value is a non-empty string.

   Performs type checking and emptiness validation in a single operation
   with maximum efficiency.

   :param value: The value to validate. Can be any Python object.

   :returns: True if the value is a non-empty string, False otherwise.
   :rtype: bool

   .. rubric:: Examples

   >>> is_non_empty_string("hello")
   True
   >>> is_non_empty_string("")
   False
   >>> is_non_empty_string(123)
   False
   >>> is_non_empty_string(None)
   False

   .. note::

      This function uses isinstance for type checking rather than type()
      to properly handle inheritance relationships.


.. py:function:: is_not_empty(value)

   Check if a string is not empty.


.. py:function:: is_numeric(value)

   Check if a value is numeric (int, float, complex, or numeric subclass).

   Determines whether a value is of a numeric type, handling both
   built-in numeric types and numbers.Number subclasses.

   :param value: The value to check

   :returns: True if the value is numeric, False otherwise
   :rtype: bool

   .. rubric:: Examples

   >>> is_numeric(42)
   True
   >>> is_numeric(3.14)
   True
   >>> is_numeric(1+2j)
   True
   >>> is_numeric("42")
   False
   >>> is_numeric(None)
   False

   .. note:: This function considers all subclasses of numbers.Number as numeric.


.. py:function:: is_positive(value)

   Check if an integer is positive.


.. py:function:: is_protocol_instance(obj, protocol)

   Check if an object satisfies a Protocol interface.

   Safely determines if an object implements all the methods and attributes
   required by a Protocol, with proper handling of runtime Protocol checking.

   :param obj: Object to check
   :param protocol: Protocol to check against

   :returns: True if the object satisfies the protocol, False otherwise
   :rtype: bool

   .. rubric:: Examples

   >>> from typing import Protocol
   >>> class SupportsLen(Protocol):
   ...     def __len__(self) -> int: ...
   >>> is_protocol_instance([1, 2, 3], SupportsLen)  # doctest: +SKIP
   True
   >>> is_protocol_instance(42, SupportsLen)  # doctest: +SKIP
   False

   .. note::

      Works with both @runtime_checkable Protocols and regular Protocols.
      For non-runtime-checkable protocols, uses attribute inspection.


.. py:function:: is_subclass_safe(cls, parent)

   Safely check if a class is a subclass of another class.

   Performs an issubclass check that won't raise TypeError if the first
   argument is not a class, unlike the built-in issubclass function.

   :param cls: The potential subclass to check
   :param parent: The parent class(es) to check against

   :returns: True if cls is a subclass of parent, False otherwise
   :rtype: bool

   .. rubric:: Examples

   >>> is_subclass_safe(str, object)
   True
   >>> is_subclass_safe("not_a_class", object)
   False
   >>> is_subclass_safe(dict, (list, tuple))
   False
   >>> is_subclass_safe(list, (list, tuple))
   True
   >>> is_subclass_safe(None, object)
   False

   .. note::

      This is a safer version of the built-in issubclass() function that
      won't raise TypeError for non-class objects.


.. py:function:: is_valid_identifier(name)

   Check if a string is a valid Python identifier.

   Validates that a string can be used as a Python variable,
   function, or class name according to Python syntax rules.

   :param name: The string to check

   :returns: True if the string is a valid Python identifier, False otherwise
   :rtype: bool

   .. rubric:: Examples

   >>> is_valid_identifier("valid_name")
   True
   >>> is_valid_identifier("123invalid")
   False
   >>> is_valid_identifier("also-invalid")
   False
   >>> is_valid_identifier("")
   False
   >>> is_valid_identifier("_private")
   True

   .. note::

      A valid identifier starts with a letter or underscore and contains
      only letters, numbers, and underscores.


.. py:function:: is_valid_length(value, min_length = None, max_length = None)

   Check if a collection has a valid length.

   :param value: The collection to check
   :param min_length: Minimum allowed length (inclusive), or None for no minimum
   :param max_length: Maximum allowed length (inclusive), or None for no maximum

   :returns: True if the length is valid, False otherwise


.. py:data:: DictSchemaT

   Dictionary schema mapping string keys to schema types.

   This represents object structures with string keys mapping to schema-defined values,
   enabling the definition of complex nested objects.

   .. rubric:: Examples

   >>> person_schema: DictSchemaT = {"name": str, "age": int}
   >>> nested_schema: DictSchemaT = {"user": {"id": int, "name": str}}

.. py:data:: ParentSpecType

   Parent class specification supporting single class or tuple of classes.

   Used for inheritance definitions and interface specifications.

.. py:data:: SchemaTypeT

   A schema type definition that can recursively represent any data structure.

   This type allows the definition of complex nested structures with full type safety,
   supporting simple types, unions of types, dictionary schemas, and list schemas.

   .. rubric:: Examples

   >>> # Simple type schema
   >>> int_schema: SchemaTypeT = int
   >>>
   >>> # Union type schema (alternative types)
   >>> union_schema: SchemaTypeT = (int, str)
   >>>
   >>> # Dictionary schema (nested object)
   >>> dict_schema: SchemaTypeT = {"name": str, "age": int}
   >>>
   >>> # List schema (array of integers)
   >>> list_schema: SchemaTypeT = [int]

.. py:data:: T

.. py:data:: T

.. py:data:: T

.. py:data:: T

.. py:data:: V

.. py:data:: version
   :value: '0.1.0'



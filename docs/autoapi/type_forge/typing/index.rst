type_forge.typing
=================

.. py:module:: type_forge.typing

.. autoapi-nested-parse::

   Type Forge Typing System
   ==========================

   This module provides a comprehensive set of typing utilities for precise type manipulation,
   validation, conversion, and analysis within the Type Forge ecosystem.

   Core Components
   --------------

   The typing system is organized into several interconnected modules that form a complete
   type management ecosystem:

   - `aliases`: Type aliases with semantic meaning for enhanced code readability
   - `analysis`: Type relationship analysis and compatibility determination
   - `conversion`: Type transformation and coercion functions with elegant error handling
   - `definitions`: Core type structures, enumerations, and semantic categories
   - `hints`: Advanced type hints for complex nested structures and schema validation
   - `mapping`: Type relationship analysis, classification, and taxonomy functions
   - `naming`: Standardized type name generation and representation utilities
   - `protocols`: Protocol interfaces defining type behaviors and operational contracts
   - `standardization`: Type normalization, deduplication, and standardization
   - `validation`: Type validation and verification utilities with static guarantees
   - `variables`: Generic type variables with precise variance annotations

   Features
   --------

   - **Type Safety**: Complete static typing with no `Any` types
   - **Elegant Error Handling**: Monadic-style error handling for conversions
   - **Precise Relationship Mapping**: Comprehensive type relationship analysis
   - **Robust Validation**: Multiple validation strategies with configurable severity
   - **Protocol-Based Behavior**: Interface definitions for type-driven operations
   - **Self-Documented Structure**: Clear categorical organization with recursive precision

   Together, these components enable recursively self-improving type operations that maintain
   integrity across all abstraction layers.

   .. rubric:: Examples

   >>> from type_forge.typing import try_convert, describe_type
   >>> result = try_convert("42", int)
   >>> assert result.success and result.value == 42
   >>> type_info = describe_type(list[str])
   >>> assert type_info.category == TypeCategory.COLLECTION

   .. admonition:: Notes

      All functions in this module are designed with strict typing and comprehensive
      error handling to ensure maximum reliability in type-sensitive operations.



Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/type_forge/typing/aliases/index
   /autoapi/type_forge/typing/analysis/index
   /autoapi/type_forge/typing/conversion/index
   /autoapi/type_forge/typing/definitions/index
   /autoapi/type_forge/typing/hints/index
   /autoapi/type_forge/typing/mapping/index
   /autoapi/type_forge/typing/naming/index
   /autoapi/type_forge/typing/protocols/index
   /autoapi/type_forge/typing/standardization/index
   /autoapi/type_forge/typing/validation/index
   /autoapi/type_forge/typing/variables/index


Attributes
----------

.. autoapisummary::

   type_forge.typing.CollectionT
   type_forge.typing.CollectionTypes
   type_forge.typing.ComparableT
   type_forge.typing.ComparableT_co
   type_forge.typing.ComparableT_contra
   type_forge.typing.ConverterMap
   type_forge.typing.ConverterMapGeneric
   type_forge.typing.ConverterMapSR
   type_forge.typing.ConverterPriority
   type_forge.typing.DictKV
   type_forge.typing.DictKV_co
   type_forge.typing.DictSchemaT
   type_forge.typing.DictSchemaT_co
   type_forge.typing.DictSchemaT_contra
   type_forge.typing.ErrorHandler
   type_forge.typing.ErrorMessage
   type_forge.typing.FallbackProvider
   type_forge.typing.FieldDefinitions
   type_forge.typing.FieldDefinitionsT
   type_forge.typing.FieldDefinitionsT_co
   type_forge.typing.FieldDefinitionsT_contra
   type_forge.typing.FieldsWithDefaults
   type_forge.typing.FieldsWithDefaultsT
   type_forge.typing.FrozenSetT
   type_forge.typing.FrozenSetT_co
   type_forge.typing.HashableT
   type_forge.typing.HashableT_co
   type_forge.typing.HashableT_contra
   type_forge.typing.IterableT
   type_forge.typing.IterableT_co
   type_forge.typing.IteratorT
   type_forge.typing.IteratorT_co
   type_forge.typing.K
   type_forge.typing.K_co
   type_forge.typing.K_contra
   type_forge.typing.ListSchemaT
   type_forge.typing.ListT
   type_forge.typing.ListT_co
   type_forge.typing.MappingTypes
   type_forge.typing.NumericTypes
   type_forge.typing.OptionalConverter
   type_forge.typing.ParentSpecType
   type_forge.typing.ParentSpecType_co
   type_forge.typing.ParentSpecType_contra
   type_forge.typing.PathSegmentT
   type_forge.typing.PathT
   type_forge.typing.PredicateFunc
   type_forge.typing.PredicateFunc_contra
   type_forge.typing.PrimitiveTypes
   type_forge.typing.R
   type_forge.typing.R_co
   type_forge.typing.R_contra
   type_forge.typing.S
   type_forge.typing.S_co
   type_forge.typing.S_contra
   type_forge.typing.SchemaNodeT
   type_forge.typing.SchemaSequenceT
   type_forge.typing.SchemaTypeMappingT
   type_forge.typing.SchemaTypeT
   type_forge.typing.SchemaTypeT_co
   type_forge.typing.SchemaTypeT_contra
   type_forge.typing.SchemaValueNodeT
   type_forge.typing.SchemaValueT
   type_forge.typing.SchemaValueT_co
   type_forge.typing.SchemaValueT_contra
   type_forge.typing.SequenceT
   type_forge.typing.SequenceT_co
   type_forge.typing.SequenceTypes
   type_forge.typing.SetT
   type_forge.typing.SetT_co
   type_forge.typing.SetTypes
   type_forge.typing.SingleTypeT
   type_forge.typing.T
   type_forge.typing.TCallable
   type_forge.typing.TCallable_co
   type_forge.typing.TCallable_contra
   type_forge.typing.TCollection
   type_forge.typing.TCollection_co
   type_forge.typing.TCollection_contra
   type_forge.typing.TError
   type_forge.typing.TError_co
   type_forge.typing.TError_contra
   type_forge.typing.TInstance
   type_forge.typing.TInstance_co
   type_forge.typing.TInstance_contra
   type_forge.typing.TValue
   type_forge.typing.TValue_co
   type_forge.typing.TValue_contra
   type_forge.typing.T_co
   type_forge.typing.T_contra
   type_forge.typing.TransformFunc
   type_forge.typing.TransformFunc_co_contra
   type_forge.typing.TryResult
   type_forge.typing.TupleT
   type_forge.typing.TupleT_co
   type_forge.typing.TypeConverter
   type_forge.typing.TypeConverterSafe
   type_forge.typing.TypeDistance
   type_forge.typing.TypeGuardFunc
   type_forge.typing.TypeGuardFuncT
   type_forge.typing.TypeHierarchy
   type_forge.typing.TypeIdentifier
   type_forge.typing.TypeMap
   type_forge.typing.TypeMapFrom
   type_forge.typing.TypeMapSR
   type_forge.typing.TypeMapTo
   type_forge.typing.TypeMatch
   type_forge.typing.TypeName
   type_forge.typing.TypePath
   type_forge.typing.TypePrecedence
   type_forge.typing.TypeRegistry
   type_forge.typing.TypeRegistryT
   type_forge.typing.TypeRegistryT_co
   type_forge.typing.TypeRegistryT_contra
   type_forge.typing.TypeRelationship
   type_forge.typing.U
   type_forge.typing.U_co
   type_forge.typing.U_contra
   type_forge.typing.UnionTypeT
   type_forge.typing.V
   type_forge.typing.V_co
   type_forge.typing.V_contra
   type_forge.typing.ValidationContext
   type_forge.typing.ValidationFunc
   type_forge.typing.ValidationFuncT
   type_forge.typing.ValidationFuncT_contra
   type_forge.typing.ValidationOptions
   type_forge.typing.ValidationPath
   type_forge.typing.ValidationResult
   type_forge.typing.ValidationResultT
   type_forge.typing.ValidationStrategy
   type_forge.typing.ValidationWithPath


Classes
-------

.. autoapisummary::

   type_forge.typing.CompositeValidator
   type_forge.typing.ConversionResult
   type_forge.typing.SupportsBoolConversion
   type_forge.typing.SupportsComparison
   type_forge.typing.SupportsEquality
   type_forge.typing.SupportsFloat
   type_forge.typing.SupportsFloatConversion
   type_forge.typing.SupportsGetAttr
   type_forge.typing.SupportsGetItem
   type_forge.typing.SupportsInt
   type_forge.typing.SupportsIntConversion
   type_forge.typing.SupportsIteration
   type_forge.typing.SupportsLen
   type_forge.typing.SupportsLength
   type_forge.typing.SupportsMapping
   type_forge.typing.SupportsStrConversion
   type_forge.typing.SupportsTypeCheck
   type_forge.typing.TypeConverterProtocol
   type_forge.typing.TypeDeduplicator
   type_forge.typing.TypeFactory
   type_forge.typing.TypeForge
   type_forge.typing.TypeInfo
   type_forge.typing.TypeNormalizer
   type_forge.typing.TypeRegistryProtocol
   type_forge.typing.TypeRelationshipAnalyzer
   type_forge.typing.TypeStandardizer
   type_forge.typing.TypedConverter
   type_forge.typing.ValidationIssue
   type_forge.typing.ValidationReport
   type_forge.typing.Validator


Functions
---------

.. autoapisummary::

   type_forge.typing.coerce_to_type
   type_forge.typing.convert_with_fallback
   type_forge.typing.deduplicate_types
   type_forge.typing.describe_type
   type_forge.typing.get_common_supertype
   type_forge.typing.get_python_type_for_name
   type_forge.typing.get_standardized_type_name
   type_forge.typing.get_type_category
   type_forge.typing.get_type_hierarchy
   type_forge.typing.get_type_name
   type_forge.typing.has_attributes
   type_forge.typing.is_abstract_type
   type_forge.typing.is_callable
   type_forge.typing.is_collection
   type_forge.typing.is_compatible_with_type
   type_forge.typing.is_function
   type_forge.typing.is_generic_type
   type_forge.typing.is_instance_of_any
   type_forge.typing.is_method
   type_forge.typing.is_non_empty_string
   type_forge.typing.is_numeric
   type_forge.typing.is_primitive_type
   type_forge.typing.is_protocol_instance
   type_forge.typing.is_subclass_safe
   type_forge.typing.is_valid_identifier
   type_forge.typing.safe_bool_convert
   type_forge.typing.safe_float_convert
   type_forge.typing.safe_int_convert
   type_forge.typing.safe_str_convert
   type_forge.typing.standardize_type_name
   type_forge.typing.try_convert


Package Contents
----------------

.. py:class:: CompositeValidator

   Bases: :py:obj:`Protocol`\ [\ :py:obj:`type_forge.typing.variables.T`\ ]


   Protocol for validators that combine multiple validation rules.

   Type Args:
       T: The type of value being validated.
           For proper variance handling, use this protocol with specific types.

   .. rubric:: Examples

   >>> class AndValidator:
   ...     def __init__(self) -> None:
   ...         self.validators = []
   ...     def add_validator(self, validator):
   ...         self.validators.append(validator)
   ...     def validate(self, value):
   ...         return all(v.validate(value) for v in self.validators)


   .. py:method:: add_validator(validator)

      Adds a validator to the composite validator.

      :param validator: The validator to add.



   .. py:method:: validate(value)

      Validates the given value using all added validators.

      :param value: The value to validate.

      :returns: True if the value passes all validators, False otherwise.
      :rtype: bool



.. py:class:: ConversionResult(success, value = None, error = None)

   Bases: :py:obj:`Generic`\ [\ :py:obj:`type_forge.typing.variables.T`\ ]


   Result of a type conversion operation with success status and error tracking.

   This class encapsulates the result of a type conversion operation,
   providing both the converted value (if successful) and error information
   when conversion fails. It allows for chainable operations and error handling.

   .. rubric:: Attributes

   success (bool): Whether the conversion was successful
   value (Optional[T]): The converted value, or None if conversion failed
   error (Optional[str]): Error message if conversion failed

   .. rubric:: Examples

   >>> result = ConversionResult.create_success(42)
   >>> result.success
   True
   >>> print(result.value)
   42
   >>> result = ConversionResult[int].failure("Invalid conversion")
   >>> result.success
   False
   >>> print(result.error)
   Invalid conversion
   >>> # Chain operations
   >>> result = ConversionResult.create_success("123")
   >>> result.then(lambda s: ConversionResult.create_success(int(s))).value
   123

   Initialize a ConversionResult.

   :param success: Whether the conversion was successful
   :param value: The converted value, None if conversion failed
   :param error: Error message if conversion failed

   .. rubric:: Examples

   >>> result = ConversionResult(True, 42)
   >>> result.success
   True
   >>> result.value
   42
   >>> failed = ConversionResult(False, None, "Conversion error")
   >>> failed.error
   'Conversion error'


   .. py:method:: __bool__()

      Boolean conversion returns success status.

      :returns: True if conversion was successful, False otherwise
      :rtype: bool

      .. rubric:: Examples

      >>> bool(ConversionResult.create_success(42))
      True
      >>> bool(ConversionResult[str].failure("Error"))
      False



   .. py:method:: __repr__()

      Detailed string representation of the conversion result.

      :returns: Detailed representation including class name
      :rtype: str

      .. rubric:: Examples

      >>> repr(ConversionResult.create_success(42))
      'ConversionResult(success=True, value=42, error=None)'
      >>> repr(ConversionResult.failure("Error"))
      'ConversionResult(success=False, value=None, error="Error")'



   .. py:method:: __str__()

      String representation of the conversion result.

      :returns: Description of the conversion result
      :rtype: str

      .. rubric:: Examples

      >>> str(ConversionResult.create_success(42))
      'Successful conversion: 42'
      >>> str(ConversionResult.failure("Invalid input"))
      'Failed conversion: Invalid input'



   .. py:method:: create_success(value)
      :classmethod:


      Create a successful conversion result.

      :param value: The successfully converted value

      :returns: A successful conversion result
      :rtype: ConversionResult[T]

      .. rubric:: Examples

      >>> result = ConversionResult.create_success(42)
      >>> result.success
      True
      >>> result.value
      42



   .. py:method:: failure(error)
      :classmethod:


      Create a failed conversion result.

      :param error: Description of the error that occurred

      :returns: A failed conversion result
      :rtype: ConversionResult[T]

      .. rubric:: Examples

      >>> result = ConversionResult.failure("Invalid format")
      >>> result.success
      False
      >>> result.error
      'Invalid format'



   .. py:method:: from_try(func)
      :classmethod:


      Create a result by trying a function that may raise exceptions.

      :param func: Function to execute that may raise an exception

      :returns:

                Successful result with the function's return value,
                                   or failed result with the exception message
      :rtype: ConversionResult[T]

      .. rubric:: Examples

      >>> ConversionResult.from_try(lambda: int("42")).value
      42
      >>> result = ConversionResult.from_try(lambda: int("not_a_number"))
      >>> result.success
      False
      >>> "invalid literal" in result.error
      True



   .. py:method:: map(transform)

      Transform the value if conversion was successful.

      :param transform: Function to transform the value

      :returns: Result containing the transformed value, or the original failure
      :rtype: ConversionResult[U]

      .. rubric:: Examples

      >>> result = ConversionResult.create_success(42)
      >>> result.map(lambda x: x * 2).value
      84
      >>> failed = ConversionResult[int].failure("Error")
      >>> failed.map(lambda x: x * 2).error
      'Error'



   .. py:method:: or_else(default_value)

      Get the result value or a default if conversion failed.

      :param default_value: Value to return if conversion failed

      :returns: The conversion result value or the default
      :rtype: T

      .. rubric:: Examples

      >>> ConversionResult.create_success(42).or_else(0)
      42
      >>> ConversionResult[int].failure("Error").or_else(0)
      0



   .. py:method:: or_else_get(provider)

      Get the result value or compute a default if conversion failed.

      :param provider: Function to compute the default value

      :returns: The conversion result value or the computed default
      :rtype: T

      .. rubric:: Examples

      >>> ConversionResult.create_success(42).or_else_get(lambda: 0)
      42
      >>> ConversionResult[int].failure("Error").or_else_get(lambda: 99)
      99



   .. py:method:: or_raise(exception_factory = ValueError)

      Get the result value or raise an exception if conversion failed.

      :param exception_factory: Function to create the exception from the error message

      :returns: The conversion result value
      :rtype: T

      :raises Exception: If conversion failed, raises the exception created by exception_factory

      .. rubric:: Examples

      >>> ConversionResult.create_success(42).or_raise()
      42
      >>> try:
      ...     ConversionResult[int].failure("Bad value").or_raise()
      ... except ValueError as e:
      ...     str(e)
      'Bad value'



   .. py:method:: recover(recovery_func)

      Attempt to recover from a failed conversion.

      :param recovery_func: Function that takes the error message and returns a recovery value

      :returns: Recovered result if this was a failure, or the original result
      :rtype: ConversionResult[T]

      .. rubric:: Examples

      >>> failed = ConversionResult[int].failure("Missing value")
      >>> failed.recover(lambda _: 0).value
      0
      >>> success = ConversionResult.create_success(42)
      >>> success.recover(lambda _: 0).value  # Original value preserved
      42



   .. py:method:: then(converter)

      Chain another conversion operation if this one succeeded.

      :param converter: Function to convert the value further

      :returns: Result of the chained conversion, or the original failure
      :rtype: ConversionResult[U]

      .. rubric:: Examples

      >>> # Convert string to int then to float
      >>> result = ConversionResult.create_success("42")
      >>> to_int = lambda s: ConversionResult.create_success(int(s))
      >>> to_float = lambda i: ConversionResult.create_success(float(i))
      >>> result.then(to_int).then(to_float).value
      42.0
      >>> # Failure stops the chain
      >>> failed = ConversionResult[str].failure("Invalid input")
      >>> failed.then(to_int).then(to_float).error
      'Invalid input'



   .. py:attribute:: error
      :type:  Optional[str]
      :value: None



   .. py:attribute:: success
      :type:  bool


   .. py:attribute:: value
      :type:  Optional[type_forge.typing.variables.T]
      :value: None



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



.. py:class:: SupportsComparison

   Bases: :py:obj:`Protocol`


   Protocol for types that support comparison operations.

   This protocol defines the interface for objects that can be compared
   using standard comparison operators.

   .. rubric:: Examples

   >>> class ComparableValue:
   ...     def __init__(self, value: int) -> None:
   ...         self.value = value
   ...     def __lt__(self, other: object) -> bool:
   ...         if isinstance(other, ComparableValue):
   ...             return self.value < other.value
   ...         return NotImplemented
   >>> ComparableValue(1) < ComparableValue(2)  # True


   .. py:method:: __lt__(other)

      Compare if self is less than other.

      :param other: Object to compare against.

      :returns: True if self is less than other, False otherwise.
      :rtype: bool



.. py:class:: SupportsEquality

   Bases: :py:obj:`Protocol`


   Protocol for objects that support equality operations.


   .. py:method:: __eq__(other)


   .. py:method:: __ne__(other)


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



.. py:class:: SupportsGetAttr

   Bases: :py:obj:`Protocol`


   Protocol for types that support attribute access.

   This protocol defines the interface for objects that implement
   custom attribute access through the __getattr__ method.

   .. rubric:: Examples

   >>> class CustomObject:
   ...     def __getattr__(self, name: str) -> int:
   ...         return len(name)
   >>> obj = CustomObject()
   >>> obj.attribute  # 9


   .. py:method:: __getattr__(name)

      Get attribute by name.

      :param name: Name of the attribute to retrieve.

      :returns: The attribute value.

      :raises AttributeError: If the attribute is not found.



.. py:class:: SupportsGetItem

   Bases: :py:obj:`Protocol`\ [\ :py:obj:`type_forge.typing.variables.K_contra`\ , :py:obj:`type_forge.typing.variables.V_co`\ ]


   Protocol for types that support item access with square brackets.

   This protocol defines the interface for objects that can be accessed
   using the subscription notation (obj[key]).

   Type Args:
       K_contra: The key type (contravariant). This allows a container that
                accepts a supertype to be used where a container that accepts
                a subtype is expected.
       V_co: The value type (covariant). This allows a container that returns
             a subtype to be used where a container that returns a supertype
             is expected.

   .. rubric:: Examples

   >>> class CustomContainer:
   ...     def __init__(self, data: dict[str, int]) -> None:
   ...         self.data = data
   ...     def __getitem__(self, key: str) -> int:
   ...         return self.data[key]
   >>> container = CustomContainer({"one": 1})
   >>> container["one"]  # 1


   .. py:method:: __getitem__(key)

      Get item at the specified key.

      :param key: The key to look up.

      :returns: The value associated with the key.

      :raises KeyError: If the key is not found.



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



.. py:class:: SupportsIteration

   Bases: :py:obj:`Protocol`\ [\ :py:obj:`type_forge.typing.variables.T_co`\ ]


   Protocol for types that support iteration.

   This protocol defines the interface for objects that can be iterated over
   using a for loop or with the iter() function.

   Type Args:
       T_co: The type of items yielded by the iterator (covariant).
             This allows an iterator of a subtype to be used where an
             iterator of a supertype is expected.

   .. rubric:: Examples

   >>> class CustomIterable:
   ...     def __init__(self, values: list[int]) -> None:
   ...         self.values = values
   ...     def __iter__(self) -> Iterator[int]:
   ...         return iter(self.values)
   >>> list(CustomIterable([1, 2, 3]))  # [1, 2, 3]


   .. py:method:: __iter__()

      Return an iterator for this object.

      :returns: An iterator yielding items of type T_co.
      :rtype: Iterator[T_co]



.. py:class:: SupportsLen

   Bases: :py:obj:`Protocol`


   Protocol for objects that support length operations.


   .. py:method:: __len__()


.. py:class:: SupportsLength

   Bases: :py:obj:`Protocol`


   Protocol for types that support the len() function.

   This protocol defines the interface for objects that can report
   their length through the __len__ method.

   .. rubric:: Examples

   >>> class CustomSized:
   ...     def __init__(self, size: int) -> None:
   ...         self.size = size
   ...     def __len__(self) -> int:
   ...         return self.size
   >>> len(CustomSized(5))  # 5


   .. py:method:: __len__()

      Return the length of the object.

      :returns: The number of items in the object.
      :rtype: int



.. py:class:: SupportsMapping

   Bases: :py:obj:`Protocol`\ [\ :py:obj:`type_forge.typing.variables.K_co`\ , :py:obj:`type_forge.typing.variables.V`\ ]


   Protocol for types that support dictionary-like mapping operations.

   This protocol defines the interface for objects that implement mapping
   behavior with key-value pairs.

   Type Args:
       K: The key type.
       V: The value type.

   .. rubric:: Examples

   >>> class CustomMapping:
   ...     def __init__(self) -> None:
   ...         self._data: dict[str, int] = {}
   ...     def __getitem__(self, key: str) -> int:
   ...         return self._data[key]
   ...     def __setitem__(self, key: str, value: int) -> None:
   ...         self._data[key] = value
   ...     def __contains__(self, key: object) -> bool:
   ...         return key in self._data
   >>> mapping = CustomMapping()
   >>> mapping["key"] = 1
   >>> "key" in mapping  # True
   >>> mapping["key"]  # 1


   .. py:method:: __contains__(key)

      Check if the mapping contains the specified key.

      :param key: The key to check for.

      :returns: True if the key exists in the mapping, False otherwise.
      :rtype: bool



   .. py:method:: __getitem__(key)

      Get the value for a given key.

      :param key: The key to look up.

      :returns: The value associated with the key.

      :raises KeyError: If the key is not found.



   .. py:method:: __setitem__(key, value)

      Set the value for a given key.

      :param key: The key to set.
      :param value: The value to associate with the key.



.. py:class:: SupportsStrConversion

   Bases: :py:obj:`Protocol`


   Protocol for types that can be converted to str.

   This protocol defines the interface for objects that support
   conversion to string values through the __str__ method.

   .. rubric:: Examples

   >>> class CustomString:
   ...     def __init__(self, value: str) -> None:
   ...         self.value = value
   ...     def __str__(self) -> str:
   ...         return self.value
   >>> str(CustomString("hello"))  # 'hello'


   .. py:method:: __str__()

      Convert to string.

      :returns: String representation of the object.
      :rtype: str



.. py:class:: SupportsTypeCheck

   Bases: :py:obj:`Protocol`


   Protocol for types that can validate if a value is of a specific type.

   This protocol defines the interface for objects that can check if a
   value conforms to a particular type specification.


   .. py:method:: is_type(value, target_type)

      Check if a value matches the specified type.

      :param value: The value to check.
      :param target_type: The type to check against.

      :returns: True if the value is of the specified type, False otherwise.
      :rtype: bool



.. py:class:: TypeConverterProtocol

   Bases: :py:obj:`Protocol`


   Protocol for types that can convert between different types.

   This protocol defines the interface for objects that implement
   conversion logic between different types.

   .. rubric:: Examples

   >>> class IntToStrConverter:
   ...     def convert(self, value: int) -> str:
   ...         return str(value)
   >>> converter = IntToStrConverter()
   >>> converter.convert(42)  # "42"


   .. py:method:: convert(value)

      Convert a value from one type to another.

      :param value: The value to convert.

      :returns: The converted value.

      :raises TypeError: If the value cannot be converted.
      :raises ValueError: If the value is semantically invalid for conversion.



.. py:class:: TypeDeduplicator

   Bases: :py:obj:`Protocol`\ [\ :py:obj:`type_forge.typing.variables.T`\ ]


   Protocol for objects that can deduplicate values based on type characteristics.

   This protocol defines the interface for objects that can identify and
   remove duplicate values according to type-specific equality criteria.

   Type Args:
       T: The type of values being deduplicated.

   .. rubric:: Examples

   >>> class IntDeduplicator:
   ...     def deduplicate(self, values: list[int]) -> list[int]:
   ...         return list(set(values))
   >>> deduplicator = IntDeduplicator()
   >>> deduplicator.deduplicate([1, 2, 2, 3])  # [1, 2, 3]


   .. py:method:: deduplicate(values)

      Remove duplicate values from a list.

      :param values: The list of values to deduplicate.

      :returns: A new list with duplicates removed.
      :rtype: list[T]



.. py:class:: TypeFactory

   Bases: :py:obj:`Protocol`\ [\ :py:obj:`type_forge.typing.variables.T_co`\ ]


   Protocol for factory objects that create instances of a specific type.

   This protocol defines the interface for objects that can create
   instances of type T_co from various inputs.

   Type Args:
       T_co: The type of object created by the factory (covariant).
             This allows a factory that creates subtypes to be used
             where a factory that creates supertypes is expected.

   .. rubric:: Examples

   >>> class PersonFactory:
   ...     def create(self, name: str, age: int) -> 'Person':
   ...         return Person(name, age)
   >>> factory = PersonFactory()
   >>> person = factory.create("Alice", 30)


   .. py:method:: create(*args, **kwargs)

      Create an instance of type T_co.

      :param \*args: Positional arguments for object construction.
      :param \*\*kwargs: Keyword arguments for object construction.

      :returns: A new instance of type T_co.

      :raises TypeError: If the arguments are incompatible with the type.
      :raises ValueError: If the arguments are semantically invalid.



.. py:class:: TypeForge

   Bases: :py:obj:`Protocol`\ [\ :py:obj:`type_forge.typing.variables.T_co`\ ]


   Protocol for type converters that transform values to specific types.

   Type Args:
       T_co: The target type that values will be converted to (covariant).
             This allows a forge that produces a subtype to be used where
             a forge that produces a supertype is expected.

   .. rubric:: Examples

   >>> class StringForge:
   ...     def forge(self, value: object) -> str:
   ...         return str(value)
   >>> forge = StringForge()
   >>> forge.forge(42)  # "42"


   .. py:method:: forge(value)

      Transforms the given value into the desired type.

      :param value: The value to transform.

      :returns: A value of type T_co.

      :raises TypeError: If the value cannot be converted to type T_co.
      :raises ValueError: If the value is semantically invalid for type T_co.



.. py:class:: TypeInfo

   Bases: :py:obj:`Protocol`


   Protocol for objects that provide type metadata and reflection capabilities.

   This protocol defines the interface for objects that can inspect and
   provide information about types.


   .. py:method:: get_attributes()

      Get the attributes defined by this type.

      :returns: Mapping of attribute names to their types.
      :rtype: dict[str, type]



   .. py:method:: get_name()

      Get the name of the type.

      :returns: The type name.
      :rtype: str



   .. py:method:: is_subtype_of(other)

      Check if this type is a subtype of another type.

      :param other: The potential supertype.

      :returns: True if this type is a subtype of other, False otherwise.
      :rtype: bool



.. py:class:: TypeNormalizer

   Bases: :py:obj:`Protocol`\ [\ :py:obj:`type_forge.typing.variables.T`\ ]


   Protocol for objects that normalize values within a type.

   This protocol defines the interface for objects that transform
   values to a normal form while preserving type.

   Type Args:
       T: The type being normalized.

   .. rubric:: Examples

   >>> class PathNormalizer:
   ...     def normalize(self, value: str) -> str:
   ...         return value.replace('\', '/')
   >>> normalizer = PathNormalizer()
   >>> normalizer.normalize("C:\Windows\System32")  # "C:/Windows/System32"


   .. py:method:: normalize(value)

      Transform a value to its normal form.

      :param value: The value to normalize.

      :returns: The normalized value of the same type.
      :rtype: T

      :raises ValueError: If the value cannot be normalized.



.. py:class:: TypeRegistryProtocol

   Bases: :py:obj:`Protocol`\ [\ :py:obj:`type_forge.typing.variables.T`\ ]


   Protocol for type registration and lookup systems.

   This protocol defines the interface for objects that maintain
   a registry of types and associated metadata or factories.

   Type Args:
       T: The type of value associated with each registered type.

   .. rubric:: Examples

   >>> class SimpleTypeRegistry:
   ...     def __init__(self) -> None:
   ...         self._registry: dict[type, str] = {}
   ...     def register(self, cls: type, description: str) -> None:
   ...         self._registry[cls] = description
   ...     def lookup(self, cls: type) -> str:
   ...         return self._registry[cls]
   >>> registry = SimpleTypeRegistry()
   >>> registry.register(int, "Integer type")
   >>> registry.lookup(int)  # "Integer type"


   .. py:method:: lookup(cls)

      Look up the value associated with a type.

      :param cls: The type to look up.

      :returns: The value associated with the type.

      :raises KeyError: If the type is not registered.



   .. py:method:: register(cls, value)

      Register a type with an associated value.

      :param cls: The type to register.
      :param value: The value to associate with the type.



.. py:class:: TypeRelationshipAnalyzer

   Analyzes and determines the relationship between types for conversion and validation.

   This utility class provides methods to analyze type relationships, determine
   compatibility, and calculate conversion distances between types. It implements
   a hierarchical type analysis system that can determine:

   1. Direct type relationships (identical, subtype, supertype)
   2. Conversion possibilities and their relative complexity
   3. Structural compatibility between collection types
   4. Common supertypes across multiple types

   .. rubric:: Examples

   >>> analyzer = TypeRelationshipAnalyzer()
   >>> analyzer.get_relationship(bool, int)
   <TypeCompatibility.SUBTYPE: 'subtype'>
   >>> analyzer.get_relationship(int, bool)
   <TypeCompatibility.SUPERTYPE: 'supertype'>
   >>> analyzer.get_relationship(int, str)
   <TypeCompatibility.CONVERTIBLE: 'convertible'>
   >>> analyzer.get_relationship(int, int)
   <TypeCompatibility.IDENTICAL: 'identical'>
   >>> analyzer.is_convertible(int, float)
   True
   >>> analyzer.is_convertible(complex, bool)
   False


   .. py:method:: find_common_supertype(*types)

      Find the most specific common supertype of all given types.

      This method analyzes the Method Resolution Order (MRO) of each type to
      identify the most specific type that all given types inherit from. It's
      useful for determining a common interface or base class.

      :param \*types: Variable number of types to analyze

      :returns:

                The most specific common supertype, or None
                                       if only object is common (effectively no meaningful
                                       common interface exists)
      :rtype: Optional[Type[object]]

      .. rubric:: Examples

      >>> analyzer = TypeRelationshipAnalyzer()
      >>> analyzer.find_common_supertype(int, float) == numbers.Number
      True
      >>> analyzer.find_common_supertype(list, tuple) == collections.abc.Sequence
      True
      >>> analyzer.find_common_supertype(str, dict) is None  # Only 'object' in common
      True



   .. py:method:: get_conversion_distance(source_type, target_type)

      Calculate the conversion distance between types (lower is easier).

      This method quantifies the complexity of converting between types using
      a numeric distance metric. The distance represents the relative difficulty
      of conversion, with smaller values indicating easier conversions.

      :param source_type: The source type to convert from
      :param target_type: The target type to convert to

      :returns:

                Distance metric with precise meaning:
                    - 0: Identical types (no conversion needed)
                    - 1: Subtype relationship (safe upcast)
                    - 2: Supertype relationship (potential downcast)
                    - 3: Implicit convertible types (automatic conversion)
                    - 5: Explicitly convertible types (requires explicit conversion)
                    - 7: Container compatible types (similar collections)
                    - 10: Structurally compatible types (similar structures)
                    - 15: Protocol compatible types (interface compatibility)
                    - float('inf'): Incompatible types (conversion impossible)
      :rtype: TypeDistance

      .. rubric:: Examples

      >>> analyzer = TypeRelationshipAnalyzer()
      >>> analyzer.get_conversion_distance(int, int)
      0
      >>> analyzer.get_conversion_distance(bool, int)
      1
      >>> analyzer.get_conversion_distance(str, int) > analyzer.get_conversion_distance(float, int)
      True
      >>> analyzer.get_conversion_distance(list, dict) == float('inf')
      True



   .. py:method:: get_relationship(source_type, target_type)

      Determine the relationship between source and target types.

      This method establishes the fundamental relationship between two types,
      forming the basis for type conversion, validation, and compatibility checks.
      It analyzes inheritance relationships, conversion possibilities, and
      structural compatibilities.

      :param source_type: The source type to analyze
      :param target_type: The target type to analyze

      :returns:

                The precise relationship between the types, with values:
                    - IDENTICAL: Types are exactly the same
                    - SUBTYPE: Source is a subtype of target
                    - SUPERTYPE: Target is a subtype of source
                    - IMPLICIT_CONVERTIBLE: Types can be converted implicitly
                    - CONVERTIBLE: Types can be converted explicitly
                    - CONTAINER_COMPATIBLE: Container types with compatible elements
                    - STRUCTURALLY_COMPATIBLE: Types share compatible structures
                    - PROTOCOL_COMPATIBLE: Source satisfies target's protocol
                    - INCOMPATIBLE: Types cannot be converted
      :rtype: TypeCompatibility

      .. rubric:: Examples

      >>> analyzer = TypeRelationshipAnalyzer()
      >>> analyzer.get_relationship(int, int)
      <TypeCompatibility.IDENTICAL: 'identical'>
      >>> analyzer.get_relationship(bool, int)
      <TypeCompatibility.SUBTYPE: 'subtype'>
      >>> analyzer.get_relationship(list, tuple)
      <TypeCompatibility.CONVERTIBLE: 'convertible'>



   .. py:method:: is_convertible(source_type, target_type)

      Determine if source type can be converted to target type.

      A convenience method that leverages the type relationship analysis to
      provide a boolean verdict on conversion possibility.

      :param source_type: The source type to convert from
      :param target_type: The target type to convert to

      :returns: True if conversion is possible through any means, False otherwise
      :rtype: bool

      .. rubric:: Examples

      >>> analyzer = TypeRelationshipAnalyzer()
      >>> analyzer.is_convertible(int, float)
      True
      >>> analyzer.is_convertible(str, bytes)
      True
      >>> analyzer.is_convertible(dict, list)
      False



.. py:class:: TypeStandardizer

   Bases: :py:obj:`Protocol`\ [\ :py:obj:`type_forge.typing.variables.S_contra`\ , :py:obj:`type_forge.typing.variables.T_co`\ ]


   Protocol for objects that standardize values to a canonical form.

   This protocol defines the interface for objects that convert values
   from various forms into a standardized representation.

   Type Args:
       S_contra: The source type (contravariant). This allows a standardizer
                that accepts a supertype to be used where a standardizer that
                accepts a subtype is expected.
       T: The standardized type.

   .. rubric:: Examples

   >>> class CaseStandardizer:
   ...     def standardize(self, value: str) -> str:
   ...         return value.lower()
   >>> standardizer = CaseStandardizer()
   >>> standardizer.standardize("Hello")  # "hello"


   .. py:method:: standardize(value)

      Convert a value to its standardized form.

      :param value: The value to standardize.

      :returns: The standardized value.

      :raises TypeError: If the value cannot be standardized.
      :raises ValueError: If the value is semantically invalid.



.. py:class:: TypedConverter

   Bases: :py:obj:`Protocol`\ [\ :py:obj:`type_forge.typing.variables.S_contra`\ , :py:obj:`type_forge.typing.variables.T_co`\ ]


   Protocol for types that can convert from a specific type to another specific type.

   This protocol defines the interface for objects that implement
   conversion logic between specific types with strong typing.

   Type Args:
       S_contra: The source type (contravariant). This allows a converter that
                accepts a supertype to be used where a converter that accepts
                a subtype is expected.
       T: The target type.

   .. rubric:: Examples

   >>> class IntToStrConverter:
   ...     def convert(self, value: int) -> str:
   ...         return str(value)
   >>> converter = IntToStrConverter()
   >>> converter.convert(42)  # "42"


   .. py:method:: convert(value)

      Convert a value from type S_contra to type T.

      :param value: The value to convert.

      :returns: The converted value of type T.

      :raises TypeError: If the value cannot be converted.
      :raises ValueError: If the value is semantically invalid for conversion.



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



.. py:class:: Validator

   Bases: :py:obj:`Protocol`\ [\ :py:obj:`type_forge.typing.variables.T_contra`\ ]


   Protocol for validators that check if values meet certain criteria.

   Validator protocols define the interface for objects that verify
   whether values conform to specific requirements or constraints.

   Type Args:
       T_contra: The type of value being validated (contravariant).
                This allows a validator that can validate a supertype
                to be used where a validator for a subtype is expected.

   .. rubric:: Examples

   >>> class IntValidator:
   ...     def validate(self, value: int) -> bool:
   ...         return value > 0
   >>> validator = IntValidator()
   >>> validator.validate(42)  # True


   .. py:method:: validate(value)

      Validates the given value.

      :param value: The value to validate.

      :returns: True if the value is valid, False otherwise.
      :rtype: bool



.. py:function:: coerce_to_type(value, target_type)

   Coerce a value to a target type, raising TypeError if conversion fails.

   Unlike try_convert, this function raises an exception if the value cannot
   be converted, making it suitable for validation scenarios where conversion
   failure should stop execution.

   :param value: The value to convert
   :param target_type: The type to convert to

   :returns: The value converted to the target type
   :rtype: T

   :raises TypeError: If the value cannot be converted to the target type

   .. rubric:: Examples

   >>> coerce_to_type("42", int)
   42
   >>> coerce_to_type(42, str)
   '42'
   >>> coerce_to_type(True, int)
   1
   >>> try:
   ...     coerce_to_type("not_a_number", int)
   ... except TypeError:
   ...     print("Conversion failed")
   Conversion failed

   .. note::

      This function is more strict than convert_with_fallback, raising an exception
      rather than returning the original value on failure.


.. py:function:: convert_with_fallback(value, primary_type, fallback_type)

   Try to convert a value to a primary type, with fallback to a secondary type.

   Attempts to convert the value to the primary type first, and if that fails,
   tries converting to the fallback type. If both fail, returns the original value.

   :param value: The value to convert
   :param primary_type: The preferred target type
   :param fallback_type: The fallback target type

   :returns: Converted value (T or R) or original value (S) if conversion fails
   :rtype: Union[T, R, S]

   .. rubric:: Examples

   >>> convert_with_fallback("123", int, float)
   123
   >>> convert_with_fallback("3.14", int, float)
   3.14
   >>> convert_with_fallback("hello", int, float)
   'hello'
   >>> convert_with_fallback(None, int, str)
   ''

   .. note::

      This function silently handles conversion errors and returns the original
      value if both conversions fail.


.. py:function:: deduplicate_types(types)

   Remove redundant types from a sequence of types.

   Removes types that are subtypes of other types in the sequence,
   keeping only the most specific types necessary.

   :param types: A sequence of types to deduplicate

   :returns: A deduplicated list of types
   :rtype: List[Type[object]]

   .. rubric:: Examples

   >>> deduplicate_types([int, object, float, numbers.Number])  # doctest: +SKIP
   [<class 'int'>, <class 'float'>]
   >>> deduplicate_types([list, Collection, Sequence])  # doctest: +SKIP
   [<class 'list'>]

   .. note:: Useful for simplifying Union types and type annotations.


.. py:function:: describe_type(value)

   Generate a detailed description of a value's type.

   Creates a human-readable description of an object's type,
   including additional information for collections.

   :param value: The value to describe

   :returns: A detailed description of the value's type
   :rtype: str

   .. rubric:: Examples

   >>> describe_type(42)
   'int'
   >>> describe_type([1, 2, 3])
   'list[int] (length: 3)'
   >>> describe_type({'a': 1, 'b': 'text'})
   'dict[str, mixed] (size: 2)'
   >>> describe_type(None)
   'None'

   .. note:: For collections, includes element types and collection size.


.. py:function:: get_common_supertype(types)

   Find the most specific common supertype of multiple types.

   Identifies the closest common ancestor type that all the given
   types inherit from, providing the tightest type bound.

   :param types: List of types to find a common supertype for

   :returns: The common supertype, or None if only object is common
   :rtype: Optional[Type[object]]

   .. rubric:: Examples

   >>> get_common_supertype([int, float])  # doctest: +SKIP
   <class 'numbers.Number'>
   >>> get_common_supertype([list, tuple])  # doctest: +SKIP
   <class 'collections.abc.Sequence'>
   >>> get_common_supertype([str, int]) is object
   True
   >>> get_common_supertype([]) is None
   True

   .. note::

      Returns object if no more specific common supertype exists.
      Returns None for an empty list of types.


.. py:function:: get_python_type_for_name(type_name)

   Get the Python type object corresponding to a type name.

   Maps common type names to their corresponding Python type objects,
   handling both builtin types and common collection types.

   :param type_name: Name of the type as a string

   :returns: The corresponding Python type, or None if not found
   :rtype: Optional[Type[object]]

   .. rubric:: Examples

   >>> get_python_type_for_name("int")
   <class 'int'>
   >>> get_python_type_for_name("str")
   <class 'str'>
   >>> get_python_type_for_name("list")
   <class 'list'>
   >>> get_python_type_for_name("unknown") is None
   True
   >>> get_python_type_for_name("STRING")  # Case insensitive
   <class 'str'>

   .. note::

      Currently handles only common builtin types. For more complex types,
      consider eval() with appropriate safety measures.


.. py:function:: get_standardized_type_name(typ)

   Get the name of a type.

   For simple types, returns the type name.
   For generic types, includes the parameter types.

   :param typ: The type to get the name for

   :returns: The name of the type
   :rtype: str

   .. rubric:: Examples

   >>> get_type_name(int)
   'int'
   >>> from typing import List
   >>> get_type_name(List[int])
   'List[int]'


.. py:function:: get_type_category(typ)

   Determine the semantic category of a type.

   Categorizes types into meaningful groups based on their structure
   and behavior rather than just their inheritance relationships.

   :param typ: The type to categorize

   :returns: The semantic category of the type
   :rtype: TypeCategory

   .. rubric:: Examples

   >>> get_type_category(int)
   <TypeCategory.ATOMIC: 'atomic'>
   >>> get_type_category(list)
   <TypeCategory.CONTAINER: 'container'>
   >>> get_type_category(dict)
   <TypeCategory.CONTAINER: 'container'>
   >>> get_type_category(Protocol)  # doctest: +SKIP
   <TypeCategory.PROTOCOL: 'protocol'>

   .. note::

      This function uses both inheritance and structural properties
      to determine the category.


.. py:function:: get_type_hierarchy(typ)

   Get the complete inheritance hierarchy of a type.

   Returns the Method Resolution Order (MRO) of a type, which
   represents its inheritance hierarchy.

   :param typ: The type to get the hierarchy for

   :returns:

             The inheritance hierarchy of the type, from
                                most specific to most general
   :rtype: List[Type[object]]

   .. rubric:: Examples

   >>> bool_hierarchy = get_type_hierarchy(bool)
   >>> bool_hierarchy  # doctest: +SKIP
   [<class 'bool'>, <class 'int'>, <class 'object'>]

   .. note:: Useful for understanding type relationships and finding common types.


.. py:function:: get_type_name(typ)

   Get a user-friendly name for a type object.

   Creates a more readable name for types, handling special cases like
   NoneType and properly formatting generic types.

   :param typ: The type to get a name for

   :returns: A user-friendly name for the type
   :rtype: str

   .. rubric:: Examples

   >>> get_type_name(int)
   'int'
   >>> get_type_name(type(None))
   'None'
   >>> get_type_name(Dict[str, int])  # doctest: +SKIP
   'Dict[str, int]'
   >>> get_type_name(List[str])  # doctest: +SKIP
   'List[str]'
   >>> get_type_name(List)  # doctest: +SKIP
   'List'

   .. note:: This function creates names similar to those used in type annotations.


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


.. py:function:: is_abstract_type(typ)

   Check if a type is abstract (cannot be instantiated directly).

   Determines whether a type is an abstract base class or interface
   that cannot be instantiated directly.

   :param typ: The type to check

   :returns: True if the type is abstract, False otherwise
   :rtype: bool

   .. rubric:: Examples

   >>> from abc import ABC, abstractmethod
   >>> class AbstractExample(ABC):
   ...     @abstractmethod
   ...     def method(self): pass
   >>> is_abstract_type(AbstractExample)  # doctest: +SKIP
   True
   >>> is_abstract_type(int)
   False

   .. note:: Identifies types that are meant to be inherited from rather than instantiated.


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


.. py:function:: is_generic_type(typ)

   Check if a type is a generic type.

   Determines whether a type is a parameterized generic type
   like List[int] rather than a concrete type like list.

   :param typ: The type to check

   :returns: True if the type is a generic type, False otherwise
   :rtype: bool

   .. rubric:: Examples

   >>> is_generic_type(List[int])  # doctest: +SKIP
   True
   >>> is_generic_type(list)
   False
   >>> is_generic_type(Dict[str, int])  # doctest: +SKIP
   True

   .. note:: Useful for handling generic types specially in type systems.


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


.. py:function:: is_primitive_type(typ)

   Check if a type is primitive.

   Primitive types are basic types like int, str, float, bool, etc.

   :param typ: The type to check

   :returns: True if the type is primitive, False otherwise
   :rtype: bool


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


.. py:function:: safe_bool_convert(value)

   Safely convert a value to bool with semantic interpretation.

   Performs intelligent boolean conversion with special handling for
   string values like "yes", "no", "true", "false", etc.

   :param value: Any value that might be convertible to bool.

   :returns:

             A boolean representation of the value, with common string patterns
                   like "yes"/"no" properly handled.
   :rtype: bool

   .. rubric:: Examples

   >>> safe_bool_convert(True)
   True
   >>> safe_bool_convert(1)
   True
   >>> safe_bool_convert("yes")
   True
   >>> safe_bool_convert("false")
   False
   >>> safe_bool_convert(0)
   False
   >>> safe_bool_convert([])
   False
   >>> safe_bool_convert([1, 2, 3])
   True
   >>> safe_bool_convert(None)
   False

   .. note::

      This function interprets strings like "yes", "true", "1", "y", "t", "on" as True,
      and "no", "false", "0", "n", "f", "off" as False.


.. py:function:: safe_float_convert(value)

   Safely convert a value to float or return None if invalid.

   Handles multiple input types including bool, int, float, and str.
   Guarantees no exceptions are raised during conversion.

   :param value: Any value that might be convertible to float.

   :returns: A float value or None if conversion is not possible.
   :rtype: Optional[float]

   .. rubric:: Examples

   >>> safe_float_convert(3.14)
   3.14
   >>> safe_float_convert("3.14")
   3.14
   >>> safe_float_convert(42)
   42.0
   >>> safe_float_convert(True)
   1.0
   >>> safe_float_convert("invalid") is None
   True
   >>> safe_float_convert(None) is None
   True
   >>> safe_float_convert("inf")
   inf
   >>> safe_float_convert("NaN")  # doctest: +ELLIPSIS
   nan

   .. note::

      This function silently handles all conversion errors by returning None.
      Special values like "inf", "-inf", and "nan" are properly handled.


.. py:function:: safe_int_convert(value)

   Safely convert a value to int or return None if invalid.

   Handles multiple input types including bool, int, float, str, and bytes.
   Guarantees no exceptions are raised during conversion.

   :param value: Any value that might be convertible to int.

   :returns: An int value or None if conversion is not possible.
   :rtype: Optional[int]

   .. rubric:: Examples

   >>> safe_int_convert(42)
   42
   >>> safe_int_convert("42")
   42
   >>> safe_int_convert(3.14)
   3
   >>> safe_int_convert(True)
   1
   >>> safe_int_convert("hello") is None
   True
   >>> safe_int_convert(None) is None
   True
   >>> safe_int_convert("0x10")  # Hex strings need explicit handling
   None

   .. note::

      This function silently handles all conversion errors by returning None.
      For hex/octal/binary strings, use the int(x, base) function directly.


.. py:function:: safe_str_convert(value)

   Safely convert a value to string with proper handling of various types.

   Provides special handling for bytes (UTF-8 decoding) and Path objects.
   Never raises exceptions, always returns a valid string.

   :param value: Any value to convert to string.

   :returns: String representation of the value. Empty string for None.
   :rtype: str

   .. rubric:: Examples

   >>> safe_str_convert("hello")
   'hello'
   >>> safe_str_convert(42)
   '42'
   >>> safe_str_convert(None)
   ''
   >>> safe_str_convert(b'hello')
   'hello'
   >>> from pathlib import Path
   >>> safe_str_convert(Path('/tmp'))  # doctest: +SKIP
   '/tmp'
   >>> safe_str_convert(b'\xff\xfe')  # Invalid UTF-8 falls back to str(bytes)
   "b'\xff\xfe'"

   .. note::

      This function attempts UTF-8 decoding for bytes objects and falls back
      to str(bytes) representation if decoding fails.


.. py:function:: standardize_type_name(name)

   Standardize a type name to a consistent format.

   Converts various styles of type names to a consistent format
   following PEP 484 conventions.

   :param name: The type name to standardize

   :returns: The standardized type name
   :rtype: str

   .. rubric:: Examples

   >>> standardize_type_name("int")
   'int'
   >>> standardize_type_name("list[int]")
   'List[int]'
   >>> standardize_type_name("Dict[str, list]")
   'Dict[str, List]'

   .. note:: Useful for ensuring consistent type naming across a codebase.


.. py:function:: try_convert(value, target_type)

   Convert a value to a target type with detailed error reporting.

   Unlike the safe_*_convert functions, this provides structured error information
   when conversion fails rather than just returning None.

   :param value: The value to convert
   :param target_type: The type to convert to

   :returns:

             A result object containing success status, converted value,
                                 and error information if conversion failed
   :rtype: ConversionResult[T]

   .. rubric:: Examples

   >>> result = try_convert("42", int)
   >>> result.success
   True
   >>> result.value
   42
   >>> result = try_convert("not_a_number", int)
   >>> result.success
   False
   >>> bool(result)
   False
   >>> result.error is not None
   True
   >>> result = try_convert(None, int)
   >>> result.success
   False

   .. note:: Captures and reports the actual exception that occurred during conversion.


.. py:data:: CollectionT

   Union type for common collection types with homogeneous elements.

   This type represents any of the standard Python collection types
   containing elements of the same type T, enabling generic collection operations.

   .. rubric:: Examples

   >>> # List collection
   >>> names: CollectionT[str] = ["Alice", "Bob", "Charlie"]
   >>>
   >>> # Dictionary collection
   >>> ages: CollectionT[int] = {"Alice": 30, "Bob": 25, "Charlie": 35}
   >>>
   >>> # Tuple collection
   >>> coordinates: CollectionT[float] = (1.0, 2.0, 3.0)
   >>>
   >>> # Set collection
   >>> unique_ids: CollectionT[int] = {1, 2, 3}

.. py:data:: CollectionTypes

   Container types that hold multiple values.

   Common Python collection implementations for type checking.

.. py:data:: ComparableT

.. py:data:: ComparableT_co

.. py:data:: ComparableT_contra

.. py:data:: ConverterMap

   Type conversion map linking type pairs to conversion functions.

   Base converter registry for dynamic type conversion systems.

.. py:data:: ConverterMapGeneric

   Generic converter map with parametric types.

   Flexible converter registry with generic type parameters for type-safe conversion
   between any source and destination types. Enables precise typing while maintaining
   adaptability for diverse conversion scenarios.

   :param T: Source type parameter for conversion input
   :param U: Target type parameter for conversion output

   .. admonition:: Example

      ```python
      converters: ConverterMapGeneric = {
          (int, str): lambda x: str(x),
          (str, int): lambda x: int(x)
      }
      ```

.. py:data:: ConverterMapSR

   Source-to-Result converter map with precise typing.

   Strongly-typed converter registry for specific type pairs.

   :param S: Source type parameter for conversion
   :param R: Result type parameter for conversion

.. py:data:: ConverterPriority

   Conversion priority map for resolving ambiguous conversions.

   Defines precedence when multiple conversion paths exist.

.. py:data:: DictKV

   Generic dictionary mapping keys of type K to values of type V.

   Type-safe dictionary with precise key and value types.

.. py:data:: DictKV_co

   Covariant dictionary allowing subtype keys and values.

   Dictionary supporting polymorphic key and value types.

.. py:data:: DictSchemaT

   Dictionary schema with hashable keys and values of type T.

   Foundation for schema-based validation of dictionary-like structures.

.. py:data:: DictSchemaT_co

   Covariant dictionary schema allowing subtypes for values.

   Flexible schema supporting polymorphic value types.

.. py:data:: DictSchemaT_contra

   Contravariant dictionary schema for specialized scenarios.

   Advanced schema type for contravariant validation cases.

.. py:data:: ErrorHandler

   Error to result handler recovering from specific errors.

   Converts error instances into valid results or None.

   :param error: Error instance to handle
   :type error: TError

   :returns: Recovered value or None if recovery impossible
   :rtype: Optional[T]

.. py:data:: ErrorMessage

   Human-readable error message for validation or conversion failures.

   Designed for clear communication of errors to end users or developers.

.. py:data:: FallbackProvider

   Provides fallback value when primary operations fail.

   Zero-argument function delivering consistent default values.

   :returns: Fallback value of specified type
   :rtype: T

.. py:data:: FieldDefinitions

   Structure field definitions mapping field names to types.

   Core definition type for structural type systems.

.. py:data:: FieldDefinitionsT

   Generic field definitions constrained to types of T.

   Enables structure definitions with type constraints.

.. py:data:: FieldDefinitionsT_co

   Covariant field definitions allowing subtypes of T_co.

   Supports field definitions with polymorphic type relationships.

.. py:data:: FieldDefinitionsT_contra

   Contravariant field definitions accepting supertypes of T_contra.

   Specialized field definitions for contravariant scenarios.

.. py:data:: FieldsWithDefaults

   Fields with default values mapping names to (type, default) pairs.

   Supports structural types with default values for optional fields.

.. py:data:: FieldsWithDefaultsT

   Generic fields with defaults constrained to specific types.

   Type-safe definition of fields with matching default values.

.. py:data:: FrozenSetT

   Generic frozen set with elements of type T.

   Type-safe immutable set with homogeneous elements.

.. py:data:: FrozenSetT_co

   Covariant frozen set allowing subtypes of T_co.

   Immutable set supporting polymorphic element types.

.. py:data:: HashableT

.. py:data:: HashableT_co

.. py:data:: HashableT_contra

.. py:data:: IterableT

   Generic iterable with elements of type T.

   Abstract iterable type for element traversal.

.. py:data:: IterableT_co

   Covariant iterable allowing subtypes of T_co.

   Iterable supporting polymorphic element types.

.. py:data:: IteratorT

   Generic iterator with elements of type T.

   Progressive access to elements of a sequence.

.. py:data:: IteratorT_co

   Covariant iterator allowing subtypes of T_co.

   Iterator supporting polymorphic element types.

.. py:data:: K

.. py:data:: K_co

.. py:data:: K_contra

.. py:data:: ListSchemaT

   List schema for array validation.

   This represents an array of items that conform to the schema type specified
   as the single element of the list.

   .. rubric:: Examples

   >>> int_list_schema: ListSchemaT = [int]
   >>> dict_list_schema: ListSchemaT = [{"name": str}]

.. py:data:: ListT

   Generic list with elements of type T.

   Type-safe list specification for homogeneous elements.

.. py:data:: ListT_co

   Covariant list allowing subtypes of T_co.

   List supporting polymorphic element types.

.. py:data:: MappingTypes

   Key-value mapping types for associative data.

   Dictionary-like types supporting key-based lookup.

.. py:data:: NumericTypes

   Numeric value types for mathematical operations.

   Types supporting arithmetic operations.

.. py:data:: OptionalConverter

   Optional-aware converter handling None values appropriately.

   Converts optional source values to optional result values.

   :param value: Source value or None
   :type value: Optional[S]

   :returns: Converted value or None if input was None/conversion failed
   :rtype: Optional[R]

.. py:data:: ParentSpecType

   Parent class specification supporting single class or tuple of classes.

   Used for inheritance definitions and interface specifications.

.. py:data:: ParentSpecType_co

   Covariant parent specification with subtype support.

   Flexibility for polymorphic inheritance relationships.

.. py:data:: ParentSpecType_contra

   Contravariant parent specification for specialized scenarios.

   Supports advanced type relationship definitions.

.. py:data:: PathSegmentT

   Type representing a single segment in a path for schema traversal.

   A path segment can be either a string key (for dictionary access)
   or an integer index (for list access).

   .. rubric:: Examples

   >>> key_segment: PathSegmentT = "name"  # Access dict key
   >>> index_segment: PathSegmentT = 0     # Access list index

.. py:data:: PathT

   List of path segments representing a traversal path through a nested structure.

   Paths enable precise targeting of nested elements within complex data structures,
   combining string keys and numeric indices as needed.

   .. rubric:: Examples

   >>> # Path to access user.addresses[0].street
   >>> path: PathT = ["user", "addresses", 0, "street"]

.. py:data:: PredicateFunc

   Boolean predicate function for type T.

   Decision function determining if value meets criteria.

   :param value: Value to test against predicate
   :type value: T

   :returns: True if value meets criteria, False otherwise
   :rtype: bool

.. py:data:: PredicateFunc_contra

   Contravariant predicate function accepting supertypes.

   Flexible decision function usable with parent types.

   :param value: Value (or any supertype) to test against predicate
   :type value: T_contra

   :returns: True if value meets criteria, False otherwise
   :rtype: bool

.. py:data:: PrimitiveTypes

   Basic value types directly supported by Python.

   Fundamental types with direct language support.

.. py:data:: R

.. py:data:: R_co

.. py:data:: R_contra

.. py:data:: S

.. py:data:: S_co

.. py:data:: S_contra

.. py:data:: SchemaNodeT

   Generic type variable for schema nodes during traversal operations.

   This enables strongly-typed traversal of schema structures where the
   specific node type can vary based on the context.

.. py:data:: SchemaSequenceT

   Sequence representation of schema for better covariance handling.

   This provides a read-only sequence for list schemas, enabling more
   flexible handling in validation and traversal functions.

.. py:data:: SchemaTypeMappingT

   Mapping representation of schema for better covariance handling.

   This provides a read-only view of the schema structure, allowing for
   more flexible usage in functions that only need to read schema information.

.. py:data:: SchemaTypeT

   Either a schema dictionary or a direct type reference.

   Flexible schema specification supporting both simple and complex cases.

.. py:data:: SchemaTypeT_co

   Covariant schema type with subtype support.

   Schema specification with polymorphic type relationships.

.. py:data:: SchemaTypeT_contra

   Contravariant schema type for specialized scenarios.

   Advanced schema specification for contravariant cases.

.. py:data:: SchemaValueNodeT

   Generic type variable for schema value nodes during validation.

   This provides type-specific handling for values being validated against
   schema definitions, allowing for context-aware validation logic.

.. py:data:: SchemaValueT

   Either a schema dictionary or a direct value.

   Represents data that conforms to a schema structure.

.. py:data:: SchemaValueT_co

   Covariant schema value with subtype support.

   Flexible value representation for polymorphic scenarios.

.. py:data:: SchemaValueT_contra

   Contravariant schema value for specialized scenarios.

   Advanced value representation for contravariant cases.

.. py:data:: SequenceT

   Generic sequence with elements of type T.

   Abstract sequence type for read-only sequential access.

.. py:data:: SequenceT_co

   Covariant sequence allowing subtypes of T_co.

   Sequence supporting polymorphic element types.

.. py:data:: SequenceTypes

   Ordered collection types maintaining element sequence.

   Sequential collection types for ordered data.

.. py:data:: SetT

   Generic set with elements of type T.

   Type-safe set specification guaranteeing uniqueness.

.. py:data:: SetT_co

   Covariant set allowing subtypes of T_co.

   Set supporting polymorphic element types.

.. py:data:: SetTypes

   Unordered unique collection types eliminating duplicates.

   Set-like collections guaranteeing uniqueness.

.. py:data:: SingleTypeT

   Type representing a single concrete type.

   This represents any Python type that can be used for validation,
   such as built-in types (int, str) or custom classes.

   .. rubric:: Examples

   >>> int_type: SingleTypeT = int
   >>> str_type: SingleTypeT = str
   >>> custom_type: SingleTypeT = MyClass

.. py:data:: T

.. py:data:: TCallable

.. py:data:: TCallable_co

.. py:data:: TCallable_contra

.. py:data:: TCollection

.. py:data:: TCollection_co

.. py:data:: TCollection_contra

.. py:data:: TError

.. py:data:: TError_co

.. py:data:: TError_contra

.. py:data:: TInstance

.. py:data:: TInstance_co

.. py:data:: TInstance_contra

.. py:data:: TValue

.. py:data:: TValue_co

.. py:data:: TValue_contra

.. py:data:: T_co

.. py:data:: T_contra

.. py:data:: TransformFunc

   Transformation function converting type T to type U.

   Pure function mapping between types with no side effects.

   :param value: Input value to transform
   :type value: T

   :returns: Transformed output value
   :rtype: U

.. py:data:: TransformFunc_co_contra

   Contravariant input, covariant output transformation.

   Advanced transformation supporting variance at both ends.

   :param value: Input value (or any supertype) to transform
   :type value: T_contra

   :returns: Transformed output value (or any subtype)
   :rtype: U_co

.. py:data:: TryResult

   Result of operation or error representing success/failure.

   Sum type pattern for success/failure outcomes without exceptions.

.. py:data:: TupleT

   Generic tuple with elements of type T.

   Type-safe immutable sequence with homogeneous elements.

.. py:data:: TupleT_co

   Covariant tuple allowing subtypes of T_co.

   Tuple supporting polymorphic element types.

.. py:data:: TypeConverter

   Type conversion function transforming S to optional R.

   Converts from source type to result type, potentially returning None on failure.

   :param value: Source value to convert
   :type value: S

   :returns: Successfully converted value or None if conversion fails
   :rtype: Optional[R]

.. py:data:: TypeConverterSafe

   Non-None type conversion function guaranteeing successful conversion.

   Guaranteed conversion from source to result with no failure cases.

   :param value: Source value to convert
   :type value: S

   :returns: Successfully converted value (never None)
   :rtype: R

.. py:data:: TypeDistance

   Measure of conversion complexity between types.

   Numeric representation of conversion difficulty:
   - 0: Identical types (no conversion needed)
   - 1: Direct subtype/supertype relationship
   - 2+: Increasing complexity of conversion

.. py:data:: TypeGuardFunc

   Type checking function for arbitrary objects.

   Runtime type verification for dynamic typing scenarios.

   :param value: Value to check for type compatibility
   :type value: object

   :returns: True if value matches expected type, False otherwise
   :rtype: bool

.. py:data:: TypeGuardFuncT

   Generic type guard function for specific types.

   Type-safe verification with known input types.

   :param value: Value to check for specific type compatibility
   :type value: T

   :returns: True if value matches expected type, False otherwise
   :rtype: bool

.. py:data:: TypeHierarchy

   Type to subtype hierarchy map for inheritance relationships.

   Represents inheritance trees for runtime type analysis.

.. py:data:: TypeIdentifier

   Type identified either by name string or class reference.

   Allows flexible type specification in APIs that accept either form.

.. py:data:: TypeMap

   Mapping between types for conversion or relationship definition.

   Foundation for type conversion systems.

.. py:data:: TypeMapFrom

   Source-specific type map defining conversions from type S.

   Specialized mapping for conversions from a specific source type.

.. py:data:: TypeMapSR

   Source-to-Result specific type map with precise typing.

   Fully-specified mapping between concrete source and result types.

.. py:data:: TypeMapTo

   Target-specific type map defining conversions to type R.

   Specialized mapping for conversions to a specific result type.

.. py:data:: TypeMatch

   Type matching result with relationship classification and distance.

   Complete analysis of relationship between two types.

.. py:data:: TypeName

   String identifier for a type (e.g., 'int', 'List[str]').

   Used for human-readable type references and registry operations.

.. py:data:: TypePath

   Dot-notation path to a type or attribute (e.g., 'module.submodule.MyClass').

   Used for dynamic type resolution and attribute access.

.. py:data:: TypePrecedence

   Type precedence for resolution of ambiguous type situations.

   Higher values indicate higher precedence in type selection.

.. py:data:: TypeRegistry

   Registry mapping type names to their corresponding type objects.

   Foundation for type lookup and registration systems.

.. py:data:: TypeRegistryT

   Generic type registry constrained to types of T.

   Enables type-safe registries for specific base types.

.. py:data:: TypeRegistryT_co

   Covariant type registry allowing subtypes of T_co.

   Suitable for registries where subtype polymorphism is desired.

.. py:data:: TypeRegistryT_contra

   Contravariant type registry accepting supertypes of T_contra.

   Specialized registry for cases requiring contravariant behavior.

.. py:data:: TypeRelationship

   Classification of relationship between two types.

   Precise categorization of how types relate to each other:
   - identical: Types are exactly the same
   - subtype: First type is a subtype of the second
   - supertype: First type is a supertype of the second
   - convertible: Types can be converted between each other
   - incompatible: No relationship exists between types

.. py:data:: U

.. py:data:: U_co

.. py:data:: U_contra

.. py:data:: UnionTypeT

   Tuple of types representing alternatives.

   This represents a set of alternative types, similar to Union but in runtime form.

   .. rubric:: Examples

   >>> union_type: UnionTypeT = (int, str)
   >>> multi_union: UnionTypeT = (int, float, str, bool)

.. py:data:: V

.. py:data:: V_co

.. py:data:: V_contra

.. py:data:: ValidationContext

   Context for validation process with shared state.

   Environmental information affecting validation decisions.

.. py:data:: ValidationFunc

   Type validation function for arbitrary objects.

   Basic validation with boolean result indicating validity.

   :param value: Value to validate
   :type value: object

   :returns: True if valid, False otherwise
   :rtype: bool

.. py:data:: ValidationFuncT

   Generic validation function for specific types.

   Type-safe validation for known input types.

   :param value: Value of type T to validate
   :type value: T

   :returns: True if valid, False otherwise
   :rtype: bool

.. py:data:: ValidationFuncT_contra

   Contravariant validation function accepting supertypes.

   Flexible validation function usable with parent types.

   :param value: Value of type T_contra or any supertype to validate
   :type value: T_contra

   :returns: True if valid, False otherwise
   :rtype: bool

.. py:data:: ValidationOptions

   Options for validation process customization.

   Configuration parameters affecting validation behavior.

.. py:data:: ValidationPath

   Path for validation error reporting (e.g., 'user.address.street').

   Provides structural context for validation errors in nested data.

.. py:data:: ValidationResult

   Primary validation outcome type for consistent usage.

   Canonical type for validation results throughout the system.

   :returns: Validation status and optional error message
   :rtype: Tuple[bool, Optional[ErrorMessage]]

.. py:data:: ValidationResultT

   Standard validation outcome with validity flag and optional error.

   Structured result providing validation status and explanation.

   :returns: Validation status and optional error message
   :rtype: Tuple[bool, Optional[ErrorMessage]]

.. py:data:: ValidationStrategy

   Strategic validation with configuration options.

   Configurable validation approach for complex scenarios.

   :param value: Value to validate
   :type value: T
   :param options: Configuration parameters
   :type options: ValidationOptions

   :returns: Validation outcome with status and error
   :rtype: ValidationResult

.. py:data:: ValidationWithPath

   Validation with path info for structural validation.

   Extended validation result with context path for nested structures.

   :returns:     Validation status, optional error message, and optional validation path
   :rtype: Tuple[bool, Optional[ErrorMessage], Optional[ValidationPath]]


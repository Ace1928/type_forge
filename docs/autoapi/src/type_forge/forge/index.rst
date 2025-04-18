.. py:module:: src.type_forge.forge

Type Forge: Advanced type manipulation and verification system.

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

   .. rubric:: Examples

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

   .. admonition:: Notes

      All functionality follows Eidosian principles of precision,
      recursive optimization, and perfect integration. The system
      maintains type safety at all abstraction levels while providing
      flexibility through well-defined transformation paths.

   .. rubric:: Attributes

   __version__ (str): Version number following semantic versioning.
   __author__ (str): Package author and maintainer details.

   .. seealso::

      - :mod:`type_forge.core`: Core type system components
      - :mod:`type_forge.typing`: Extended typing utilities
      - :mod:`type_forge.validators`: Validation framework


Package Contents
----------------

.. py:data:: R

.. py:data:: S

.. py:data:: T

.. py:data:: T_co

.. py:data:: T_contra

.. py:data:: __author__
      :value: 'TypeForge Team'


.. py:data:: __version__
      :value: '0.1.0'


.. py:data:: assert_type

.. py:data:: check_type

.. py:data:: convert_value

.. py:data:: create_type

.. py:data:: safe_convert

.. py:data:: validate

.. py:data:: validate_and_convert

.. py:data:: validate_dict_schema

.. py:data:: validate_recursive

.. py:data:: validate_type


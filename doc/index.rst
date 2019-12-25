.. code-block::

                   ____      _ _ ____
      _ __  _   _ / ___|__ _| | | __ ) _   _
     | '_ \| | | | |   / _` | | |  _ \| | | |
     | |_) | |_| | |__| (_| | | | |_) | |_| |
     | .__/ \__, |\____\__,_|_|_|____/ \__, |
     |_|    |___/                      |___/

pyCallBy Documentation
######################

Auxillary classes to implement call by reference.

Python does not allow a user to distinguish between *call-by-value* and *call-by-reference*
parameter passing. Python's standard types are passed by-value to a function or
method. Instances of a class are passed by-reference (pointer) to a function or
method.

By implementing a wrapper-class :class:`CallByRefParam`, any types value can be
passed by-reference. In addition, standard types like :class:`int` or :class:`bool`
can be handled by derived wrapper-classes.


Example
*******

.. code-block:: Python

   # define a call-by-reference parameter for integer values
   myInt = CallByRefIntParam()

   # a function using a call-by-reference parameter
   def func(param : CallByRefIntParam):
     param <= 3

   # call the function and pass the wrapper object
   func(myInt)

   print(myInt.value)



Contributors
************

* `Patrick Lehmann <https://github.com/Paebbels>`_ (Maintainer)



License
*******

This library is licensed under **Apache License 2.0**.

------------------------------------

.. |docdate| date:: %b %d, %Y - %H:%M

.. only:: html

   This document was generated on |docdate|.

.. toctree::
   :caption: Overview
   :hidden:

   Installation
   Dependencies


.. toctree::
   :caption: CallBy Classes
   :hidden:

   CommonClasses
   SpecialClasses


.. toctree::
   :caption: Appendix
   :hidden:

   License
   genindex

.. #
   py-modindex

![PyPI - License](https://img.shields.io/pypi/l/pyCallBy)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/Paebbels/pyCallBy) 
![GitHub release (latest by date)](https://img.shields.io/github/v/release/Paebbels/pyCallBy)
[![Documentation Status](https://readthedocs.org/projects/pycallby/badge/?version=latest)](https://pyCallBy.readthedocs.io/en/latest/?badge=latest)  
[![PyPI](https://img.shields.io/pypi/v/pyCallBy)](https://pypi.org/project/pyCallBy/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyCallBy)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/pyCallBy)
![PyPI - Status](https://img.shields.io/pypi/status/pyCallBy)

# pyCallBy

Auxillary classes to implement call by reference.

Python does not allow a user to distinguish between *call-by-value* and *call-by-reference*
parameter passing. Python's standard types are passed by-value to a function or
method. Instances of a class are passed by-reference (pointer) to a function or
method.

By implementing a wrapper-class `CallByRefParam`, any types value can be
passed by-reference. In addition, standard types like `int` or `bool`
can be handled by derived wrapper-classes.


## Example

```Python
# define a call-by-reference parameter for integer values
myInt = CallByRefIntParam()

# a function using a call-by-reference parameter
def func(param : CallByRefIntParam):
  param <= 3

# call the function and pass the wrapper object
func(myInt)

print(myInt.value)
```


## Contributors:

* [Patrick Lehmann](https://github.com/Paebbels) (Maintainer)


## License

This library is licensed under [Apache License 2.0](LICENSE.md)

-------------------------

SPDX-License-Identifier: Apache-2.0

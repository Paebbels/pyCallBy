[![PyPI - License](https://img.shields.io/pypi/l/pyCallBy?logo=PyPI)](LICENSE.md)
[![GitHub tag (latest SemVer incl. pre-release)](https://img.shields.io/github/v/tag/Paebbels/pyCallBy?logo=GitHub&include_prereleases)](https://github.com/Paebbels/pyCallBy/tags)
[![GitHub release (latest SemVer incl. including pre-releases)](https://img.shields.io/github/v/release/Paebbels/pyCallBy?logo=GitHub&include_prereleases)](https://github.com/Paebbels/pyCallBy/releases/latest)
[![GitHub release date](https://img.shields.io/github/release-date/Paebbels/pyCallBy?logo=GitHub&)](https://github.com/Paebbels/pyCallBy/releases)
[![Libraries.io status for latest release](https://img.shields.io/librariesio/release/pypi/pyCallBy)](https://libraries.io/github/Paebbels/pyCallBy)
[![Requires.io](https://img.shields.io/requires/github/Paebbels/pyCallBy)](https://requires.io/github/Paebbels/pyCallBy/requirements/?branch=master)  
[![Travis](https://img.shields.io/travis/com/Paebbels/pyCallBy?logo=Travis)](https://travis-ci.com/Paebbels/pyCallBy)
[![PyPI](https://img.shields.io/pypi/v/pyCallBy?logo=PyPI)](https://pypi.org/project/pyCallBy/)
![PyPI - Status](https://img.shields.io/pypi/status/pyCallBy?logo=PyPI)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyCallBy?logo=PyPI)
[![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/pyCallBy)](https://github.com/Paebbels/pyCallBy/network/dependents)  
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a738753f1b94494b9fa133584e70889c)](https://www.codacy.com/manual/Paebbels/pyCallBy)
[![Libraries.io SourceRank](https://img.shields.io/librariesio/sourcerank/pypi/pyCallBy)](https://libraries.io/github/Paebbels/pyCallBy/sourcerank)
[![Read the Docs](https://img.shields.io/readthedocs/pycallby)](https://pyCallBy.readthedocs.io/en/latest/)

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


## Contributors

* [Patrick Lehmann](https://github.com/Paebbels) (Maintainer)


## License

This library is licensed under [Apache License 2.0](LICENSE.md)

-------------------------

SPDX-License-Identifier: Apache-2.0

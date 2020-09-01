# EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
# vim: tabstop=2:shiftwidth=2:noexpandtab
# kate: tab-width 2; replace-tabs off; indent-width 2;
# =============================================================================
#                ____      _ _ ____
#   _ __  _   _ / ___|__ _| | | __ ) _   _
#  | '_ \| | | | |   / _` | | |  _ \| | | |
#  | |_) | |_| | |__| (_| | | | |_) | |_| |
#  | .__/ \__, |\____\__,_|_|_|____/ \__, |
#  |_|    |___/                      |___/
# =============================================================================
# Authors:            Patrick Lehmann
#
# Python unittest:    Testing the pyCallBy module
#
# Description:
# ------------------------------------
#		TODO
#
# License:
# ============================================================================
# Copyright 2017-2020 Patrick Lehmann - Bötzingen, Germany
# Copyright 2007-2016 Patrick Lehmann - Dresden, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
# ============================================================================
#
"""
pyAttributes
############

:copyright: Copyright 2007-2020 Patrick Lehmann - Bötzingen, Germany
:license: Apache License, Version 2.0
"""
from unittest     import TestCase

from pyCallBy     import CallByRefParam, CallByRefBoolParam, CallByRefIntParam


if __name__ == "__main__":
	print("ERROR: you called a testcase declaration file as an executable module.")
	print("Use: 'python -m unitest <testcase module>'")
	exit(1)

def func1(param : CallByRefParam):
	param <<= (3, 4)

def func2(param : CallByRefBoolParam):
	param <<= True

def func3(param : CallByRefIntParam):
	param <<= 42

class CallByReference_AnyParam(TestCase):
	ref : CallByRefParam = CallByRefParam()

	def setUp(self) -> None:
		func1(self.ref)

	def test_Value(self):
		self.assertTupleEqual(self.ref.value, (3, 4))

	def test_Equal(self):
		self.assertTrue(self.ref == (3, 4))

	def test_Unequal(self):
		self.assertTrue(self.ref != (4, 3))


class CallByReference_BoolParam(TestCase):
	ref : CallByRefBoolParam = CallByRefBoolParam()

	def setUp(self) -> None:
		func2(self.ref)

	def test_Value(self):
		self.assertTrue(self.ref.value)

	def test_Invert(self):
		self.assertFalse(not self.ref)

	def test_Equal(self):
		self.assertTrue(self.ref == True)

	def test_Unequal(self):
		self.assertTrue(self.ref != False)

	def test_And(self):
		self.assertTrue(self.ref & True)

	def test_Or(self):
		self.assertTrue(self.ref | False)

	def test_TypeConvertToBool(self):
		self.assertTrue(bool(self.ref))

	def test_TypeConvertToInt(self):
		self.assertEqual(int(self.ref), 1)


class CallByReference_IntParam(TestCase):
	ref : CallByRefIntParam = CallByRefIntParam()

	def setUp(self) -> None:
		func3(self.ref)

	def test_Value(self):
		self.assertEqual(self.ref.value, 42)

	def test_Negate(self):
		self.assertEqual(-self.ref, -42)

	def test_GeaterThanOrEqual(self):
		self.assertTrue(self.ref >= 40)

	def test_GreaterThan(self):
		self.assertTrue(self.ref >  41)

	def test_Equal(self):
		self.assertTrue(self.ref == 42)

	def test_Unequal(self):
		self.assertTrue(self.ref != 43)

	def test_LessThan(self):
		self.assertTrue(self.ref <  44)

	def test_LessThanOrEqual(self):
		self.assertTrue(self.ref <= 45)

	def test_Addition(self):
		self.assertEqual(self.ref + 1, 43)

	def test_Subtraction(self):
		self.assertEqual(self.ref - 1, 41)

	def test_Multiplication(self):
		self.assertEqual(self.ref * 1, 42)

	def test_Division(self):
		self.assertEqual(self.ref / 1, 42)

	def test_TypeConvertToBool(self):
		self.assertTrue(bool(self.ref))

	def test_TypeConvertToInt(self):
		self.assertEqual(int(self.ref), 42)

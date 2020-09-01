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

class CallByReference(TestCase):
	def test_ByRef(self):
		ref = CallByRefParam()
		func1(ref)
		self.assertTupleEqual(ref.value, (3, 4))

	def test_ByBoolRef(self):
		ref = CallByRefBoolParam()
		func2(ref)
		self.assertTrue(ref.value)

	def test_ByIntRef(self):
		ref = CallByRefIntParam()
		func3(ref)
		self.assertEqual(ref.value, 42)

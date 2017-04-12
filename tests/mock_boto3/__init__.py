# Copyright 2017 Yelp
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Mercilessly taunt THREE Amazonian river dolphins.

This is by no means a complete mock of boto3, just what we need for tests.
"""
from .case import MockBoto3TestCase
from .iam import MockIAMClient

# temporary shim
from .util import MockObject as MockEmrObject

# quiet pyflakes
MockBoto3TestCase
MockEmrObject
MockIAMClient

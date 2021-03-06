#!/usr/bin/env python
#
# Copyright (C) 2015 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Interface to NDK build information."""
import os
import sys

import tests.util as util


THIS_DIR = os.path.dirname(os.path.realpath(__file__))
NDK_ROOT = os.path.realpath(os.path.join(THIS_DIR, '..'))


def get_host_tag():
    if sys.platform.startswith('linux'):
        return 'linux-x86_64'
    elif sys.platform == 'darwin':
        return 'darwin-x86_64'
    elif sys.platform == 'win32':
        host_tag = 'windows-x86_64'
        test_path = os.path.join(os.environ['NDK'], 'prebuilt', host_tag)
        if not os.path.exists(test_path):
            host_tag = 'windows'
        return host_tag


def get_tool(tool):
    ext = ''
    if sys.platform == 'win32':
        ext = '.exe'

    host_tag = get_host_tag()
    prebuilt_path = os.path.join(os.environ['NDK'], 'prebuilt', host_tag)
    return os.path.join(prebuilt_path, 'bin', tool) + ext


def build(build_flags):
    ndk_build_path = os.path.join(os.environ['NDK'], 'ndk-build')
    if os.name == 'nt':
        return util.call_output(['cmd', '/c', ndk_build_path] + build_flags)
    return util.call_output([ndk_build_path] + build_flags)

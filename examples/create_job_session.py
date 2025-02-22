#!/usr/bin/env python 
# ___INFO__MARK_BEGIN__
#######################################################################################
# Copyright 2008-2022 Altair Engineering Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License.
#
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#######################################################################################
# ___INFO__MARK_END__

from drmaa2 import JobSession

if __name__ == '__main__':
    session_names = JobSession.list_session_names()
    print('Existing session names: %s' % session_names)
    session_name = 'js-01'
    print('Creating session with name: %s' % session_name)
    js = JobSession(session_name, destroy_on_exit=False)
    print('Got session object: %s' % js)
    session_names2 = JobSession.list_session_names()
    print('Current session names: %s' % session_names2)
    print('Opening new session with name: %s' % session_name)
    js2 = JobSession(session_name, destroy_on_exit=False)
    print('Got session object: %s' % js2)
    session_names2 = JobSession.list_session_names()
    print('Current session names: %s' % session_names2)

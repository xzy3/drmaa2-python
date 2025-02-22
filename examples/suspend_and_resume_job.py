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

import time
from drmaa2 import JobSession

if __name__ == '__main__':
    js = JobSession('js-01')
    j = js.run_job({'remote_command': '/bin/sleep', 'args': ['100']})
    ji = j.get_info()
    print('Submitted job info: %s' % ji)
    time.sleep(10)
    j.suspend()
    ji = j.get_info()
    print('Suspended job info: %s' % ji)

    time.sleep(10)
    j.resume()
    ji = j.get_info()
    print('Resumed job info: %s' % ji)

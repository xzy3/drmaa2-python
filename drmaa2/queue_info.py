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

from ctypes import POINTER
from ctypes import cast

from .byte_string import ByteString
from .drmaa2_constants import Cpu
from .drmaa2_constants import Os
from .drmaa2_ctypes import drmaa2_queueinfo
from .drmaa2_object import Drmaa2Object
from .drmaa2_exceptions import InvalidArgument

from .drmaa2_version_descriptor import Drmaa2VersionDescriptor


class QueueInfo(Drmaa2Object):
    """ High-level DRMAA2 queue info class. """

    name = Drmaa2Object.StringDescriptor('name')
    """ Queue name (str). """
    implementation_specific = Drmaa2Object.ImplSpecDescriptor('implementationSpecific')
    """ Implementation specific dictionary ({str:str}). """

    def __init__(self, queue_info):
        """ 
        Constructor. 

        :param queue_info: Low-level drmaa2_queueinfo struct.
        :type queue_info: drmaa2_queueinfo
        """
        Drmaa2Object.__init__(self)
        if isinstance(queue_info, POINTER(drmaa2_queueinfo)):
            self._struct = POINTER(drmaa2_queueinfo)()
            self._struct.contents = drmaa2_queueinfo()
            self.name = ByteString(getattr(queue_info.contents, 'name').value).decode()
            self.implementation_specific = getattr(queue_info.contents, 'implementationSpecific')
        else:
            raise InvalidArgument('Invalid argument: %s' % str(queue_info))
        self._read_only = True

    def __del__(self):
        pass

    @classmethod
    def get_implementation_specific_keys(cls):
        """
        Retrieve list of implementation-specific keys.

        :returns: String list of implementation-specific keys.

        >>> print(QueueInfo.get_implementation_specific_keys())
        []
        """
        if cls.implementation_specific_keys is None:
            cls.implementation_specific_keys = cls.to_py_string_list(
                cls.get_drmaa2_library().drmaa2_queueinfo_impl_spec())
        return cls.implementation_specific_keys

    @classmethod
    def to_py_queue_info_list(cls, ctypes_list):
        drmaa2_lib = cls.get_drmaa2_library()
        py_queue_info_list = list()
        if ctypes_list:
            count = drmaa2_lib.drmaa2_list_size(ctypes_list)
            cls.logger.debug('Converting ctypes queue info list of size {}'.format(count))
            for i in range(count):
                void_ptr = drmaa2_lib.drmaa2_list_get(ctypes_list, i)
                if void_ptr:
                    qi = cast(void_ptr, POINTER(drmaa2_queueinfo))
                    qi = QueueInfo(qi)
                    py_queue_info_list.append(qi)
                else:
                    ExceptionMapper.check_last_error_code()
                    py_queue_info_list.append(None)
        return py_queue_info_list

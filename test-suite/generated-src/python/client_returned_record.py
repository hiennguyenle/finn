# AUTOGENERATED FILE - DO NOT MODIFY!
# This file generated by Djinni from client_interface.djinni

from djinni.support import MultiSet # default imported in all files
from djinni.exception import CPyException # default imported in all files
from djinni.pycffi_marshal import CPyPrimitive, CPyRecord, CPyString
from PyCFFIlib_cffi import ffi, lib

from djinni import exception # this forces run of __init__.py which gives cpp option to call back into py to create exception

class ClientReturnedRecord:
    """ Record returned by a client """

    c_data_set = MultiSet()

    @staticmethod
    def check_c_data_set_empty():
        assert len(ClientReturnedRecord.c_data_set) == 0

    # Record deriving types
    def __hash__(self):
        # Pick an arbitrary non-zero starting value
        hash_code = 17
        hash_code = hash_code * 31 + self.record_id.__hash__()
        hash_code = hash_code * 31 + self.content.__hash__()
        hash_code = hash_code * 31 + self.misc.__hash__()
        return hash_code

    def __init__(self, record_id, content, misc):
        self.record_id = record_id
        self.content = content
        self.misc = misc


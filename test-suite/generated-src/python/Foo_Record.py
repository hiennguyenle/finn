# AUTOGENERATED FILE - DO NOT MODIFY!
# This file generated by Djinni from foo_duplicate_file_creation.djinni

from djinni.support import MultiSet # default imported in all files
from djinni.exception import CPyException # default imported in all files
from djinni.pycffi_marshal import CPyRecord, CPyString
from PyCFFIlib_cffi import ffi, lib

from djinni import exception # this forces run of __init__.py which gives cpp option to call back into py to create exception

class FooRecord:
    """
     this file is using mixed-case as in past this was causing
     duplicate files creation error
    """

    c_data_set = MultiSet()

    @staticmethod
    def check_c_data_set_empty():
        assert len(FooRecord.c_data_set) == 0


    def __init__(self, a):
        self.a = a


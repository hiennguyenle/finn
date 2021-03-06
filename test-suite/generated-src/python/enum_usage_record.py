# AUTOGENERATED FILE - DO NOT MODIFY!
# This file generated by Djinni from enum.djinni

from djinni.support import MultiSet # default imported in all files
from djinni.exception import CPyException # default imported in all files
from djinni.pycffi_marshal import CPyEnum, CPyObject, CPyObject, CPyObjectProxy, CPyRecord

from color import Color
from dh__list_enum_color import ListEnumColorHelper
from dh__map_enum_color_enum_color import MapEnumColorEnumColorHelper
from dh__map_enum_color_enum_color import MapEnumColorEnumColorProxy
from dh__set_enum_color import SetEnumColorHelper
from dh__set_enum_color import SetEnumColorProxy
from PyCFFIlib_cffi import ffi, lib

from djinni import exception # this forces run of __init__.py which gives cpp option to call back into py to create exception

class EnumUsageRecord:
    c_data_set = MultiSet()

    @staticmethod
    def check_c_data_set_empty():
        assert len(EnumUsageRecord.c_data_set) == 0
        Color.check_c_data_set_empty()
        ListEnumColorHelper.check_c_data_set_empty()
        SetEnumColorHelper.check_c_data_set_empty()
        MapEnumColorEnumColorHelper.check_c_data_set_empty()

    # Record deriving types
    def __hash__(self):
        # Pick an arbitrary non-zero starting value
        hash_code = 17
        hash_code = hash_code * 31 + self.e.__hash__()
        hash_code = hash_code * 31 + self.o.__hash__()
        hash_code = hash_code * 31 + self.l.__hash__()
        hash_code = hash_code * 31 + self.s.__hash__()
        hash_code = hash_code * 31 + self.m.__hash__()
        return hash_code

    def __init__(self, e, o, l, s, m):
        self.e = e
        self.o = o
        self.l = l
        self.s = s
        self.m = m


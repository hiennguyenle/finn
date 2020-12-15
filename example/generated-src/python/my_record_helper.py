# AUTOGENERATED FILE - DO NOT MODIFY!
# This file generated by Djinni from example.djinni

from djinni.support import MultiSet # default imported in all files
from djinni.exception import CPyException # default imported in all files
from djinni.pycffi_marshal import CPyBinary, CPyBoxedDate, CPyBoxedI16, CPyBoxedI32, CPyDate, CPyEnum, CPyObject, CPyObject, CPyObjectProxy, CPyPrimitive, CPyRecord, CPyString

from dh__list_binary import ListBinaryHelper
from dh__list_enum_my_enum import ListEnumMyEnumHelper
from dh__list_int32_t import ListInt32THelper
from dh__list_record_rc import ListRecordRcHelper
from dh__map_enum_my_enum_int16_t import MapEnumMyEnumInt16THelper
from dh__map_enum_my_enum_int16_t import MapEnumMyEnumInt16TProxy
from dh__map_int32_t_string import MapInt32TStringHelper
from dh__map_int32_t_string import MapInt32TStringProxy
from dh__set_enum_my_enum import SetEnumMyEnumHelper
from dh__set_enum_my_enum import SetEnumMyEnumProxy
from dh__set_int32_t import SetInt32THelper
from dh__set_int32_t import SetInt32TProxy
from my_enum import MyEnum
from rc import Rc
from rc_helper import RcHelper
from PyCFFIlib_cffi import ffi, lib

from djinni import exception # this forces run of __init__.py which gives cpp option to call back into py to create exception

from my_record import MyRecord

class MyRecordHelper:
    @staticmethod
    def release(c_ptr):
        assert c_ptr in c_data_set
        c_data_set.remove(ffi.cast("void*", c_ptr))

    @ffi.callback("int32_t(struct DjinniRecordHandle *)")
    def get_my_record_f1(cself):
        try:
            _ret = CPyPrimitive.fromPy(CPyRecord.toPy(None, cself).test)
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniBoxedI32 *(struct DjinniRecordHandle *)")
    def get_my_record_f2(cself):
        try:
            with CPyBoxedI32.fromPyOpt(CPyRecord.toPy(None, cself).test1) as py_obj:
                return py_obj.release_djinni_boxed()
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniObjectHandle *(struct DjinniRecordHandle *)")
    def get_my_record_f3(cself):
        try:
            _ret = CPyObject.fromPy(ListInt32THelper.c_data_set, CPyRecord.toPy(None, cself).test2)
            assert _ret != ffi.NULL
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniString *(struct DjinniRecordHandle *)")
    def get_my_record_f4(cself):
        try:
            with CPyString.fromPy(CPyRecord.toPy(None, cself).test3) as py_obj:
                _ret = py_obj.release_djinni_string()
                assert _ret != ffi.NULL
                return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniString *(struct DjinniRecordHandle *)")
    def get_my_record_f5(cself):
        try:
            with CPyString.fromPyOpt(CPyRecord.toPy(None, cself).test3_1) as py_obj:
                return py_obj.release_djinni_string()
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("uint64_t(struct DjinniRecordHandle *)")
    def get_my_record_f6(cself):
        try:
            _ret = CPyDate.fromPy(CPyRecord.toPy(None, cself).test4)
            assert _ret != ffi.NULL
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniBoxedDate *(struct DjinniRecordHandle *)")
    def get_my_record_f7(cself):
        try:
            with CPyBoxedDate.fromPyOpt(CPyRecord.toPy(None, cself).test4_1) as py_obj:
                return py_obj.release_djinni_boxed()
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniBinary *(struct DjinniRecordHandle *)")
    def get_my_record_f8(cself):
        try:
            with CPyBinary.fromPy(CPyRecord.toPy(None, cself).test5) as py_obj:
                _ret = py_obj.release_djinni_binary()
                assert _ret != ffi.NULL
                return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniObjectHandle *(struct DjinniRecordHandle *)")
    def get_my_record_f9(cself):
        try:
            _ret = CPyObject.fromPy(ListBinaryHelper.c_data_set, CPyRecord.toPy(None, cself).test6)
            assert _ret != ffi.NULL
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniObjectHandle *(struct DjinniRecordHandle *)")
    def get_my_record_f10(cself):
        try:
            _ret = CPyObjectProxy.fromPy(SetInt32THelper.c_data_set, SetInt32TProxy(CPyRecord.toPy(None, cself).test7))
            assert _ret != ffi.NULL
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniObjectHandle *(struct DjinniRecordHandle *)")
    def get_my_record_f11(cself):
        try:
            _ret = CPyObjectProxy.fromPy(MapInt32TStringHelper.c_data_set, MapInt32TStringProxy(CPyRecord.toPy(None, cself).test8))
            assert _ret != ffi.NULL
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniRecordHandle *(struct DjinniRecordHandle *)")
    def get_my_record_f12(cself):
        try:
            _ret = CPyRecord.fromPy(Rc.c_data_set, CPyRecord.toPy(None, cself).test9)
            assert _ret != ffi.NULL
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniOptionalRecordHandle *(struct DjinniRecordHandle *)")
    def get_my_record_f13(cself):
        try:
            return CPyRecord.fromPyOpt(Rc.c_data_set, CPyRecord.toPy(None, cself).test10)
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniObjectHandle *(struct DjinniRecordHandle *)")
    def get_my_record_f14(cself):
        try:
            _ret = CPyObject.fromPy(ListRecordRcHelper.c_data_set, CPyRecord.toPy(None, cself).test10_1)
            assert _ret != ffi.NULL
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("int(struct DjinniRecordHandle *)")
    def get_my_record_f15(cself):
        try:
            _ret = CPyEnum.fromPy(CPyRecord.toPy(None, cself).test11)
            assert _ret != -1
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("int(struct DjinniRecordHandle *)")
    def get_my_record_f16(cself):
        try:
            return CPyEnum.fromPyOpt(CPyRecord.toPy(None, cself).test13)
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniBoxedI16 *(struct DjinniRecordHandle *)")
    def get_my_record_f17(cself):
        try:
            with CPyBoxedI16.fromPyOpt(CPyRecord.toPy(None, cself).test14) as py_obj:
                return py_obj.release_djinni_boxed()
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniObjectHandle *(struct DjinniRecordHandle *)")
    def get_my_record_f18(cself):
        try:
            _ret = CPyObject.fromPy(ListEnumMyEnumHelper.c_data_set, CPyRecord.toPy(None, cself).test15)
            assert _ret != ffi.NULL
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniObjectHandle *(struct DjinniRecordHandle *)")
    def get_my_record_f19(cself):
        try:
            _ret = CPyObjectProxy.fromPy(SetEnumMyEnumHelper.c_data_set, SetEnumMyEnumProxy(CPyRecord.toPy(None, cself).test16))
            assert _ret != ffi.NULL
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniObjectHandle *(struct DjinniRecordHandle *)")
    def get_my_record_f20(cself):
        try:
            _ret = CPyObjectProxy.fromPy(MapEnumMyEnumInt16THelper.c_data_set, MapEnumMyEnumInt16TProxy(CPyRecord.toPy(None, cself).test17))
            assert _ret != ffi.NULL
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniRecordHandle *(int32_t,struct DjinniBoxedI32 *,struct DjinniObjectHandle *,struct DjinniString *,struct DjinniString *,uint64_t,struct DjinniBoxedDate *,struct DjinniBinary *,struct DjinniObjectHandle *,struct DjinniObjectHandle *,struct DjinniObjectHandle *,struct DjinniRecordHandle *,struct DjinniOptionalRecordHandle *,struct DjinniObjectHandle *,int,int,struct DjinniBoxedI16 *,struct DjinniObjectHandle *,struct DjinniObjectHandle *,struct DjinniObjectHandle *)")
    def python_create_my_record(test,test1,test2,test3,test3_1,test4,test4_1,test5,test6,test7,test8,test9,test10,test10_1,test11,test13,test14,test15,test16,test17):
        py_rec = MyRecord(
            CPyPrimitive.toPy(test),
            CPyBoxedI32.toPyOpt(test1),
            CPyObject.toPy(ListInt32THelper.c_data_set, test2),
            CPyString.toPy(test3),
            CPyString.toPyOpt(test3_1),
            CPyDate.toPy(test4),
            CPyBoxedDate.toPyOpt(test4_1),
            CPyBinary.toPy(test5),
            CPyObject.toPy(ListBinaryHelper.c_data_set, test6),
            CPyObjectProxy.toPyObj(SetInt32THelper.c_data_set, test7),
            CPyObjectProxy.toPyObj(MapInt32TStringHelper.c_data_set, test8),
            CPyRecord.toPy(Rc.c_data_set, test9),
            CPyRecord.toPyOpt(Rc.c_data_set, test10),
            CPyObject.toPy(ListRecordRcHelper.c_data_set, test10_1),
            CPyEnum.toPy(MyEnum, test11),
            CPyEnum.toPyOpt(MyEnum, test13),
            CPyBoxedI16.toPyOpt(test14),
            CPyObject.toPy(ListEnumMyEnumHelper.c_data_set, test15),
            CPyObjectProxy.toPyObj(SetEnumMyEnumHelper.c_data_set, test16),
            CPyObjectProxy.toPyObj(MapEnumMyEnumInt16THelper.c_data_set, test17))
        return CPyRecord.fromPy(MyRecord.c_data_set, py_rec) #to do: can be optional?

    @ffi.callback("void (struct DjinniRecordHandle *)")
    def __delete(dh):
        assert dh in MyRecord.c_data_set
        MyRecord.c_data_set.remove(dh)

    @staticmethod
    def _add_callbacks():
        lib.my_record_add_callback_get_my_record_f4(MyRecordHelper.get_my_record_f4)
        lib.my_record_add_callback_get_my_record_f15(MyRecordHelper.get_my_record_f15)
        lib.my_record_add_callback_get_my_record_f5(MyRecordHelper.get_my_record_f5)
        lib.my_record_add_callback_get_my_record_f16(MyRecordHelper.get_my_record_f16)
        lib.my_record_add_callback_get_my_record_f6(MyRecordHelper.get_my_record_f6)
        lib.my_record_add_callback_python_create_my_record(MyRecordHelper.python_create_my_record)
        lib.my_record_add_callback_get_my_record_f7(MyRecordHelper.get_my_record_f7)
        lib.my_record_add_callback_get_my_record_f10(MyRecordHelper.get_my_record_f10)
        lib.my_record_add_callback_get_my_record_f8(MyRecordHelper.get_my_record_f8)
        lib.my_record_add_callback_get_my_record_f17(MyRecordHelper.get_my_record_f17)
        lib.my_record_add_callback_get_my_record_f11(MyRecordHelper.get_my_record_f11)
        lib.my_record_add_callback_get_my_record_f1(MyRecordHelper.get_my_record_f1)
        lib.my_record_add_callback_get_my_record_f18(MyRecordHelper.get_my_record_f18)
        lib.my_record_add_callback_get_my_record_f2(MyRecordHelper.get_my_record_f2)
        lib.my_record_add_callback_get_my_record_f19(MyRecordHelper.get_my_record_f19)
        lib.my_record_add_callback_get_my_record_f9(MyRecordHelper.get_my_record_f9)
        lib.my_record_add_callback_get_my_record_f20(MyRecordHelper.get_my_record_f20)
        lib.my_record_add_callback_get_my_record_f3(MyRecordHelper.get_my_record_f3)
        lib.my_record_add_callback_get_my_record_f12(MyRecordHelper.get_my_record_f12)
        lib.my_record_add_callback___delete(MyRecordHelper.__delete)
        lib.my_record_add_callback_get_my_record_f13(MyRecordHelper.get_my_record_f13)
        lib.my_record_add_callback_get_my_record_f14(MyRecordHelper.get_my_record_f14)

MyRecordHelper._add_callbacks()


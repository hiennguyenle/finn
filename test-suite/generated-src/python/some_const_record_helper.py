# AUTOGENERATED FILE - DO NOT MODIFY!
# This file generated by Djinni from foo_constants.djinni

from djinni.support import MultiSet # default imported in all files
from djinni.exception import CPyException # default imported in all files
from djinni.pycffi_marshal import CPyPrimitive, CPyRecord
from PyCFFIlib_cffi import ffi, lib

from djinni import exception # this forces run of __init__.py which gives cpp option to call back into py to create exception

from some_const_record import SomeConstRecord

class SomeConstRecordHelper:
    @staticmethod
    def release(c_ptr):
        assert c_ptr in c_data_set
        c_data_set.remove(ffi.cast("void*", c_ptr))

    @ffi.callback("int16_t(struct DjinniRecordHandle *)")
    def get_some_const_record_f1(cself):
        try:
            _ret = CPyPrimitive.fromPy(CPyRecord.toPy(None, cself).number1)
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("int16_t(struct DjinniRecordHandle *)")
    def get_some_const_record_f2(cself):
        try:
            _ret = CPyPrimitive.fromPy(CPyRecord.toPy(None, cself).number2)
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniRecordHandle *(int16_t,int16_t)")
    def python_create_some_const_record(number1,number2):
        py_rec = SomeConstRecord(
            CPyPrimitive.toPy(number1),
            CPyPrimitive.toPy(number2))
        return CPyRecord.fromPy(SomeConstRecord.c_data_set, py_rec) #to do: can be optional?

    @ffi.callback("void (struct DjinniRecordHandle *)")
    def __delete(dh):
        assert dh in SomeConstRecord.c_data_set
        SomeConstRecord.c_data_set.remove(dh)

    @staticmethod
    def _add_callbacks():
        lib.some_const_record_add_callback_get_some_const_record_f1(SomeConstRecordHelper.get_some_const_record_f1)
        lib.some_const_record_add_callback_get_some_const_record_f2(SomeConstRecordHelper.get_some_const_record_f2)
        lib.some_const_record_add_callback___delete(SomeConstRecordHelper.__delete)
        lib.some_const_record_add_callback_python_create_some_const_record(SomeConstRecordHelper.python_create_some_const_record)

SomeConstRecordHelper._add_callbacks()


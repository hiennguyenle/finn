// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from interface_inheritance.djinni

#include "NativeInterfaceInheritanceConstant.hpp"  // my header
#include "Marshal.hpp"

namespace djinni_generated {

NativeInterfaceInheritanceConstant::NativeInterfaceInheritanceConstant() : ::djinni::JniInterface<::testsuite::InterfaceInheritanceConstant, NativeInterfaceInheritanceConstant>("com/dropbox/djinni/test/InterfaceInheritanceConstant$CppProxy") {}

NativeInterfaceInheritanceConstant::~NativeInterfaceInheritanceConstant() = default;

NativeInterfaceInheritanceConstant::JavaProxy::JavaProxy(JniType j) : Handle(::djinni::jniGetThreadEnv(), j) { }

NativeInterfaceInheritanceConstant::JavaProxy::~JavaProxy() = default;


CJNIEXPORT void JNICALL Java_com_dropbox_djinni_test_InterfaceInheritanceConstant_00024CppProxy_nativeDestroy(JNIEnv* jniEnv, jobject /*this*/, jlong nativeRef)
{
    try {
        DJINNI_FUNCTION_PROLOGUE1(jniEnv, nativeRef);
        delete reinterpret_cast<::djinni::CppProxyHandle<::testsuite::InterfaceInheritanceConstant>*>(nativeRef);
    } JNI_TRANSLATE_EXCEPTIONS_RETURN(jniEnv, )
}

}  // namespace djinni_generated
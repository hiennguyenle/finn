// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from interface_inheritance.djinni

#include "NativeBaseObjcJavaInterfaceInheritance.hpp"  // my header
#include "Marshal.hpp"

namespace djinni_generated {

NativeBaseObjcJavaInterfaceInheritance::NativeBaseObjcJavaInterfaceInheritance() : ::djinni::JniInterface<::testsuite::BaseObjcJavaInterfaceInheritance, NativeBaseObjcJavaInterfaceInheritance>() {}

NativeBaseObjcJavaInterfaceInheritance::~NativeBaseObjcJavaInterfaceInheritance() = default;

NativeBaseObjcJavaInterfaceInheritance::JavaProxy::JavaProxy(JniType j) : Handle(::djinni::jniGetThreadEnv(), j) { }

NativeBaseObjcJavaInterfaceInheritance::JavaProxy::~JavaProxy() = default;

std::string NativeBaseObjcJavaInterfaceInheritance::JavaProxy::base_method() {
    auto jniEnv = ::djinni::jniGetThreadEnv();
    ::djinni::JniLocalScope jscope(jniEnv, 10);
    const auto& data = ::djinni::JniClass<::djinni_generated::NativeBaseObjcJavaInterfaceInheritance>::get();
    auto jret = (jstring)jniEnv->CallObjectMethod(Handle::get().get(), data.method_baseMethod);
    ::djinni::jniExceptionCheck(jniEnv);
    return ::djinni::String::toCpp(jniEnv, jret);
}
std::string NativeBaseObjcJavaInterfaceInheritance::JavaProxy::override_method() {
    auto jniEnv = ::djinni::jniGetThreadEnv();
    ::djinni::JniLocalScope jscope(jniEnv, 10);
    const auto& data = ::djinni::JniClass<::djinni_generated::NativeBaseObjcJavaInterfaceInheritance>::get();
    auto jret = (jstring)jniEnv->CallObjectMethod(Handle::get().get(), data.method_overrideMethod);
    ::djinni::jniExceptionCheck(jniEnv);
    return ::djinni::String::toCpp(jniEnv, jret);
}

}  // namespace djinni_generated
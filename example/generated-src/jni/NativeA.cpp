// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from example.djinni

#include "NativeA.hpp"  // my header
#include "JNIMarshal+Json.h"
#include "Marshal.hpp"

namespace djinni_generated {

NativeA::NativeA() = default;

NativeA::~NativeA() = default;

auto NativeA::fromCpp(JNIEnv* jniEnv, const CppType& c) -> ::djinni::LocalRef<JniType> {
    const auto& data = ::djinni::JniClass<NativeA>::get();
    auto r = ::djinni::LocalRef<JniType>{jniEnv->NewObject(data.clazz.get(), data.jconstructor,
                                                           ::djinni::get(::djinni::U8::fromCpp(jniEnv, c.h)))};
    ::djinni::jniExceptionCheck(jniEnv);
    return r;
}

auto NativeA::toCpp(JNIEnv* jniEnv, JniType j) -> CppType {
    ::djinni::JniLocalScope jscope(jniEnv, 2);
    assert(j != nullptr);
    const auto& data = ::djinni::JniClass<NativeA>::get();
    return {::djinni::U8::toCpp(jniEnv, jniEnv->GetShortField(j, data.field_mH))};
}

}  // namespace djinni_generated

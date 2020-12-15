// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from example.djinni

#pragma once

#include "djinni_support.hpp"
#include "my_enum.hpp"

namespace djinni_generated {

class NativeMyEnum final : ::djinni::JniEnum {
public:
    using CppType = ::textsort::my_enum;
    using JniType = jobject;

    using Boxed = NativeMyEnum;

    static CppType toCpp(JNIEnv* jniEnv, JniType j) { return static_cast<CppType>(::djinni::JniClass<NativeMyEnum>::get().ordinal(jniEnv, j)); }
    static ::djinni::LocalRef<JniType> fromCpp(JNIEnv* jniEnv, CppType c) { return ::djinni::JniClass<NativeMyEnum>::get().create(jniEnv, static_cast<jint>(c)); }

private:
    NativeMyEnum() : JniEnum("com/dropbox/textsort/MyEnum") {}
    friend ::djinni::JniClass<NativeMyEnum>;
};

}  // namespace djinni_generated

// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from example.djinni

#import <DjinniExample/DjinniExample-Swift.h>
#include "rc.hpp"

static_assert(__has_feature(objc_arc), "Djinni requires ARC to be enabled for this file");

@class Rc;

namespace djinni_generated {

struct RcHelper
{
    using CppType = ::textsort::Rc;
    using ObjcType = Rc*;

    using Boxed = RcHelper;

    static CppType toCpp(ObjcType objc);
    static ObjcType fromCpp(const CppType& cpp);
};

}  // namespace djinni_generated

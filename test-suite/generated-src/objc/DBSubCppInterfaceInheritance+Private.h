// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from interface_inheritance.djinni

#include "sub_cpp_interface_inheritance.hpp"
#import "DBBaseCppInterfaceInheritance+Private.h"
#include <memory>

static_assert(__has_feature(objc_arc), "Djinni requires ARC to be enabled for this file");

@class DBSubCppInterfaceInheritance;

namespace djinni_generated {

class SubCppInterfaceInheritance
{
public:
    using CppType = std::shared_ptr<::testsuite::SubCppInterfaceInheritance>;
    using CppOptType = std::shared_ptr<::testsuite::SubCppInterfaceInheritance>;
    using ObjcType = DBSubCppInterfaceInheritance*;

    using Boxed = SubCppInterfaceInheritance;

    static CppType toCpp(ObjcType objc);
    static ObjcType fromCppOpt(const CppOptType& cpp);
    static ObjcType fromCpp(const CppType& cpp) { return fromCppOpt(cpp); }

private:
    class ObjcProxy;
};

}  // namespace djinni_generated

// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from single_language_interfaces.djinni

#include <iostream> // for debugging
#include <cassert>
#include "wrapper_marshal.hpp"
#include "java_only_listener.hpp"

#include "cw__java_only_listener.hpp"

std::shared_ptr<::testsuite::JavaOnlyListener> DjinniWrapperJavaOnlyListener::get(djinni::WrapperRef<DjinniWrapperJavaOnlyListener> dw) {
    if (dw) {
        return dw->wrapped_obj;
    }
    return nullptr;
}

void java_only_listener___wrapper_add_ref(DjinniWrapperJavaOnlyListener * dh) {
    dh->ref_count.fetch_add(1);
}
void java_only_listener___wrapper_dec_ref(DjinniWrapperJavaOnlyListener * dh) {
    const size_t ref = dh->ref_count.fetch_sub(1);
    if (ref == 1) {// value before sub is returned
        delete dh;
    }
}
djinni::Handle<DjinniWrapperJavaOnlyListener> DjinniWrapperJavaOnlyListener::wrap(std::shared_ptr<::testsuite::JavaOnlyListener> obj) {
    if (obj)
        return djinni::Handle<DjinniWrapperJavaOnlyListener>(new DjinniWrapperJavaOnlyListener{ std::move(obj) }, java_only_listener___wrapper_dec_ref);
    return nullptr;
}


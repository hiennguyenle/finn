// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from foo_interface.djinni

#pragma once // python_cdef_ignore
#include <stdbool.h>  // python_cdef_ignore

#include <stdint.h> // python_cdef_ignore

struct DjinniWrapperFooInterface;
void foo_interface___wrapper_dec_ref(struct DjinniWrapperFooInterface * dh);
void foo_interface___wrapper_add_ref(struct DjinniWrapperFooInterface * dh);

int32_t cw__foo_interface_int32_inverse(struct DjinniWrapperFooInterface * djinni_this, int32_t x);

void cw__foo_interface_set_private_int32(struct DjinniWrapperFooInterface * djinni_this, int32_t private_int);

int32_t cw__foo_interface_get_private_int32(struct DjinniWrapperFooInterface * djinni_this);

void cw__foo_interface_set_private_string(struct DjinniWrapperFooInterface * djinni_this, struct DjinniString * private_string);

struct DjinniString * cw__foo_interface_get_private_string(struct DjinniWrapperFooInterface * djinni_this);

struct DjinniString * cw__foo_interface_get_set_strings(struct DjinniWrapperFooInterface * djinni_this, struct DjinniString * ps1, struct DjinniString * ps2);

struct DjinniWrapperFooInterface * cw__foo_interface_create(void);

struct DjinniWrapperFooPrimitives * cw__foo_interface_get_foo_primitives(struct DjinniWrapperFooInterface * djinni_this);


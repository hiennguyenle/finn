// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from example.djinni

#pragma once

#include "rc.hpp"
#include <json+extension.hpp>
#include <json.hpp>

namespace nlohmann {

template <>
struct adl_serializer<::textsort::Rc>  {
    static ::textsort::Rc from_json(const json & j)  {
        auto result = ::textsort::Rc();
        if (j.contains("a")) {
            j.at("a").get_to(result.a);
        }
        if (j.contains("b")) {
            j.at("b").get_to(result.b);
        }
        if (j.contains("c")) {
            j.at("c").get_to(result.c);
        }
        if (j.contains("e")) {
            j.at("e").get_to(result.e);
        }
        return result;
    }
    static void to_json(json & j, ::textsort::Rc item)  {
        j = json {
            {"a", item.a},
            {"b", item.b},
            {"c", item.c},
            {"d", item.d},
            {"e", item.e}
        }
        ;
    }
}
;

}  // namespace nlohmann

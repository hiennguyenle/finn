// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from example.djinni

#pragma once

#include "my_enum.hpp"
#include <cstdint>
#include <json+extension.hpp>
#include <json.hpp>
#include <optional>
#include <string>
#include <utility>
#include <vector>

namespace textsort {

struct  Rc {
    int32_t a;
    int32_t b;
    std::optional<int32_t> c;
    my_enum d;
    std::vector<uint8_t> e;

    Rc(int32_t a_,
       int32_t b_,
       std::optional<int32_t> c_,
       my_enum d_,
       std::vector<uint8_t> e_)
    : a(std::move(a_))
    , b(std::move(b_))
    , c(std::move(c_))
    , d(std::move(d_))
    , e(std::move(e_))
    {}

    Rc() = default;
};

}  // namespace textsort


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
}

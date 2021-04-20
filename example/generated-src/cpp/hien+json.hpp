// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from example.djinni

#pragma once

#include "hien.hpp"
#include "json+extension.hpp"
#include "json.hpp"
#include <cstdint>

namespace nlohmann {

template <>
struct adl_serializer<::textsort::Hien>  {
    static ::textsort::Hien from_json(const json & j)  {
        auto result = ::textsort::Hien();
        if (j.contains("val")) {
            j.at("val").get_to(result.val);
        }
        return result;
    }
    static void to_json(json & j, const ::textsort::Hien & item)  {
        j = json {
            {"val", item.val}
        };
    }
};

}  // namespace nlohmann
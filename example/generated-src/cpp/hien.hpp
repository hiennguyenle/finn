// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from example.djinni

#pragma once

#include "json.hpp"
#include <cstdint>
#include <string>
#include <utility>

namespace textsort {

struct  Hien {
    int8_t val;

    Hien(int8_t val_)
    : val(std::move(val_))
    {}

    Hien() = default;
    virtual nlohmann::json to_json() const;
};

}  // namespace textsort
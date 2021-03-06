// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from foo_client_interface.djinni

#pragma once

#include "foo_some_other_record.hpp"
#include <cstdint>
#include <string>
#include <utility>

namespace testsuite {

struct FooClientReturnedRecord final {
    int64_t record_id;
    std::string content;
    FooSomeOtherRecord some_record;

    friend bool operator==(const FooClientReturnedRecord& lhs, const FooClientReturnedRecord& rhs);
    friend bool operator!=(const FooClientReturnedRecord& lhs, const FooClientReturnedRecord& rhs);

    friend bool operator<(const FooClientReturnedRecord& lhs, const FooClientReturnedRecord& rhs);
    friend bool operator>(const FooClientReturnedRecord& lhs, const FooClientReturnedRecord& rhs);

    friend bool operator<=(const FooClientReturnedRecord& lhs, const FooClientReturnedRecord& rhs);
    friend bool operator>=(const FooClientReturnedRecord& lhs, const FooClientReturnedRecord& rhs);

    FooClientReturnedRecord(int64_t record_id_,
                            std::string content_,
                            FooSomeOtherRecord some_record_)
    : record_id(std::move(record_id_))
    , content(std::move(content_))
    , some_record(std::move(some_record_))
    {}
};

}  // namespace testsuite

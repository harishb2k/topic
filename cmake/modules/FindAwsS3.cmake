

find_library(
        aws_checksums_LIBRARIES
        NAMES aws-checksums
)
find_library(
        aws_cpp_sdk_kinesis_LIBRARIES
        NAMES aws-cpp-sdk-kinesis
)
find_library(
        aws_cpp_sdk_s3_LIBRARIES
        NAMES aws-cpp-sdk-s3
)
find_library(
        aws_cpp_sdk_transfer_LIBRARIES
        NAMES aws-cpp-sdk-transfer
)
find_library(
        aws_cpp_sdk_core_LIBRARIES
        NAMES aws-cpp-sdk-core
)
find_library(
        aws_c_event_stream_LIBRARIES
        NAMES aws-c-event-stream
)
find_library(
        aws_c_common_LIBRARIES
        NAMES aws-c-common
)

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(AwsS3 DEFAULT_MSG
        aws_checksums_LIBRARIES
        aws_cpp_sdk_kinesis_LIBRARIES
        aws_cpp_sdk_s3_LIBRARIES
        aws_cpp_sdk_transfer_LIBRARIES
        aws_cpp_sdk_core_LIBRARIES
        aws_c_event_stream_LIBRARIES
        aws_c_common_LIBRARIES
        )


list(APPEND AWS_S3_LIBRARIES ${aws_checksums_LIBRARIES} ${aws_cpp_sdk_kinesis_LIBRARIES} ${aws_cpp_sdk_s3_LIBRARIES} ${aws_cpp_sdk_transfer_LIBRARIES} ${aws_cpp_sdk_core_LIBRARIES} ${aws_c_event_stream_LIBRARIES} ${aws_c_common_LIBRARIES})

if (AwsS3_FOUND)
    add_library(AwsS3 UNKNOWN IMPORTED)
    set_target_properties(AwsS3
            PROPERTIES
            IMPORTED_LOCATION  ${aws_checksums_LIBRARIES} ${aws_cpp_sdk_kinesis_LIBRARIES} ${aws_cpp_sdk_s3_LIBRARIES} ${aws_cpp_sdk_transfer_LIBRARIES} ${aws_cpp_sdk_core_LIBRARIES} ${aws_c_event_stream_LIBRARIES} ${aws_c_common_LIBRARIES}
            )
endif ()

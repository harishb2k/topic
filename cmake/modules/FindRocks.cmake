# - Find RocksDb-Cloud
# Find the lz4 compression library and includes
#
# ROCKS_INCLUDE_DIRS - where to find rocksdb/db.h, etc.
# ROCKS_LIBRARIES - List of libraries when using rocksdb.
# ROCKS_FOUND - True if rocksdb found.

find_path(
        ROCKS_INCLUDE_DIRS
        NAMES rocksdb/db.h
)

find_library(
        ROCKS_LIBRARIES
        NAMES rocksdb
)

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(Rocks DEFAULT_MSG ROCKS_LIBRARIES ROCKS_INCLUDE_DIRS)

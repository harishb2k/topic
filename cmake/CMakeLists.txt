cmake_minimum_required(VERSION 3.18)
project(thread_example)
set(CMAKE_CXX_STANDARD 14)

# This will let you include "mason"
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")

include(mason)

set(MASON_BOOST_VERSION "1.65.1")

# This is mandatory to get all headers for Boost  -> MASON_PACKAGE_boost_INCLUDE_DIRS will be filled
mason_use(boost VERSION ${MASON_BOOST_VERSION} HEADER_ONLY)

# Add any boost lib you want -> MASON_PACKAGE_boost_libthread_STATIC_LIBS will be avaliable
mason_use(boost_libthread VERSION ${MASON_BOOST_VERSION})

add_executable(${PROJECT_NAME} main.cpp)

# Add static libs and include to your code
target_include_directories(${PROJECT_NAME} PRIVATE ${MASON_PACKAGE_boost_INCLUDE_DIRS})
target_link_libraries(${PROJECT_NAME} ${MASON_PACKAGE_boost_libthread_STATIC_LIBS})
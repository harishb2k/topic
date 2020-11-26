put the mason.cmake file in the cmake dir in the project


Some important packages
```
find_package(lz4 REQUIRED)
find_package(JeMalloc REQUIRED)
find_package(Snappy REQUIRED)
find_package(zstd REQUIRED)
find_package(CURL REQUIRED)
find_package(Mac REQUIRED)

${CURL_LIBRARIES}
        ${JeMalloc_LIBRARIES}
        ${Snappy_LIBRARIES}
        ${lz4_LIBRARIES}
        ${zstd_LIBRARIES}
        ${ROCKS_LIBRARIES}
        ${MAC_CORE_FRAMEWORK}
```

# Use CoreFoundation if this build is running in MacOS
if (APPLE)
    set(MAC_CORE_FRAMEWORK
            "-framework CoreFoundation"
            "-framework CoreFoundation"
            "-framework CoreGraphics"
            "-framework CoreData"
            "-framework CoreText"
            "-framework Security"
            "-framework Foundation"
            "-Wl,-U,_MallocExtension_ReleaseFreeMemory"
            "-Wl,-U,_ProfilerStart"
            "-Wl,-U,_ProfilerStop"
            )
else ()
    set(MAC_CORE_FRAMEWORK "")
endif ()
FindProto:
https://raw.githubusercontent.com/Kitware/CMake/master/Modules/FindProtobuf.cmake


find_package(Protobuf REQUIRED)
include_directories(${Protobuf_INCLUDE_DIRS})
protobuf_generate_cpp(PROTO_SRCS PROTO_HDRS proto/example.proto)

PROTO_SRCS and PROTO_HDRS - these will be populated

# Add proto to your exe
add_executable(helloworld main.cpp ${PROTO_SRCS} ${PROTO_HDRS})


# Link Proto Libs
target_link_libraries(helloworld LINK_PUBLIC ${Protobuf_LIBRARIES})




# Write data to buffer
tutorial::Person person;
person.set_name("Some Name");
person.set_email("a@gmail.com");
person.set_id(10);
void *buffer = malloc(person.ByteSizeLong());
person.SerializeToArray(buffer, person.ByteSizeLong());


# Read object from buffer
tutorial::Person person1;
bool n1 = person1.ParseFromArray(data, size);
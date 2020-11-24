
#include <child/child.h>
#include <zmq.h>
#include <czmq.h>
#include <zsock.h>
#include <cstdlib>
#include <iostream>
#include<thread>

int main() {
  child_hello();

  std::thread thread_object1([]() {
    zsock_t * writer = zsock_new_pair("@tcp://127.0.0.1:5560");

    int i = 0;
    while (i++ < 1000) {
      zmsg_t *msg = zmsg_new();

      zframe_t *frame = zframe_new("HelloHelloHelloHello", 20);
      zmsg_prepend(msg, &frame);

      int rc = zmsg_send(&msg, writer);

      zframe_destroy(&frame);
      zmsg_destroy(&msg);

      std::cout << i << " Sender: rc=" << rc << std::endl;
      usleep(1000);

      zmsg_t *msg1 = zmsg_recv(writer);
      zframe_t *f = zmsg_pop(msg1);
      byte *data = zframe_data(f);
      std::string s((char *) data, zframe_size(f));
      std::cout << i << " Receive: rc=[" << s << "] size=" << zframe_size(f) << std::endl;
      zframe_destroy(&f);
      zmsg_destroy(&msg1);

    }
  });

  std::thread thread_object([]() {
    zsock_t * writer = zsock_new_pair (">tcp://127.0.0.1:5560");
    int i = 0;
    while (i++ < 1000) {
      zmsg_t *msg = zmsg_recv(writer);
      zframe_t *f = zmsg_pop(msg);
      byte *data = zframe_data(f);
      std::string s((char *) data, zframe_size(f));
      std::cout << i << " Receive: rc=[" << s << "] size=" << zframe_size(f) << std::endl;
      zframe_destroy(&f);
      zmsg_destroy(&msg);


      zmsg_t *msg1  = zmsg_new();
      zframe_t *frame = zframe_new("HelloHelloHelloHello-Response", 30);
      zmsg_prepend(msg1, &frame);
      int rc = zmsg_send(&msg1, writer);
      std::cout << i << " Receive_Sender: rc=" << rc << std::endl;
      zframe_destroy(&frame);
      zmsg_destroy(&msg1);
    }
  });

  std::cout << "Wait" << std::endl;
  sleep(10000);
  return 0;
}

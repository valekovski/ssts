#include <iostream>
#include <string>

const char* new_string() {
  char* test = "test";
  std::cout << "test je " << test << std::endl;

  return test;
}

int main(int argc, char** argv) {
  const char* test2 = new_string();
  std::cout << "test2 je " << test2 << std::endl;

  return 0;
}
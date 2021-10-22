#include <iostream>
#include <cstdlib>
#include <ctime>

const int ELEM_NUM = 20;


void print_array(int* data) {

  for (int i = 0; i < ELEM_NUM; ++i) {
    std::cout << data[i] << " ";
  }
  std::cout << std::endl;
}

void swap(int* left, int* right) {
  int tmp = *left;
  *left = *right;
  *right = tmp;
}

int razdeli(int* data, int start, int end) {
  int pivot = data[end];
  int left_idx = start;
  int right_idx = end-1;

  while (left_idx < right_idx) {
    while (data[left_idx] <= pivot && left_idx < end) {
      ++left_idx;
    }
    while (data[right_idx] > pivot && right_idx > 0) {
      --right_idx;
    }
    if (left_idx < right_idx) {
      swap(&data[left_idx], &data[right_idx]);
    }
  }
  swap(&data[end], &data[left_idx]);

  return left_idx;
}

void quicksort(int* data, int start, int end) {
  if (start >= end) return;

  int pivot_idx = razdeli(data, start, end);

  quicksort(data, start, pivot_idx - 1);
  quicksort(data, pivot_idx + 1, end);
}

int main(int argc, char** argv) {
  int data[ELEM_NUM];

  srand(time(NULL));

  for (int i = 0; i < ELEM_NUM; ++i) {
    int curr_num = rand()%20;
    data[i] = curr_num;
  }

  print_array(data);
  quicksort(data, 0, ELEM_NUM-1);
  print_array(data);

  return 0;
}
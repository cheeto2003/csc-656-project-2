#include <algorithm>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <random>
#include <vector>
#include <string.h>

#include "sums.h"

void 
setup(int64_t N, int64_t A[])
{
   printf(" inside sum_vector problem_setup, N=%lld \n", N);
   for (int64_t i = 0; i < N; ++i) {
      A[i] = i;     //0 to N-1
   }
}

int64_t
sum(int64_t N, int64_t A[])
{
   printf(" inside sum_vector perform_sum, N=%lld \n", N);
   int64_t acc = 0;
   for (int64_t i = 0; i < N; ++i) {
      acc += A[i];
   }
   return acc; //changed from 0 to retrn the sum
}


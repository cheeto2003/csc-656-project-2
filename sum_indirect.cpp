#include <algorithm>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <random>
#include <vector>
#include <string.h>
#include <stdlib.h>    //for lrand48 and srand48

#include "sums.h"

static std::vector<int64_t> B;  // data array used by indirection

void 
setup(int64_t N, int64_t A[])
{
   printf(" inside sum_indirect problem_setup, N=%lld \n", (long long)N);
   B.resize(N);
   for (int64_t i = 0; i < N; ++i) B[i] = i;       // data values
   srand48(1);                                     // deterministic
   for (int64_t i = 0; i < N; ++i) A[i] = lrand48() % N;  // A holds random indices 0 to N-1

}

int64_t
sum(int64_t N, int64_t A[])
{
   printf(" inside sum_indirect perform_sum, N=%lld \n", (long long)N);
   int64_t acc = 0;
   for (int64_t i = 0; i < N; ++i) {
      int64_t j = A[i];   // 1st load (index)
      acc += B[j];        // 2nd load (indirect)
   }
   return acc;
}


"""
Have not solved this, can be bounded by sqrt(N). Integer factorization problem.

"""
from typing import List


class Solution:
    def cns(self, N: int) -> List[List[int]]:
        results = [[N]]

        upper_bound = int(N ** 0.5) + 1
        count = 1

        for n in range(1, upper_bound):
            if N % n == 0:
                count += 1

        # if N % 3 == 0:
        #     results.append([N - 1, N, N + 1])
        # if N % 2 == 1:
        #     results.append([N // 2, N // 2 + 1])
        # if N % 5 == 0:
        #     d = N // 5
        #     results.append([d - 2, d - 1, d, d + 1, d + 2])

        # for r in results:
        #     if r[-1] == N:
        #         continue
        #     sub = self.cns(r[-1])
        #     if sub[-1][-1] + 1 == r[0]:
        #         results.append(sub[-1].extend(results[0][:-1]))

        return results

    def consecutiveNumbersSum(self, N: int) -> int:
        for n in range(1, N + 1):
            sum = n
            vals = [n]
            j = n + 1
            while sum <= N:
                if sum == N:
                    print(vals)
                vals.append(j)
                sum += j
                j += 1


Solution().consecutiveNumbersSum(15)
print(Solution().cns(15))
# print(Solution().cns(15))

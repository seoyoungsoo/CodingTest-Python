# 1748번 수 이어 쓰기 1

N = int(input())
nums = [int('9'+'0'*i) for i in range(0, len(str(N)))]
res = 0

for i, v in enumerate(nums):
    if v == nums[-1]:
        res += len(str(v)) * (N - sum(nums[:-1]))
    else:
        i += 1
        res += i * v
print(res)
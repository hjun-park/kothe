import sys

input = sys.stdin.readline

N = int(input().rstrip())
nums = list(map(int, input().split()))

nums.sort()

cnt = 0
for i in range(N):
    l, r = 0, N - 1

    while l < r:
        temp = nums[l] + nums[r]

        if temp == nums[i]:
            # 서로 다른 두 수까지 확인
            if l != i and r != i:
                cnt += 1
                break
            elif l == i:
                l += 1
            elif r == i:
                r -= 1
        elif temp > nums[i]:
            r -= 1
        elif temp < nums[i]:
            l += 1

print(cnt)

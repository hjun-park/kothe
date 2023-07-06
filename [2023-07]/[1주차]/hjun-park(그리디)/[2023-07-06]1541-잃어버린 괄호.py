import sys

input = sys.stdin.readline

formula = input().rstrip()

nums = formula.split('-')

total = sum(list(map(int, nums[0].split('+'))))
for n in nums[1:]:
    a = sum(list(map(int, n.split('+'))))
    total -= sum(list(map(int, n.split('+'))))

print(total)

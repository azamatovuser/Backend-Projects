nums = [int(i) for i in input().split()]
val = int(input())
list = []
for i in nums:
    if i == val:
        continue
    else:
        list.append(i)
print(len(list))
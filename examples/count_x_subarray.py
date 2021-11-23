from collections import Counter


n = int(input())
arr = [int(num) for num in input().split()]
cached = {}

for _ in range(int(input())):
    l, r, x = input().split()
    if (l, r) in cached:
        print(cached.get((l, r)).get(int(x), 0))
    else:
        cached[(l, r)] = Counter(arr[int(l):int(r)+1])
        print(cached.get((l, r)).get(int(x), 0))

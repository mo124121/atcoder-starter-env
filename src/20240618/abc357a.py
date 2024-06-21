N, M = map(int, input().split())
H = list(map(int, input().split()))

ans = 0
for h in H:
    if h > M:
        break
    M -= h
    ans += 1

print(ans)

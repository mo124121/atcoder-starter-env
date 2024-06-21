def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))

    ans = solve(N, M, H)

    print(ans)


def solve(N, M, H):
    ans = 0
    for h in H:
        if h > M:
            break
        M -= h
        ans += 1
    return ans


def test():
    assert 3 == solve(5, 10, [2, 3, 2, 5, 3])
    assert 4 == solve(5, 10, [2, 3, 2, 3, 5])
    assert 1 == solve(1, 5, [1])


test()
# main()

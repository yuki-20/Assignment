def ihavenoideawhatintheworldisthisvariabledef(s):
    chars = list(s)
    i = len(chars) - 1
    while i >= 0 and chars[i] == "c":
        chars[i] = "a"
        i -= 1
    if i < 0:
        return "a" * (len(s) + 1)
    if chars[i] == "a":
        chars[i] = "b"
    else:
        chars[i] = "c"
    return "".join(chars)


def ispentlike10minutestothinkaboutthisdefnamefr(s):
    if s == "a":
        return None
    if s == "a" * len(s):
        return "c" * (len(s) - 1)
    chars = list(s)
    i = len(chars) - 1
    while i >= 0 and chars[i] == "a":
        chars[i] = "c"
        i -= 1
    if chars[i] == "c":
        chars[i] = "b"
    else:
        chars[i] = "a"
    return "".join(chars)


def imissher(s):
    value = 0
    for ch in s:
        if ch == "a":
            digit = 0
        elif ch == "b":
            digit = 1
        else:
            digit = 2
        value = value * 3 + digit
    return 3 ** len(s) - 1 - value


def prefix_function(s):
    pi = [0] * len(s)
    i = 1
    while i < len(s):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
        i += 1
    return pi


def ilosther(n, s):
    m = len(s)
    if m == 0:
        return 3 ** n
    if m > n:
        return 0
    pi = prefix_function(s)
    trans = [[0] * 3 for _ in range(m)]
    alphabet = "abc"
    for state in range(m):
        for k in range(3):
            ch = alphabet[k]
            j = state
            while j > 0 and s[j] != ch:
                j = pi[j - 1]
            if s[j] == ch:
                j += 1
            trans[state][k] = j
    dp = [0] * m
    dp[0] = 1
    for _ in range(n):
        new_dp = [0] * m
        for state in range(m):
            if dp[state] == 0:
                continue
            for k in range(3):
                nxt = trans[state][k]
                if nxt < m:
                    new_dp[nxt] += dp[state]
        dp = new_dp
    return 3 ** n - sum(dp)


print("Problem 1")
print("Part 1")
part1_tests = ["aaa", "abc", "acc", "bccc", "ccc"]
for s in part1_tests:
    print("next(" + s + ") =", ihavenoideawhatintheworldisthisvariabledef(s))

print()
print("Part 2")
part2_tests = ["b", "ba", "aaaa", "abca", "caa"]
for s in part2_tests:
    ans = ispentlike10minutestothinkaboutthisdefnamefr(s)
    if ans is None:
        print("previous(" + s + ") = No previous string")
    else:
        print("previous(" + s + ") =", ans)

print()
print("Part 3")
part3_tests = ["a", "abc", "bca", "ccc"]
for s in part3_tests:
    print("count behind same length(" + s + ") =", imissher(s))

print()
print("Part 4")
part4_tests = [(2, "a"), (3, "ab"), (4, "ab"), (5, "abc")]
for n, s in part4_tests:
    print("count strings containing(" + str(n) + ", " + s + ") =", ilosther(n, s))

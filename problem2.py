A = [[1, 3], [2, -1]]
B = [[2, 1], [1, 4]]


def product(M, N):
    return [
        [M[0][0] * N[0][0] + M[0][1] * N[1][0], M[0][0] * N[0][1] + M[0][1] * N[1][1]],
        [M[1][0] * N[0][0] + M[1][1] * N[1][0], M[1][0] * N[0][1] + M[1][1] * N[1][1]],
    ]


def add(M, N):
    return [
        [M[0][0] + N[0][0], M[0][1] + N[0][1]],
        [M[1][0] + N[1][0], M[1][1] + N[1][1]],
    ]


def scale(M, k):
    return [
        [M[0][0] * k, M[0][1] * k],
        [M[1][0] * k, M[1][1] * k],
    ]


def pair_product(X, Y):
    P, Q = X
    R, S = Y
    left = add(product(P, R), scale(product(Q, S), 7))
    right = add(product(P, S), product(Q, R))
    return left, right


def compute_An_Bn(n):
    result = ([[1, 0], [0, 1]], [[0, 0], [0, 0]])
    base = (A, scale(B, -1))
    while n > 0:
        if n % 2 == 1:
            result = pair_product(result, base)
        base = pair_product(base, base)
        n //= 2
    return result


def print_matrix(M):
    print("[" + str(M[0][0]) + " " + str(M[0][1]) + "]")
    print("[" + str(M[1][0]) + " " + str(M[1][1]) + "]")


print("Problem 2")
print("Part 1")
product_tests = [
    ([[1, 2], [3, 4]], [[5, 6], [7, 8]]),
    ([[2, 0], [1, 3]], [[4, 1], [2, 5]]),
]
for index, pair in enumerate(product_tests, 1):
    M, N = pair
    print("Test", index)
    print("M =")
    print_matrix(M)
    print("N =")
    print_matrix(N)
    print("product(M, N) =")
    print_matrix(product(M, N))
    print()

print("Part 2")
n_tests = [0, 1, 2, 3, 4]
for n in n_tests:
    An, Bn = compute_An_Bn(n)
    print("n =", n)
    print("An =")
    print_matrix(An)
    print("Bn =")
    print_matrix(Bn)
    print()

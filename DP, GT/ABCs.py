def find_triplets(A, B, C):
    for x in range(1, int((A // 3) ** 0.5) + 1):
        for y in range(x + 1, int((A // 2) ** 0.5) + 1):
            z = A - x - y
            if x * y * z == B and x * x + y * y + z * z == C:
                return x, y, z
    return -1, -1, -1

ABC = find_triplets(int(input("A: ")), int(input("B: ")), int(input("C: ")))
print(f"A: {ABC[0]}")
print(f"B: {ABC[1]}")
print(f"C: {ABC[2]}")
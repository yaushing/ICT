#input  validation
def parse_int(inputgiven, msg):
    try:
        int(inputgiven)
        return int(inputgiven)
    except:
        return parse_int(input(msg), msg)
n = parse_int(input("Enter n: "), "Enter n: ")
#1 - 5 align left
print(f"Easy: 1 - {n} align left")
print()
for i in range(n):
    for _ in range(i + 1):
        print("*", end = "")
    print()

print()
#5 - 1 align left
print(f"Medium: {n} - 1 align left")
print()
for i in range(n, 0, -1):
    for _ in range(i):
        print("*", end = "")
    print()
print()
#5 - 1 align right 
print(f"Hard: {n} - 1 align right")
print()
for i in range(n, 0, -1):
    for _ in range(n - i):
        print(" ", end = "")
    for _ in range(i):
        print("*", end="") 
    print()
print()
#1 - 5 align right 
print(f"Hard: 1 - {n} align right")
print()
for i in range(n):
    for _ in range(n - i - 1):
        print(" ", end = "")
    for _ in range(i + 1):
        print("*", end="") 
    print()
print()
#hourglass
print("Bonus: Hourglass")
print()
order = []
for i in range(n, 0, -2):
    order.append([i, (n - i) // 2]) 
for i in range(len(order)):
    for _ in range(order[i][1]):
        print(" ", end = "")
    for _ in range(order[i][0]):
        print("*", end = "")
    for _ in range(order[i][1]):
        print(" ", end = "")
    print()
for i in range(len(order)):
    if i == 0:continue
    for _ in range(order[(i + 1) * -1][1]):
        print(" ", end = "")
    for _ in range(order[(i + 1) * -1][0]):
        print("*", end = "")
    for _ in range(order[(i + 1) * -1][1]):
        print(" ", end = "")
    print()
print()
#diamond
print("Bonus: Diamond")
print()
order = []
lowest_n = n
while lowest_n > 1:
    lowest_n -= 2
for i in range(lowest_n, n + 1, 2):
    order.append([i, (n - i) // 2]) 
for i in range(len(order)):
    for _ in range(order[i][1]):
        print(" ", end = "")
    for _ in range(order[i][0]):
        print("*", end = "")
    for _ in range(order[i][1]):
        print(" ", end = "")
    print()
for i in range(len(order)):
    if i == 0:continue
    for _ in range(order[(i + 1) * -1][1]):
        print(" ", end = "")
    for _ in range(order[(i + 1) * -1][0]):
        print("*", end = "")
    for _ in range(order[(i + 1) * -1][1]):
        print(" ", end = "")
    print()
print()
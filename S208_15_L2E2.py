def parse_int(input):
    try:
        int(input) 
        return True
    except:
        return False

F = input("Enter F: ")
while not parse_int(F): F = input("Enter F")
F = int(F)
V = input("Enter V: ")
while not parse_int(V): V = input("Enter F")
V = int(V)
E = input("Enter E: ")
while not parse_int(E): E = input("Enter F")
E = int(E)
FVE2 = ["F", "V", "E"]
FVE = [F, V, E]
for EVF in FVE:
    if EVF == 0:
        zero = FVE2[FVE.index(EVF)]
        print(zero, "equals", 2 + E - V) if zero == "F" else print(zero, "equals", F + V - 2) if zero == "E" else print(zero, "equals", 2 - F + E)
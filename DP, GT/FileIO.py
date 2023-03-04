data = []
def read_data(file_name):
    with open(file_name, "r") as file:
        data = [list(map(int, line.strip().split())) for line in file.readlines()]
    return data

def display_data(data, data2change):
    for row in data:
        print(*row)
        data2change.append(row)
    return data2change

def display_total(data2):
    total = 0
    for _ in range(3):
        data2[0].append(0)
    print(data2)
    for column in range(5):
        for row in data2:
            if len(row) > 0:
                total += row[column]
        print(f"Total of column {column + 1} {total}")

def find_max(data):
    max_val = -1e10
    max_row = -1
    max_col = -1
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if col > max_val:
                max_val = col
                max_row = i
                max_col = j
    return max_row, max_col

def display_max(data):
    max_row, max_col = find_max(data)
    print("Max value is {} at co-ord ({}, {})".format(data[max_row][max_col], max_row + 1, max_col + 1))

file_name = "data.txt"
data = read_data(file_name)
print("Data:")
data2 = []
data2 = display_data(data, data2)
print("Total:")
display_total(data2)
display_max(data)

from time import time
from itertools import product
def maximum_cash(traintime, max_time, book_cost, payback_rate):
    actions = ["TEACH", "TRAIN", "BUY"]
    listss = []
    dp = []
    for lenlist in range(int(max_time * 0.6), int(max_time * 0.7)):
        print("running", lenlist)
        for roll in product([0, 1, 2], repeat=lenlist - 1):
            knowledge = 0
            cash = 0
            lists = []
            time = 0
            books = 0
            perm = list(roll)
            perm.insert(0, 0)
            for action in (perm):
                lists.append(actions[action])
            if lists[0] == "BUY" or lists[0] == "TRAIN" or lists[1] == "TRAIN": # rule out any that bankrupts me as soon as launch
                break
            for action in lists:
                if action == "TEACH":
                    time += 2
                    cash += 10 + min(20, knowledge) * payback_rate
                elif action == "TRAIN":
                    time += max(1, (int)(8 / max(1, books * traintime)))
                    cash -= 20
                    knowledge += 1
                else:
                    if books == 4: 
                        books += 1
                        break
                    cash -= book_cost[books] if books < 4 else 1000
                    time += books
                    books += 1
                if time > max_time or cash < 0 or books > 4:
                    break
            if time > max_time or cash < 0 or books > 4:
                continue
            else:
                dp.append([cash, lists])
        print(lenlist)
    max_cash = 0
    for i in dp:
        cash = i[0]
        max_cash = max(max_cash, cash)
        if cash == max_cash:
            trueactionlist = i[1]
    return max_cash, trueactionlist
    

if __name__ == '__main__':
    max_time_units, learning_rate, payback_rate = map(int, input().split())
    book_cost = list(map(int, input().split()))
    start = time()
    print(maximum_cash(learning_rate, max_time_units, book_cost, payback_rate))
    print(f"Simulation Run Time: {time() - start} seconds")
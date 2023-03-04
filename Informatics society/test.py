def maximum_cash(max_time_units, learning_rate, payback_rate, book_cost):
    actionlist = []
    max_cash = 0
    cash = 0
    books = 0
    knowledge = 0
    time = 0
    trained = 0
    for t in range(max_time_units + 1):
        while time < max_time_units and (time + 2 <= max_time_units or books < 4):
            if books < 4 and time + books + 1 <= max_time_units and cash >= book_cost[books] and max(1, (int)(8 / max(1, books * learning_rate))) > 1:
                if cash >= book_cost[books]:
                    actionlist.append("BUY")
                    cash -= book_cost[books]
                    books += 1
                else:
                    print("buy not worth buying")
                    pass
            elif time + max(1, (int)(8 / max(1, books * learning_rate))) <= max_time_units and cash >= 20 and (t - max(1, (int)(8 / max(1, books * learning_rate)))) > 2 and trained < int(max_time_units // 10):
                actionlist.append("TRAIN")
                training_time = max(1, (int)(8 / max(1, books * learning_rate)))
                if cash >= 20:
                    cash -= 20
                    time += training_time
                    knowledge += 1
                    trained += 1
                else:
                    break
            break
        while time < t:
            if time + 2 <= t:
                actionlist.append("TEACH")
                time += 2
                cash += 10 + min(20, knowledge) * payback_rate
            else:
                break
        max_cash = cash
        
    return max_cash, actionlist

if __name__ == '__main__':
    max_time_units, learning_rate, payback_rate = map(int, input().split())
    book_cost = list(map(int, input().split()))
    print(maximum_cash(max_time_units, learning_rate, payback_rate, book_cost))


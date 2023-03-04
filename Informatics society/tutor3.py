def maximum_cash(max_time_units, learning_rate, payback_rate, book_cost):
    actionlist = []
    max_cash = [0] * (max_time_units + 1)
    books = 0
    knowledge = 0
    time = 0
    trained = 0
    
    for t in range(1, max_time_units + 1):
        cash = max_cash[t-1]
        while time < t:
            if books < 4 and time + books + 1 <= t and cash >= book_cost[books] and max(1, (int)(8 / max(1, books * learning_rate))) > 1:
                cash -= book_cost[books]
                books += 1
                actionlist.append("BUY")
            elif time + max(1, (int)(8 / max(1, books * learning_rate))) <= t and cash >= 20 and (t - max(1, (int)(8 / max(1, books * learning_rate)))) > 2 and trained < int(max_time_units // 8) and max(1, (int)(8 / max(1, books * learning_rate))) == 1:
                training_time = max(1, (int)(8 / max(1, books * learning_rate)))
                cash -= 20
                time += training_time
                knowledge += 1
                trained += 1
                actionlist.append("TRAIN")
            elif time + 2 <= t:
                time += 2
                cash += 10 + min(20, knowledge) * payback_rate
                actionlist.append("TEACH")
            else:
                break
        max_cash[t] = cash
    
    return max_cash[max_time_units], actionlist, trained, knowledge

if __name__ == '__main__':
    max_time_units, learning_rate, payback_rate = map(int, input().split())
    book_cost = list(map(int, input().split()))
    print(maximum_cash(max_time_units, learning_rate, payback_rate, book_cost))
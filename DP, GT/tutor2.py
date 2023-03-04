from time import time
def maximum_cash(max_time_units, learning_rate, payback_rate, book_cost):
    max_cash = 0
    trueactiondict = {}
    for trainamt in range(max_time_units):
        actionlist = []
        actiondict = {}
        cash = 0
        books = 0
        knowledge = 0
        time = 0
        trained = 0
        amtperteach = 0
        for t in range(max_time_units + 1):
            while time < max_time_units and (time + 2 <= max_time_units or books < 4):
                if books < 4 and time + books + 1 <= max_time_units and cash >= book_cost[books] and max(1, (int)(8 / max(1, books * learning_rate))) > 1:
                    actionlist.append("BUY")
                    cash -= book_cost[books]
                    time += books
                    books += 1
                elif time + max(1, (int)(8 / max(1, books * learning_rate))) <= max_time_units and cash >= 20 and trained < int(trainamt) and (max(1, (int)(8 / max(1, books * learning_rate))) == 1 or books == 4):
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
                    amtperteach = 10 + min(20, knowledge) * payback_rate
                else:
                    break
            
            # Debugging information
            '''
            print("Time:", t)
            print("Cash:", cash)
            print("Books:", books)
            print("Knowledge:", knowledge)
            print("Max Cash:", str(max_cash))
            print("----------------")
            '''
        max_cash = max(max_cash, cash)    
        print(max_cash, cash, amtperteach, trainamt)
        for action in actionlist:
            if action in actiondict:
                actiondict[action] += 1
            else:
                actiondict[action] = 1
        if max_cash == cash:
            trueactiondict = actiondict
            trueactionlist = actionlist
    return max_cash, trueactiondict, trueactionlist

if __name__ == '__main__':
    max_time_units, learning_rate, payback_rate = map(int, input().split())
    book_cost = list(map(int, input().split()))
    start = time()
    print(maximum_cash(max_time_units, learning_rate, payback_rate, book_cost))
    print(time() - start)
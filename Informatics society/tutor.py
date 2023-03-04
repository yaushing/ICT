def TEACH(knowledge, paybackRate, timeleft):
    if timeleft > 2: return 0
    income = 10 + min(20, knowledge) * paybackRate
    return income, -2

def TRAIN(knowledge, books, learningRate, timeleft):
    trainingTime = max(1, (int)(8 / max(1, books * learningRate)))
    if timeleft < trainingTime: return 0
    return knowledge + 1, trainingTime * -1

def BUY(currentnobooks, timeleft):
    if timeleft <= currentnobooks: return 0
    return currentnobooks + 1, currentnobooks * -1

print(TRAIN(0, 1, 20, 15))
    
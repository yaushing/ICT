from time import time
def DP_table(tu, lr, pbr, bk):
    arr = [[[-1 for _ in range(5)] for _ in range(21)] for _ in range(tu + 1)]
    '''
    Split into lines
    b_arr = [-1, -1, -1, -1, -1]
    kb_arr = []
    for _ in range(21):
        kb_arr.append(b_arr)
    tkb_arr = []
    for _ in range(tu + 1):
        tkb_arr.append(kb_arr)
    '''
    arr[0][0][0] = 0
    maxValue = 0
    for i in range(tu + 1):
        for k in range(21):
            for b in range(5):
                #buy
                tt = max(1, (int)(8 / max(1, b * lr)))
                if tt > 1 and b < 4 and arr[i][k][b] >= bk[b] and i+b <= tu:
                    arr[i+b][k][b+1] = max(arr[i+b][k][b+1], arr[i][k][b]-bk[b])
                #train
                tt = max(1, (int)(8 / max(1, b * lr)))
                if k < 20 and arr[i][k][b] >= 20 and i + tt <= tu:
                    arr[i+tt][k+1][b] = max(arr[i + tt][k+1][b], arr[i][k][b] - 20)
                #teach
                if i + 2 <= tu and arr[i][k][b] >= 0:
                    arr[i+2][k][b] = max(arr[i+2][k][b], arr[i][k][b] + 10 + min(20, k) * pbr)
                    if maxValue < arr[i + 2][k][b]:
                        maxValue = arr[i + 2][k][b]
    return maxValue
if __name__ == '__main__':
    max_time_units, learning_rate, payback_rate = map(int, input().split())
    book_cost = list(map(int, input().split()))
    start = time()
    print(DP_table(max_time_units, learning_rate, payback_rate, book_cost))
    print(f"Simulation Run Time: {time() - start} seconds")

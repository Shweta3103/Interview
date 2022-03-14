   comb = 0
available = []
def candy_combination(count, idx):
    global comb

    if count == 0 and len(available) != 0:
        comb += 1
        return

    if idx >= len(available) or count < 0:
        return
    candy_combination(count - available[idx], idx+1)
    candy_combination(count, idx+1)

def candy_problem(n=None):
    temp = 1
    while temp <= n:
        available.append(temp)
        temp += 2
    print(available)
    candy_combination(n, 0)
    print(comb)


candy_problem(8)

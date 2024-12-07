def evaluate(test_val, vals, idx, res) -> bool:
    if idx+1 > len(vals):
        return res == test_val
    if res > test_val: # early return
        return False
    c1 = evaluate(test_val, vals, idx+1, res + vals[idx])
    c2 = evaluate(test_val, vals, idx+1, res * vals[idx])
    c3 = evaluate(test_val, vals, idx+1, int(str(res) + str(vals[idx])))
    return c1 or c2 or c3

def day6_part1():
    with open('./input.txt', 'r') as fd:
        data = fd.readlines()
        ddata = {}
        ret = 0
        for line in data:
            test_val = int(line.split(':')[0])
            vals = list(map(lambda x: int(x), line.split(':')[-1].strip().split(' ')))
            print(test_val, vals)
            if evaluate(test_val, vals, 0, 0) == True:
                ret += test_val
        print(ret)
        
day6_part1()

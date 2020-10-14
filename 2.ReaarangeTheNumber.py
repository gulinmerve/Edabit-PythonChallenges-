#https://edabit.com/challenge/jwzAdBnJnBxCe4AXP

def rearranged_difference(num):
    num = str(num)
    a ="".join(sorted(num,reverse = True))
    b = "".join(sorted([i for i in num if i != '0' ]))
    return int(a) - int(b)

def rearranged_difference(x):
    max = int("".join(sorted(str(x), reverse = True)))
    min = int("".join(sorted(str(x))))
    return max - min

def rearranged_difference(nmbr):
    return int("".join(sorted([i for i in str(nmbr)], reverse=True))) - int("".join(sorted([i for i in str(nmbr)])))


def rearranged_difference(num):
    max_num = int("".join(sorted(str(num), reverse =True)))
    min_num = int("".join(sorted(str(num))))
    return (max_num - min_num)

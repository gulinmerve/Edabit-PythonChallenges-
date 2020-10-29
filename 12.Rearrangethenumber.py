#https://edabit.com/challenge/jwzAdBnJnBxCe4AXP

def rearranged_difference(num):
    num = str(num)
    a ="".join(sorted(num,reverse = True))
    b = "".join(sorted([i for i in num if i != '0' ]))
    return int(a) - int(b)

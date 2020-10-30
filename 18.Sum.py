def accumulating_list(lst):
    return [lst[i]+sum(lst[:i]) for i in range(len(lst))]
accumulating_list([1, 0, 1, 0, 1])


####https://edabit.com/challenge/6CGomPbu3dK536PH2
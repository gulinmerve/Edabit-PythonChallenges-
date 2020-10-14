##https://edabit.com/challenge/mHLAmj4vmRuXrT8Nb

def consecutive_combo(lst1, lst2):
    l = lst1+lst2
    if sorted(l) == list(range(min(l),max(l)+1)):
        return True
    else:
        return False


def concecutive(lst1,lst2):
    a = sorted(lst1+lst2)
    b = [abs(a[i-1] -a[i]) for i in range(1,len(a)) ]
    c = (True if set(b)=={1} else False )
    return(c)


def consecutive_combo(a, b) :
    a.extend(b)
    a.sort()
    message = True
    for i in range(1,len(a)):
        if a[i] - a[i-1] != 1 :
            message = False
            break 
    if message :
        return mesage
    else:
        return message

#
def consecutive_combo(lst1, lst2):
    lst = lst1 + lst2
    return max(lst) - min(lst) == len(lst) - 1

#
def consecutive_combo(lst_1, lst_2):
    lst = sorted(lst_1 + lst_2)
    if (((lst[-1]*(lst[-1]+1))/2) - (((lst[0]-1)*lst[0])/2)) == sum(lst):
        return True
    else:
        return False
#

def consecutive_combo(lst1, lst2):
    return True if sorted(lst1+lst2)==[*range(min(lst1+lst2),max(lst1+lst2)+1)] else False   

#
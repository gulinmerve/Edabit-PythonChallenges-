#https://edabit.com/challenge/JzBLDzrcGCzDjkk5n

def encrypt(word):
    return word[::-1].replace("a", "0").replace("e", "1").replace("o", "2").replace("u", "3")+"aca"


##
def encrypt(word):
    dict={"a":0,"e":1 ,"i":2, "o":2, "u":2}
    print(*[dict[x] if x in dict else x for x in word[::-1]],end="aca",sep="")

##
def encrypt(word):
	x={"a":0,"e":1,"i":2,"o":2,"u":3}
	for i in word:
		if i in x:
			word=word.replace(i,str(x[i]))
	return word[::-1]+"aca" #acik halini de yazayim dedim

##
def encrypt(word):
    x={"a":0,"e":1,"i":2,"o":2,"u":3}
    return "".join(str(x[i]) if i in x else i for i in word[::-1]) +'aca'

##
def encrypt(word):
	B = word[::-1]
	C=B.maketrans({ord('a'): ord('0'),ord('e'): ord('1'),ord('o'): ord('2'),ord('u'):ord('3')})
	return B.translate(C)+'aca'
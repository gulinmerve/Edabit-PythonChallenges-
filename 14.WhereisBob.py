#https://edabit.com/challenge/fDkAuAwR4PMWZwBKs

def find_bob(names):
		return names.index('Bob') if 'Bob' in names else -1

###
def find_bob(names):
    if "Bob" in names: return names.index("Bob")
    else: return -1
    ###

    
#https://edabit.com/challenge/S7rdJsn6vkfC9BzcR
class Employee:
    def __init__(self,fname,**kwargs):
        self.fname=fname
        for key,value in kwargs.items():
            setattr(self,key,value)
        self.name,self.lastname=self.fname.split()
john = Employee('John Doe')
mary = Employee('Mary Major', salary=120000)
richard = Employee('Richard Roe', salary=110000, height=178)
giancarlo = Employee('Giancarlo Rossi', salary=115000, height=182, nationality='Italian')
peng = Employee('Peng Zhu', salary=500000, height=185, nationality='Chinese', subordinates=[i.lastname for i in (john, mary, richard, giancarlo)])
print(giancarlo.nationality)
print(richard.height)
print(peng.subordinates)

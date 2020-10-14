#https://edabit.com/challenge/7FyTyi68Df2CxLx6C
class Pizza :
    count = 0
    def __init__(self,ingredients):
        self.ingredients = ingredients
        Pizza.count += 1
        self.order_number = Pizza.count
    @classmethod   
    def hawaiian (cls):
        return cls(["ham", "pineapple"])
      
    @classmethod 
    def meat_festival (cls):
        return cls(["beef", "meatball","bacon"])
       
    @classmethod 
    def garden_feast (cls):
        return cls(["spinach", "olives", "mushroom"])
p1 = Pizza(["bacon", "parmesan", "ham"])
p2 = Pizza.garden_feast()
p3 = Pizza.hawaiian()
p4 = Pizza.meat_festival()
p5 = Pizza(["pepperoni", "bacon"])
my_pizza = Pizza(["cheese", "caviar", "oyster", "uranium"])
print(p1.ingredients)
print(p2.ingredients)
print(p1.order_number)

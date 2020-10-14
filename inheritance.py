#https://edabit.com/challenge/5T978H873HFZ7xKd8
class BasicPlan:
	can_stream = True
	can_download = True
	num_of_devices = 1
	has_SD = True
	has_HD = False
	has_UHD = False
	price = '$8.99'
	
# Write the classes for StandardPlan and PremiumPlan here!
class StandardPlan(BasicPlan):
    has_HD = True
    num_of_devices = 2
    price = '$12.99'
class PremiumPlan(StandardPlan):
    has_UHD = True
    num_of_devices = 4
    price = '$15.99'
print(BasicPlan.can_stream)
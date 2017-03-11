class Mpesa:
	def __init__(self):
		self.name = input("Please Enter Your Name:")
		self.phone_number = input("Please Enter Your phone number: ")
		self.balance = 0
		print ("Dear {} welcome to Mpesa".format(self.name))
		print ("Start by depositing some money into Your Account! ")

	def deposit_cash(self, amount):
		self.balance += amount
		print ("Your current amount is {}".format(self.balance))

	def show_balance(self)
		print ("Dear, {} Your Current Mpesa balance is {} :".format(self.name, self.balance))













import logging
import OS

logging.basicConfig(filename='test.py', level=logging.INFO,)


class User:

	def __init__ (self, name, address, phone):
		self.name = input("what is your name: ")
		self.address= input("what is your address: ")
		self.phone= input("what is your phone number: ")


		return(self.name,self.address,self.phone)
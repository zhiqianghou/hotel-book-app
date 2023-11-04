import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})

# Instance variable coded inside a method
# Class variable coded outside a method


"""
I will show ABC which is abstracted base class and how to use it. 
Basically, the ABC is used to force the programmer to use the same structure of the class
I put the import module here not at beginning just for the clarification of how to use it
"""
from abc import ABC, abstractmethod

class Ticket(ABC):
	@abstractmethod
	def generate(self): # DigitalTicket and ReservationTicket both have generate method but different output
		pass

class DigitalTicket(Ticket):
	def generate(self):
		print("Hello, this is an abstract base class inherited from Ticket and must have a generate method")


class ReservationTicket(Ticket):
	def __init__(self, customer_name, hotel_object):
		self.customer_name = customer_name
		self.hotel = hotel_object

	def generate(self):
		content = f"""
		Thank you for your reservation
		Here are your booking data:
		name: {self.the_customer_name}
		hotel: {self.hotel.name}
		
		"""
		return content

	"""
	   What is a property?
	   Below is an example to show property especially when you need some processing.
	"""
	@property
	def the_customer_name(self):
		name = self.customer_name.strip()
		name = name.title()
		return name


	@staticmethod
	def covert(number):
		return number * 1.2







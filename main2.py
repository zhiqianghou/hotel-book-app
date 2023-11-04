import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})

# Instance variable coded inside a method
# Class variable coded outside a method

class Hotel:
	watermark = "WenwenMeidai USA Real Estate Company"
	def __init__(self, hotel_id):
		self.hotel_id = hotel_id
		self.name = df.loc[df["id"]==self.hotel_id, "name"].squeeze()

	def book(self):
		"""Book a hotel by changing its availability to no"""
		df.loc[df["id"]==self.hotel_id, "available"] = "no"
		df.to_csv("hotels.csv", index=False)

	def available(self):
		"""Check if the hotel is available"""
		availability = df.loc[df["id"]==self.hotel_id, "available"].squeeze()
		if availability == "yes":
			return True
		else:
			return False


	"""
	   What is a class method?
	   Below is an example to show difference to the instance method
	"""
	@classmethod
	def get_hotel_count(cls,data):
		return len(data)


class ReservationTicket:
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



hotel1 = Hotel(hotel_id="188")
hotel2 = Hotel(hotel_id="134")

print(hotel1.available())
print(hotel2.name)

print(hotel1.watermark)
print(hotel2.watermark)

print(Hotel.watermark)

#Test the class method
print(f"The total number of the hotel in our database is {Hotel.get_hotel_count(data=df)}")

# Test the property
ticket = ReservationTicket(customer_name="john smith ", hotel_object=hotel1)
print(ticket.the_customer_name)
print(ticket.generate())




#9-2. Three Restaurants: Start with your class from Exercise 9-1. 
#Create three different instances from the class, and call describe_restaurant() for eachinstance

class Restaurant:
 
 # A class to model a restaurant
 def __init__(self, restaurant_name, cuisine_type):
  self.rest_name = restaurant_name
  self.cuisine= cuisine_type

 def describe_restaurant(self):
  print(f" Hello ! welcome to {self.rest_name} Restaurant")
  print(f"{self.rest_name} is here to serve the best {self.cuisine} food you have ever tasted")
    

 def open_restaurant(self):
  print(f"{self.rest_name} us now open")

her_restaurant = Restaurant("laziz", "Arabian")
restaurant = Restaurant('Rahmas Kitchen', "Traditional")
Their_restaurant = Restaurant('Vicenzo', "Italian")
restaurant.describe_restaurant()
her_restaurant.describe_restaurant()
Their_restaurant.describe_restaurant()










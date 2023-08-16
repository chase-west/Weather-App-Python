import requests

#Get user input for city
city = input("Enter a city: ")

#Read from text file api_key.txt
file = open("api_key.txt", "r")
api_key = file.read() 

#Create response variable
response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")

#Exception handling incase of issue
try: 
  #Assign data to values generated from api call
  data = response.json()

  temp = data['main']['temp']

  #Change temperature to fahrenheit 
  temp = (temp - 273.15) * 9/5 + 32
  desc = data['weather'][0]['description']
  wind = data['wind']['speed']


  print(f"\nThe weather for {city} is...")
  print(f'Temperature: {round(temp, 1)} degrees fahrenheit')
  print(f'Description: {desc}')
  print(f"Wind Speed: {wind} MPH")

except:
  print("Error occurred, please try again")


# import requests 

# response = requests.get(url="https://world.openfoodfacts.org/api/v0/product/737628064502.json")
# print(response)

# # response.raise_for_status()
# data = response.json()
# print(data["product"])
# print("--"*10)
# # sunrise = data["results"]["sunrise"]
# # print(sunrise)
# # print(data["status"])
# # lat = data["iss_position"]["latitude"]
# # iss_position = (long, lat)
# # print(iss_position)
# NASA
import requests

api_key = "3ZEUiddbVoOGsOEPiYvf1olLUww72x5l0KrYRa8Z"

url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
response = requests.get(url)
data = response.json()
print(data)



import requests

url = "https://yummly2.p.rapidapi.com/feeds/search"

ingredients = input("What ingredients do you want to use up? ")
diet = input("Do you have any dietary restrictions? If so, please type it in! Examples include vegetarian, vegan, lacto... etc ")
if diet == "No":
    diet1 = ""
else:
    diet1 = diet
# querystring = {"q":ingredients}
querystring = {"start":"0","maxResult":"18","maxTotalTimeInSeconds":"7200",
               "q":ingredients, "allowedAttribute": diet1, "FAT_KCALMax":"1000"}
# "diet-lacto-vegetarian,diet-low-fodmap","FAT_KCALMax":"1000"
headers = {
	"X-RapidAPI-Key": "b913050d98mshda76f7dc59f7480p18af0djsna972adde7447",
	"X-RapidAPI-Host": "yummly2.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.content)
print(response.headers)
print(response.text)

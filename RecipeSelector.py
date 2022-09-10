import requests






url = "https://yummly2.p.rapidapi.com/feeds/auto-complete"

querystring = {"q":"chicken soup"}

headers = {
	"X-RapidAPI-Key": "b913050d98mshda76f7dc59f7480p18af0djsna972adde7447",
	"X-RapidAPI-Host": "yummly2.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
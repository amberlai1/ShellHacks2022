import requests
import pandas
import numpy

food = input("What do you want to eat? ")

length = input("How many minutes do you want to spend cooking? ")
length_int = int(length)
length_int *= 60
length_string = str(length_int)

yummly_url = "https://yummly2.p.rapidapi.com/feeds/search"

querystring = {"start":"0","maxResult":"18","maxTotalTimeInSeconds":length_string,"q":food}

headers = {
	"X-RapidAPI-Key": "b913050d98mshda76f7dc59f7480p18af0djsna972adde7447",
	"X-RapidAPI-Host": "yummly2.p.rapidapi.com"
}

response = requests.request("GET", yummly_url, headers=headers, params=querystring)

json_response = response.json()

df = pandas.DataFrame.from_dict(response.json()['seo'])

matrix = df.to_numpy()

print(matrix[4][0][0]['href'])
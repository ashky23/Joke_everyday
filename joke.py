# -----------------------------------------------------------++
# This is a script to get a joke from site dadjoke with your ||
# desired topic.I've used requests module for retrieving the ||
# data from the site					    ||
# -----------------------------------------------------------++

import requests
import termcolor
import pyfiglet
import random
color_choice = random.choice(
    ["red", "green", "yellow", "blue", "magenta", "cyan", "white"])
text1 = "Dad Joke 3000"
text2 = pyfiglet.figlet_format(text1)
text3 = termcolor.colored(text2, color=color_choice)
print(text3)

url = "https://icanhazdadjoke.com/search"
user_joke = input(
    "Let me tell you a joke! Give me a topic and enjoy a little laugh ^.^  ")
try:
    response = requests.get(
        url,
        headers={
            "Accept": "application/json"},
        params={
            "term": user_joke})
except BaseException:
    print("You're having an error while retrieving data from the aforementioned site")
# print(response.json())
res = response.json()
res_parse = res["results"]
print("------------------------------")
no_of_jokes = len(res_parse)
x = random.randint(0, no_of_jokes)
print(x)
if no_of_jokes > 1:
    print(
        "I've %d jokes for your %s topic: Let me tell you one" %
        (no_of_jokes, user_joke))
    #print("I've {} for your {} topic: Let me tell you one".format(no_of_jokes,user_joke))

    p = res_parse[x]
    print(p["joke"])

elif no_of_jokes == 1:
    print("I've only one joke: Here it is")
else:
    print("I don\'t have any joke for this topic")

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import csv
import os

url = 'https://www.foreca.fi/Finland/Ylivieska/10vrk'

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
uClient = urlopen(req)
page_html = uClient.read()
uClient.close()


page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class":"day"})

filename = "/home/mazku/testi/files/WeatherYlivieska.csv"
f = open(filename, "w")

headers = "Päivämäärä, Sää, Ylin, Alin, Tuuli\n"
f.write(headers)


for container in containers:

    Day_container = container.findAll("h5")
    Day = Day_container[0].text

    weather = container.a["title"]
    try:
        Max_container = container.findAll("span", {"class":"warm"})
        Max = Max_container[0].text
    except IndexError:
        Max_container = container.findAll("span", {"class":"warm"})
        Max = Max_container[0].text
    try:
        Min_container = container.findAll("span", {"class":"cold"})
        Min = Min_container[0].text
    except IndexError:
        Min_container = container.findAll("span", {"class":"warm"})
        Min = Min_container[0].text

    Wind_container = container.findAll("div", {"class":"ws"})
    Wind_speed = Wind_container[0].text

    print("Päivämäärä: " + Day + "\n")
    print("Sää: " + weather + "\n")
    print("Ylin: " + Max + "\n")
    print("Alin: " + Min + "\n")
    print("Tuuli: " + Wind_speed + "\n")

    f.write(Day + "," + weather + "," + Max + "," + Min + "," + Wind_speed + "\n")


f.close()


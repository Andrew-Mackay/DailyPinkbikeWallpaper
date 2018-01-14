#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import re
import os
import ctypes


r = requests.get("https://www.pinkbike.com/")
data = r.text
soup = BeautifulSoup(data, "lxml")

# retrieve link for PoD
podLink = soup.find_all('a', attrs={'href': re.compile("^(https:\/\/www.pinkbike.com\/photo\/[0-9]*\/$)")})[0].get('href')
# extract number for pod
photoNum = re.compile("([0-9]+)").findall(podLink)[0]

#pinkbike high res download url = lp1.pinkbike.org/p0pb(image #)/(image #).jpg
urlStart = "https://lp1.pinkbike.org/p0pb"
urlEnd = ".jpg"
downloadURL = urlStart + photoNum + '/' + photoNum + urlEnd

r2 = requests.get(downloadURL)

dir_path = os.path.dirname(os.path.realpath(__file__))

file_location = dir_path + '\\' + 'PinkbikeBackground.jpg'

# Save image to file named "PinkbikeBackground.jpg"
open(file_location, 'wb').write(r2.content)

# Set background
ctypes.windll.user32.SystemParametersInfoW(20, 0, file_location, 3)

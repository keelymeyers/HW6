import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

url = "http://py4e-data.dr-chuck.net/known_by_Ka.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup()
for tag in tags:
	
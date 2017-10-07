import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

url = "http://py4e-data.dr-chuck.net/known_by_Ka.html"

count = 7
h_list = []
while count != 0:
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	url = tags[17].get('href', None)
	h_list.append(url)
	html = urllib.request.urlopen(url).read()
	count = count - 1
print (h_list[-1])


	




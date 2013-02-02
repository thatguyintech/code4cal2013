#! /usr/bin/env python3

from bs4 import BeautifulSoup
import requests

r = requests.get("http://students.berkeley.edu/osl/studentgroups/public/index.asp?todo=listgroups")
soup = BeautifulSoup(r.text, 'lxml')
print(soup.prettify())

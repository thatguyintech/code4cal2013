#! /usr/bin/env python

import requests

r = requests.get("http://students.berkeley.edu/osl/studentgroups/public/index.asp?todo=listgroups")
page = r.text

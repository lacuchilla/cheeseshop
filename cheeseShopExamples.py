# I planned on making this a "read from a file" example. 
# But it makes even more sense as a web example.
# http://lacuchilla.github.io/cheeseshop/ points to the project "GitPage" 
# I have placed some cheese data there.

# About the data: 
# Only has orders. I will cover more things after "Intro to Databases" on Tuesday
# Don't worry about Costs or Units. We will had that in later.

# Area for Implementation Questions (as we think of them)
# Do we want to support lots of different units (lb, kg, parcel counts) or convert 
# everything to one unit set?

# Python is huge on modules. Almost everything is in a module and almost everything has
# several modules to do the same thing. Urllib2 is an official way to open URLs.
import urllib2

print "Opening Cheese Orders"

# The response is related to the success/failure of the attempt to open the file
response = urllib2.urlopen('http://lacuchilla.github.io/cheeseshop/')

#Feel free to look at the kind of data that web pages return, it might be helpful later
#print response.info()

#Access the actual data
html = response.read()

# --------------------- The fun section -------------------------
# Some cool ways of handling text files:

# 1. As csv (this one is an old favorite of mine. 
# Note that almost all spreadsheets can be saved as a csv file):
import csv #For csv processing
import re  #For regular expressions - the learning curve on those is like a wall.

#print html
html = re.sub( '</br>','',html)
html = html.splitlines()
print html
csvReader = csv.reader(html)
for row in csvReader:
	print row[0] # Just the shop names



#Function examples
# TBD

#Good practice to close open http connections.
response.close()
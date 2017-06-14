#!/usr/bin/python
#
# Scrapelinks.py - scrape the webpage for date and links and make a CSV file from them
#

#Load some libs to help starting with requests to get the URL
import requests
#Load lxml to do the legwork sorting through the HTML. An alternative is BeautifulSoup but many sites recommend that you use lxml as the parser in BS so...
from lxml import html
#The commands to make a CSV file.
import csv

#We'll start by grabbing the page 
page = requests.get('http://www.whittinghamparishcouncil.org.uk/agenda-minutes.php')

# Then we take what we got from the page and turn that into HTML 
html_content = html.fromstring(page.content)

# Then, and here's the bit that looks tricky, we look for the the links to the minutes and scrape out the data we need

#First we scrape out the date. This is the link text so we look for the text in any link with the class pdf.
#We do this using xpath - a way of mapping where the bit we want is with respect to another element or the start of the page
#In this instance we say start looking at a div with the id=accordion and then work down.

minDate = html_content.xpath('//div[@id="accordion"]/div/a[@class="pdf"]/text()')

#We do the same thing, but this time we want the URL of the minutes and that's in the href attribute of the link. 
minLinks = html_content.xpath('//div[@id="accordion"]/div/a[@class="pdf"]/@href')

print(minDate,minLinks)

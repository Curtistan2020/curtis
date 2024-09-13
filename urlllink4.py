import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup  # Correct import for BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Get the URL from the user
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()  # Use urlopen from urllib.request

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

#Initialize the counters
counts = 0
sum = 0

# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    counts = counts+1
    number=int((tag.text))
    sum = sum+number
print(f'counts: {counts}')
print(f'Sum: {sum}')
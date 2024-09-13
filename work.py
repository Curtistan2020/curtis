import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Get the initial URL, count, and position from the user
url = input('Enter URL: ')
count = int(input('Enter count: '))  # How many times to repeat the process
position = int(input('Enter position: '))  # Position of the link to follow (1-based)

# Repeat the process for the specified number of times
for i in range(count):
    print('Retrieving:', url)
    
    # Open the URL and read the HTML
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Retrieve all anchor tags
    tags = soup('a')
    
    # Find the tag at the specified position (position is 1-based)
    # So we access position-1 in the list (since Python lists are 0-based)
    url = tags[position - 1].get('href', None)

# Print the last URL retrieved
print('Last URL:', url)

# Open the final URL and print the last name (which is in the URL itself)
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
print('Last name in sequence:', soup.title.string.split()[2])  # Extract the name from the title

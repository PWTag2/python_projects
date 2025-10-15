from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
sum = 0
for tag in tags:
    #Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    contents = ('Contents:', tag.contents[0])
    for line in contents:
        numbers = re.findall('\d+', line)
        if len(numbers) > 0:
            sum += int(numbers[0])
            print('Attrs:', tag.attrs)
print(sum)

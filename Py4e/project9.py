import json
import urllib.request

url = input('Enter location: ')
if len(url) < 1 :
    url = 'http://py4e-data.dr-chuck.net/comments_2208157.json'
print('Retrieving', url)

uh = urllib.request.urlopen(url)
data = uh.read()
info = json.loads(data)

sums = list()
for comment in info["comments"]:
    print('Id', sums.append(comment["count"]))
    print('Name', comment["name"])

print(sum(sums))

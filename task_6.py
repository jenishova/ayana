#1
import json
dict = {
"list": [
{
"login": "kom___0",
"email": "ayanasdfghj@gmail.com",
"age": 17,
"phone_number": 779779779
}
]
}
out_file = open('file.json', 'w')
json.dump(dict, out_file, indent = 6)
out_file.close()
print(dict)




#2

import requests
resp = requests.get('https://api.github.com/events')
p = [{"actor": 'kairat sexy'}]
print(resp)
print(resp.json())



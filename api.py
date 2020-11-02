import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0',
    'Referer': 'https://psycatgames.com/app/truth-or-dare/'
}

data = {}
data["id"] = "truth-or-dare"
data["language"] = "en"
data["category"] = "hot"
data["type"] = "dare"

response = requests.post('https://psycatgames.com/api/tod-v2/', headers=headers, data=json.dumps(data))

s = response.json()

out1 = (s['results'][0])
out2 = (s['results'][1])
out3 = (s['results'][2])
out4 = (s['results'][3])
out5 = (s['results'][4])
out6 = (s['results'][5])
out7 = (s['results'][6])
out8 = (s['results'][7])
out9 = (s['results'][8])
out10 = (s['results'][9])

print(out1)
print(out2)
print(out3)
print(out4)
print(out5)
print(out6)
print(out7)
print(out8)
print(out9)
print(out10)

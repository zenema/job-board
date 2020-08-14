import requests, json 

r = requests.get("https://jobs.github.com/positions.json?utf8=%E2%9C%93&description=software&location=")
# print(r.status_code)
r.json()

with open('scraped-jobs.json', 'w') as f:
    json.dump(r.json(), f)
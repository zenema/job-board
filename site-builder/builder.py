from jinja2 import Template
import json




with open("scraped-jobs.json", "r") as f:
    data = json.load(f)
    f.close()
    # print(data)

with open('template.html') as file_:
    template = Template(file_.read())
template.render(jobs=data)
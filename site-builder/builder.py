from jinja2 import Template
import json
import pprint
from datetime import datetime as dt

def date_formatter(entry):
            input = entry['created_at'] # "Wed Aug 05 04:21:47 UTC 2020"
            today = dt.today()
            difference = str(today - dt.strptime(input, '%a %b %d %H:%M:%S %Z %Y'))
            if("day" in difference):
                entry['created_at'] =  difference.split(',')[0] + " ago"
            else:
                entry['created_at'] = "today"

def formatter(data):
    for entry in data:
        date_formatter(entry)

# Get template
with open('template.j2') as file_:
    template = Template(file_.read())

# Stream jobs into script
with open("scraped-jobs.json", "r", encoding="utf8") as f:
    data = json.load(f)
    formatter(data)
    f.close()
    # print(data)
    # pprint.pprint(data, indent=2)


# Write generated html
with open('../public/index.html', 'w', encoding="utf-8") as output_file:
    output_file.write(template.render(jobs=data))
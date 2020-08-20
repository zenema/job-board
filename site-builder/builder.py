from jinja2 import Template
import json
import pprint
import datetime

def date_formatter(entry):
            input = entry['created_at'] # "Wed Aug 05 04:21:47 UTC 2020"
            output = datetime.datetime.strptime(input, '%a %b %d %H:%M:%S %Z %Y')
            # print(output)
            today = datetime.datetime.today()
            difference = today - output
            # print(today)
            entry['created_at'] = difference

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


# for job in data:
#     print("ID:", job["id"])
#     print("Type:", job["type"])
#     print("URL:", job["url"])
#     print("Posted:", job["created_at"])
#     print("Company:", job["company"])
#     print("Company URL:", job["company_url"])
#     print("Location:", job["location"])
#     print("Job Title:", job["title"])
#     print("Job Description:", job["description"])
#     # print("How To Apply:", job["how_to_apply"])
#     # print("Company Logo:", job["company_logo"])
#     print()
#     print("----------------------------------------------------------------------")
#     print("----------------------------------------------------------------------")
#     print()
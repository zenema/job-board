from jinja2 import Template
import json

# Get template
# with open('template.html') as file_:
#     template = Template(file_.read())

# Stream jobs into script
with open("scraped-jobs.json", "r") as f:
    data = json.load(f)
    f.close()
    # print(data)

# Write generated html
# with open('public/index.html', 'w') as output_file:
#     output_file.write(template.render(jobs=data))

for job in data:
    print("ID:", job["id"])
    print("Type:", job["type"])
    print("URL:", job["url"])
    print("Posted:", job["created_at"])
    print("Company:", job["company"])
    print("Company URL:", job["company_url"])
    print("Location:", job["location"])
    print("Job Title:", job["title"])
    print("Job Description:", job["description"])
    # print("How To Apply:", job["how_to_apply"])
    # print("Company Logo:", job["company_logo"])
    print()
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")
    print()
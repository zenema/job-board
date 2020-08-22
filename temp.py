def create_job(title, location, age, company, description, url):
    return {
        "title": title,
        "location": location,
        "age": age,
        "company": company,
        "description": description,
        "url": url
    }


job_1 = create_job("Tech Writer", "Berlin", "2 Days", "Google Inc.",
                   "Job Description bla bla bla bla bla", "career.google.com/tech-writer")
job_2 = create_job("Data Scientist", "NY", "5 Days", "Facebook Inc.",
                   "Another job Description bla bla bla bla bla", "career.google.com/tech-writer")

job_list = []


def job_factory(job):
    job_list.append(job)


job_factory(job_1)
job_factory(job_2)

print(job_list)


# Das hier kommt am Ende dabei dann herraus. (Liste mit Objekten als Elemente) [{}]
[
    {'title': 'Tech Writer',
    'location': 'Berlin', 
    'age': '2 Days',
    'company': 'Google Inc.',
    'description': 'Job Description bla bla bla bla bla',
    'url': 'career.google.com/tech-writer'
    },

    {
    'title': 'Data Scientist',
    'location': 'NY',
    'age': '5 Days', 
    'company': 'Facebook Inc.', 
    'description': 'Another job Description bla bla bla bla bla', 
    'url': 'career.google.com/tech-writer'
    }
]

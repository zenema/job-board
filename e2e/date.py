import datetime

entry = "Wed Aug 20 04:21:47 UTC 2020"
entry2 = "Wed Aug 5 04:21:47 UTC 2020"
def entry_formatter(entry):
            today = datetime.datetime.today()
            difference = str(today - datetime.datetime.strptime(entry, '%a %b %d %H:%M:%S %Z %Y'))
            if("day" in difference):
                return difference.split(',')[0]
            else:
                return "today"
            

print(entry_formatter(entry))
print(entry_formatter(entry2))
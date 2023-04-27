import WorkScript

with open('Config.txt','r') as file:
    for details in file:
        email, password = details.split(',')

with open('Link.txt','r') as file:
    for details in file:
        link = details
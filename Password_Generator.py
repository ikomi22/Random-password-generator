# Importing thr relevant modules
from random import randint

# All uppercase password

password = ""
for i in range(10):
    i = chr(randint(65, 90))
    password = str(password) + i
print(password)

# Upper and lowercase password
password = ""
for i in range(10):
    i = chr((randint(65, 90)))
    for j in range(10):
        j = chr((randint(65, 90))).lower()
    password = str(password) + i + j
print(password)


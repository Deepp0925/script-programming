import urllib.request
import json
import datetime
import os
import re
import azuremaps

########## Global Variables ##########
# 1. Three Python list objects will be required to store our data found.
# Create 3 empty python lists named 'ips','unique_ips', and 'toJson'
# YOUR CODE HERE (3 lines)
ips = []
unique_ips = []
toJson = []


########## Extract IPs from log file ##########
# 2. A file object is needed to open our log file
# in logs/access.log
# Create with variable name "file". Read mode is only needed
# YOUR CODE HERE (1 line)
file = open("logs/access.log", "r")


# 3. You will need to iterate through the log file line by line
# looking for an IP address pattern. For example: 192.168.1.101
# RegEx would be most helpful searching for patterns. Each IP returned
# will be in the form of a list.
# You will need to use the 'extend' method to add each ip list
# to the new list 'ips'
# YOUR CODE HERE (< 5 lines)
for line in file:
    ips.extend(re.findall(
        r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', line))


# 4. Now that ips is populated, you will need to populate a new list
# called unique_ips removing all duplicates. One method is to convert
# the ips list to a set and then back to a list. Example: list(set(ips))
# YOUR CODE HERE (1 line)
unique_ips = list(set(ips))


# HINT: The number of total IPs found in the log file should return
# length of 300. The number of unique IPs found should return: 147
# Use print statements to validate your lists. It is recommended
# validating your list lenghts before proceeding...
print(ips)
print(len(ips))
print(len(unique_ips))


# 5. For the remaining steps, your function getCountry(ip) created in
# azure maps will be needed in order to
# return a country ISO code for each IP in the unique_ips list.
# Write a for loop to iterate through the unique_ips list.
# YOUR CODE HERE (1 line)
for ip in unique_ips:

    # 6. A variable user_country will be needed to store the country value.
    # Make a call to getCountry function in azuremaps.
    # YOUR CODE HERE (1 line)
    print(ip)
    user_country = azuremaps.getCountry(ip)

# IMPORTANT: Uncomment the three tick marks below and at the end
# of the code to complete rest of the assignment.

    # 7. Complete the if statement below to build a
    # dictionary with two key:value pairs. "user" will be a single ip address provided
    # through a variable. "country" will be the country code returned in a variable
    # you recentry created.
    # Lastly, the formated user will need to be appended to the toJson list.
    # YOUR CODE HERE (2 variables and method name)
    if user_country:
        user = {"user": ip,
                "country": user_country}
        toJson.append(user)


# Lastly, we must build the found.js file to be used with
# the javascript map library to place the circles on the world map.
# This section is already completed for you. Do not change ;)
file = open("js/found.js", "w")
file.writelines("var DATA = {\n")
file.writelines("users:"+str(toJson)+",\n")
file.write("created_at: new Date()\n")
file.writelines("};")


# If you completed all the steps, now it's time to check out your map!
# Open your index.html file and answer the questions below...

# 8. How many countries were identified with attacker addresses?
# Answer
answer8 = 0
# 9. Which country contained the most unique attacker addresses?
# Answer
answer9 = 0
# 10. How many total attackers have been identified?
# Answer
answer10 = 0

import firewall as fw
import packet as p

# 1. Your organization is in need of a firewall to block malicious
# network traffic. You are being asked to implement a software based
# firewall built in python. Follow the comments below to implement it.
# Create a new Firewall object with name "CS1411 Firewall". Review
# the firewall class to see how the object initiated
# Note: Use "cs1411FW" as the object name
# Run your script to see traffic flow in. You should see 737 allowed packets.
# Your code here
cs1411FW = fw.Firewall("CS1411 Firewall")


# 2. Now that traffic is flowing through the firewall, the security ops team
# has identified suspicious RDP traffic from 206.14.8.100 to 202.13.6.223.
# Add a new firewall rule to your firewall to block the traffic.
# You may need to look up the port number for RDP.
# Refer to the firewall class for examples to add a rule.
# You should see 7 packets blocked
# Your code here
cs1411FW.addRule(src="206.14.8.100", dst="202.13.6.223",
                 port="3389", action="Block")


# 3. What object type is the rules property of the firewall object?
# Use a print statement of the answer
# Your code here
print(type(cs1411FW.rules))


# 4. What object type is a rule in the rules property of the firewall object?
# Use a print statement of the answer
# Your code here
print(type(cs1411FW.rules[0]))


# 5. More RDP attempts and now SMTP are being attacked to systems inside your network.
# Adding individual rules for each source and destination is becoming
# a laborious effort. Since you have the source code for the firewall
# you can add a way to accept wildcard rules like the following example:
# Rule {"id":1,"src":"*","dst":"*","port":"123","action":"Block"}
# Modify the firewall class method "findRuleMatch" to account for
# wildcard source and destination addresses.
# After finishing your modification, add two rules below
# with the wildcards that will block SMTP and RDP ports.
# Your code here
cs1411FW.addRule(src="*", dst="*", port="25", action="Block")
cs1411FW.addRule(src="*", dst="*", port="3389", action="Block")


# Optional: Verbose Mode
# Change to True to see all traffic
cs1411FW.verbose = False


#### DO NOT MODIFY BELOW ####
networkLog = open("networkLog.txt", "r")
for line in networkLog.readlines():
    x = line.split(" ")
    a = p.Packet(x[0], x[1], x[2])
    cs1411FW.inspectPacket(a)

print("*************************")
print("Total Packets:", cs1411FW.totalPacketsBlocked +
      cs1411FW.totalPacketsAllowed)
print("Total Packets Blocked:", cs1411FW.totalPacketsBlocked)
print("Total Packets Allowed:", cs1411FW.totalPacketsAllowed)
print("*************************")

import sys

# Prompt the user for the required information
protocol = input("Enter the protocol (tcp, udp, icmp): ")
port = input("Enter the port number or range: ")
ip_address = input("Enter the IP address or range: ")
action = input("Enter the action (allow, deny): ")

# Generate the firewall rule
rule = "{} {} {} {}".format(protocol, port, ip_address, action)
print("Firewall rule:", rule)

# Save the firewall rule to a file
with open("firewall_rules.txt", "a") as f:
  f.write(rule + "\n")

# Ping values
ping = int(input("Enter the value:"))
ping_report = "low to average" if ping < 150 else "too high"
print(ping_report)
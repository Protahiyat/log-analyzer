import re
from collections import defaultdict, Counter
from datetime import datetime

# Adjust this to the path where your auth.log file is located
log_file_path = "auth.log"

# Regex pattern to find failed login attempts with IP addresses
failed_login_pattern = re.compile(r"(?P<month>\w+)\s+(?P<day>\d+)\s(?P<time>\d+:\d+:\d+).*sshd.*Failed password.*from (?P<ip>\d+\.\d+\.\d+\.\d+)")


failed_attempts = 0
ip_counter = Counter()
hour_counter = defaultdict(int)

with open(log_file_path, "r") as f:
    for line in f:
        match = failed_login_pattern.search(line)
        if match:
            failed_attempts += 1
            ip = match.group("ip")
            ip_counter[ip] += 1

            # Parse the hour
            hour_str = match.group("time").split(":")[0]
            hour_counter[hour_str] += 1

# Get top 5 IPs
top_5_ips = ip_counter.most_common(5)

#Find the hour with most alerts
top_hour = max(hour_counter.items(), key=lambda x: x[1], default=("N/A", 0))[0]

# Output
print("==== Log Analysis Results ====")
print(f"Total Failed Login Attempts: {failed_attempts}")

print("\nTop 5 IPs by Activity: ")
if top_5_ips:
    for ip, count in top_5_ips:
        print(f"{ip}: {count} attempts")
else:
    print("No IPs found.")

print(f"\nHour with Most Alerts: {top_hour}")

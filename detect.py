log_file = "auth.log"

failed_attempts = {}

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            parts = line.split("from")
            ip = parts[1].strip()

            if ip in failed_attempts:
                failed_attempts[ip] += 1
            else:
                failed_attempts[ip] = 1

print(" Suspicious Activity:")

for ip, count in failed_attempts.items():
    if count > 2:
        print(f"{ip} has {count} failed attempts (Possible Brute Force)")
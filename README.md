#  SIEM Detection Lab (Custom)

##  Objective
Detect brute force login attempts using log analysis.

## ⚙️ What I Built
- Created authentication logs
- Developed a Python-based detection system
- Identified suspicious IPs based on repeated failed logins

##  Detection Logic
Counts failed login attempts per IP  
Flags any IP with more than 2 failed attempts

##  Tools Used
- Python
- Log Analysis

##  Output
192.168.1.10 has 3 failed attempts (Possible Brute Force)

##  Future Improvements
- Real-time log monitoring
- Dashboard visualization
- Detect multiple attack types

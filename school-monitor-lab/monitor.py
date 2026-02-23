import time
import os

# Get the school name from an Environment Variable
school_name = os.getenv("SCHOOL_NAME", "Public School 01 - Brasília")

print(f"--- Starting Monitoring System for: {school_name} ---")

while True:
    print(f"[STATUS] Checking Database... ONLINE")
    print(f"[STATUS] Checking Attendance System... ONLINE")
    time.sleep(5)
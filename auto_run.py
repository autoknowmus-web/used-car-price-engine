import time
import subprocess

while True:
    subprocess.run(["python", "read_form.py"])
    print("Checking for new form responses...")
    time.sleep(30)
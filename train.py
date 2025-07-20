from wakepy import keep
import time

with keep.presenting():
    print("Display will stay awake. Running task...")
    # Replace this with your long-running workload
    time.sleep(60*60)  # e.g., 1 hour

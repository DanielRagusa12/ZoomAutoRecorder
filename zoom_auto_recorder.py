import obsws_python as obs
import sys
import os
from datetime import datetime
import webbrowser
import time
from dotenv import load_dotenv


def main():
    load_dotenv()

    
    # check if obs is running
    if os.system("tasklist | find /i \"obs64.exe\" >nul 2>&1") == 1:
        print("OBS is not running")
        sys.exit()
    # connect to obs
    try:
        cl = obs.ReqClient(host='localhost', port=4455, password=os.getenv('OBS_PASSWORD'), timeout=3)
        resp = cl.get_version()
        print(f"[Connected] OBS Version: {resp.obs_version}")
    except Exception as e:
        print(f"Error connecting to OBS: {e}")
        sys.exit(1)

    # ask user for zoom link
    zoom_link = ""
    while not zoom_link.strip():
        zoom_link = input("Enter Zoom link: ")

    # ask user the time to start recording
    start_time = ""
    while not start_time.strip():
        start_time = input("Class Time (24H Format) [HH:MM] (): ")

    
    # convert start_time to datetime.time object
    try:
        start_time = datetime.strptime(start_time, "%H:%M").time()
    except ValueError:
        print("Invalid time format. Please enter time in 24-hour format (HH:MM).")
        sys.exit()
    
    # wait for class to start
    while True:
        current_time = datetime.now().time()
        if current_time > start_time:
            break
        print("Waiting for class to start...")
        time.sleep(10)
        sys.stdout.flush()
    
    print("Class has started!")
    time.sleep(2)
    webbrowser.open(zoom_link)
    time.sleep(5)

    # wait for zoom to open
    while(True):
        # check if zoom is open
        if os.system("tasklist | find /i \"zoom.exe\" >nul 2>&1") == 0:
            print("Zoom is open")
            break
    
    # start recording
    try:
        # check if obs is recording
        resp = cl.get_record_status()
        print(f"Recording: {resp.output_active}")

        if resp.output_active:
            # stop recording
            resp = cl.stop_recording()
            print(f"Recording stopped: {resp}")
        # start recording
        resp = cl.start_record()
        print("Recording started")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    

if __name__ == "__main__":
    main()
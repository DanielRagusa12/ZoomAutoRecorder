# OBS Zoom Recorder

## Overview

This Python script is designed to automate the process of starting OBS (Open Broadcaster Software), opening a Zoom meeting, and initiating the recording of the meeting. The motivation behind creating this project was to address the issue of being consistently late to this one Zoom meeting due to traffic on my way home from campus. The script does not end the recording and does not create any scenes, you must already have your desired scene set up in OBS. The [obsws-python](https://github.com/aatikturk/obsws-python) SDK has much more capability that can be explored so feel free to modify the script to your own specific use case.

## Requirements

Before using this script, ensure that you have the following:

- [Open Broadcaster Software (OBS)](https://obsproject.com/)
- [OBS Websocket v5 Plugin](https://github.com/obsproject/obs-websocket/releases/tag/5.0.0)

- Zoom client installed on your machine.
- Python installed on your machine (version 3.x recommended).

- Your default browser has permissions to automatically launch zoom.

## Setup

1. Clone or download the repository to your local machine.

   ```bash
   git clone https://github.com/DanielRagusa12/obs-zoom-recorder.git
   ```

2. Navigate to the project directory.

   ```bash
   cd obs-zoom-recorder
   ```
***
3. Create a virtual env (optional but recommended)
   ```bash
   python -m venv venv
   ```
    Activate it

    - Powershell
        ```bash
        .\venv\Scripts\activate
        ```
    - Command Prompt
        ```bash
        venv\Scripts\activate
        ```
    - Unix or MacOS
        ```bash
        source venv/bin/activate
        ```

***
4. Install the required Python packages.

   ```bash
   pip install -r requirements.txt
   ```
5. Open OBS, go to Tools then WebSocket Server Settings
   
   Check the box to enable the WebSocket server and set your port and password.

&nbsp;


6. Create a `.env` file in the project directory and add your OBS password.

   ```
   OBS_PASSWORD=your_obs_password
   ```

## Usage

1. Run the script using the following command:

   ```bash
   python obs_zoom_recorder.py
   ```

2. The script will check if OBS is running. If not, it will exit with a message.

3. Enter the Zoom meeting link when prompted.

4. Enter the class start time in 24-hour format (HH:MM) when prompted.

5. The script will wait until the specified class time before opening the Zoom meeting.

6. Once the class starts, the Zoom meeting will open automatically.

7. The script will continuously check if Zoom is open, and when detected, it will start recording using OBS.

8. The recording status will be displayed, and the script will automatically stop the recording if it's already active.

9. The script will start recording the Zoom meeting.

## Notes
- This script does not generate a new scene. You must configure your own scene for Zoom recording.
- There's a zoom setting to always open meetings in fullscreen.
- Make sure to keep OBS and Zoom in the default installation directories.
- Ensure that the OBS password is correctly set in the `.env` file.

Feel free to customize the script according to your needs and preferences.
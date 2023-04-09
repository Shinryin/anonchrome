# anonchrome
This tool launches Google Chrome in incognito mode with enhanced privacy and security features using the undetected-chromedriver library. The script clears existing Chrome data and creates a new temporary Chrome user profile directory for the session.

The script uses various Chrome options to improve privacy and security, including:

- Disabling browser notifications, GPU acceleration, and software rendering
- Disabling web security, which allows loading of local files in Chrome
- Disabling features that enable browser fingerprinting, such as WebGL and WebRTC
- Blocking third-party cookies and disabling canvas anti-aliasing rendering
- Bypassing most captchas that are not IP-based.

# Installation/Build
Head over to releases and install anonchrome.exe, this is standalone version made with Nuitka.
All you need to do then is run anonchrome.exe - and the program will run!
OR, you can build the program if you'd like:
- Install Python (version 3.6 or later).
- Selenium
- undetected-chromedriver
Build the script as a .py file and run it using CMD. You will need Chrome on your system.

# Usage
- After starting the program, enter the URL you would like to visit.
- The window will run and you can do whatever you need. Then just press enter on the tool again to end the temporary session.

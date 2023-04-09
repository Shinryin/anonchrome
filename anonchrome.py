import os
import shutil
from selenium import webdriver
import undetected_chromedriver as uc

def clear_chrome_data(chrome_data_path):
    if os.path.exists(chrome_data_path):
        try:
            shutil.rmtree(chrome_data_path)
        except Exception as e:
            print(f"Error clearing Chrome data: {e}")

def launch_chrome_incognito():
    chrome_data_path = os.path.join(os.getcwd(), 'chrome_data')
    clear_chrome_data(chrome_data_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument(f"--user-data-dir={chrome_data_path}")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-features=site-per-process")
    options.add_argument("--disable-blink-features=EnumerateDevices")
    options.add_argument("--disable-blink-features=MediaStreamConstraints")
    options.add_argument("--disable-blink-features=AudioContext")
    options.add_argument("--disable-blink-features=WebGL")
    options.add_argument("--disable-blink-features=WebRTC")
    options.add_argument("--disable-blink-features=PictureInPictureAPI")
    options.add_argument("--disable-blink-features=GamepadAPI")
    options.add_argument("--disable-blink-features=GetUserMedia")
    options.add_argument("--disable-geolocation")
    options.add_argument("--disable-accelerated-video-decode")
    options.add_argument("--block-third-party-cookies")
    options.add_argument("--disable-canvas-aa-rendering")
    driver = uc.Chrome(executable_path="chromedriver", options=options)
    return driver

if __name__ == "__main__":
    try:
        url = input("Enter a URL: ")
        driver = launch_chrome_incognito()
        driver.get(url)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        input("Press any key to close the browser...")
        driver.quit()

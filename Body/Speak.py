# Speak Functions - Two Speak Functions

# Windows Based - pip install pyttsx3
# Chrome Based - pip install selenium==4.1.3

# Windows Based
# Advantages = Fast , Offline.
# Disadvantages =  OverSpeak , Less Voices.

# import pyttsx3

# def Speak(Text):
#     engine = pyttsx3.init("sapi5")
#     voices = engine.getProperty('voices')
#     engine.setProperty('voices',voices[1].id)
#     engine.setProperty('rate',170)
#     print("")
#     print(f"You : {Text}.")
#     print("")
#     engine.say(Text)
#     engine.runAndWait()

# Chrome Base
# Advantages = More Voices, More Clear , Overspeaking.
# Disadvantages = Word Limit, Slow.

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Specify the path to the Chrome executable
chrome_executable_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

# Set up the Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Add any other options you need

# Set up the service
service = Service(chrome_executable_path)


chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = True
Path = "DataBase\\chromedriver.exe"
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

website = r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
ButtonSelection = Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
ButtonSelection.select_by_visible_text('British English / Brian')

def Speak(Text):

    lengthoftext = len(str(Text))

    if lengthoftext==0:
        pass

    else:
        print("")
        print(f"AI : {Text}.")
        print("")
        Data = str(Text)
        xpathofsec = '/html/body/div[4]/div[2]/form/textarea'
        driver.find_element(By.XPATH,value=xpathofsec).send_keys(Data)
        driver.find_element(By.XPATH,value='//*[@id="vorlesenbutton"]').click()
        driver.find_element(By.XPATH,value="/html/body/div[4]/div[2]/form/textarea").clear()

        if lengthoftext>=30:
            sleep(4)

        elif lengthoftext>=40:
            sleep(6)

        elif lengthoftext>=55:
            sleep(8)

        elif lengthoftext>=70:
            sleep(10)

        elif lengthoftext>=100:
            sleep(13)

        elif lengthoftext>=120:
            sleep(14)

        else:
            sleep(2)


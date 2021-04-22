import os
import smtplib
import time
from selenium import webdriver
from email.message import EmailMessage
PATH = "C:\SeleniumChromeDriver\chromedriver.exe"

def chromedriver():
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.tesco.com/")
    driver.maximize_window()
    element_1 = driver.find_element_by_class_name("search-logo-container")
    element_2 = element_1.find_element_by_class_name("input-text-box  ").send_keys("eat natural")
    button = element_1.find_element_by_class_name("search-icon-button").click()

    natural = driver.find_element_by_id("content")
    # natural_1 = natural.find_element_by_class_name("tile-content")
    natural_2 = natural.find_element_by_id("tile-284256556")
    natural_curr = natural_2.find_element_by_class_name("currency")
    natural_3 = natural_2.find_element_by_class_name("value")
    natural_4 = natural_2.find_element_by_class_name("product-details--content")
    text_value1 = natural_3.text
    text_value = natural_4.text
    currency = natural_curr.text
    if text_value1 >= "1.00":
        print(f"Item price is: {text_value1} {currency}")
        driver.close()
        time.sleep(60)
        return chromedriver()
    else:
        print(f"{text_value} {text_value1}")
        return (f"{text_value} {text_value1} {currency}")
    #print(f"{text_value} {text_value1}")
    #return (f"{text_value} {text_value1}")

def mail_sending():
    mail_sender =  os.environ.get('mail_sender')
    sender_pass = os.environ.get('sender_pass')
    mail_receiver = os.environ.get('mail_receiver')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(mail_sender, sender_pass)

        message = EmailMessage()
        message["Subject"] = "Eat Natural price"
        message["From"] = mail_sender
        message["To"] = mail_receiver
        message.set_content(chromedriver())
        smtp.send_message(message)
mail_sending()

#chromedriver()
#a simple script that sends english words with theri definition to a specified email
from bs4 import BeautifulSoup
import requests
import random
import schedule
import time
import smtplib
import os
pwd=os.environ.get('gmail')
print(pwd)
URL = "https://www.vocabulary.com/lists/176046"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

corrupted = [t.text for t in soup.find_all(attrs={"class": "word dynamictext"})]
corrupted_2 = [t.text for t in soup.find_all(attrs={"class": "definition"})]

def pick_random_word():
    my_dict = dict(zip(corrupted, corrupted_2))
    random_word=random.choice(list(my_dict.items()))
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("simo.rko10@gmail.com", pwd)
    subject='Your daily English word'
    body= random_word
    msg=f'Subject:{subject}\n \n {body} '
    server.sendmail('simo.rko10@gmail.com','simo.rko10@gmail.com',msg)
    server.sendmail('simo.rko10@gmail.com', 'yas.amel98@gmail.com', msg)
    
schedule.every(10).seconds.do(pick_random_word)
while True:
     schedule.run_pending()
     time.sleep(30)
   

  


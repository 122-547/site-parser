#code
       # import requests
       # from LxmlSoup import LxmlSoup
       # with open("parse_information.txt", "w") as file:
       #               file.write('')
       # url = input('Write Url Address: ')
       # tag_name = input('Write Element`s Tag Name: ')
       # class_name = input('Write Element`s Class Name: ')
       # html = requests.get(url).text

       # soup = LxmlSoup(html)
       # texts = soup.find_all(tag_name, class_=class_name)
       # for text in texts:
       #        name = text.text()
       #        with open("parse_information.txt", "a") as file:
       #               file.write(f"#------------------------------------#\n \n{name}\n \n")

#code's end

from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from LxmlSoup import LxmlSoup

def fail_function(function_text_name):
       return f"We can't find this word: {function_text_name}"


try:
       url = "https://psycatgames.com/ru/magazine/conversation-starters/things-to-talk-about/"
       text_name = input("Search Word: ")
       
       
       
       html = requests.get(url).text
       soup = LxmlSoup(html)
       
       link = soup.find_all('h3')
       for i in link:
              tag_name = i.text
              print(f"Find Text: {tag_name}")

except:
       fail_function(text_name)
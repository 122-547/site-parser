#code
import requests
from LxmlSoup import LxmlSoup
with open("parse_information.txt", "w") as file:
              file.write('')
url = input('Write Url Address: ')
tag_name = input('Write Element`s Tag Name: ')
class_name = input('Write Element`s Class Name: ')
html = requests.get(url).text

soup = LxmlSoup(html)
texts = soup.find_all(tag_name, class_=class_name)
for text in texts:
       name = text.text()
       with open("parse_information.txt", "a") as file:
              file.write(f"#------------------------------------#\n \n{name}\n \n")

#code's end
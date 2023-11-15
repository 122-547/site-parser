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

#-----------------------------------------------------------#
       
# from LxmlSoup import LxmlSoup
# import requests

# html = requests.get('https://www.virustotal.com/gui/home/upload').text  # получаем html код сайта
# soup = LxmlSoup(html)  # создаём экземпляр класса LxmlSoup

# links = soup.find_all('a', class_='blue-link')  # получаем список ссылок и наименований
# for i, link in enumerate(links):

#     name = link.text()
#     url = link.find('href')
#     print(i)
#     print(f"Url - {url}")  # извлекаем наименование из блока со ссылкой # извлекаем цену
#     print(f"Name - {name}")

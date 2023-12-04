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

# import requests
# from LxmlSoup import LxmlSoup

# def fail_function(function_text_name):
#        return f"We can't find this word: {function_text_name}"


# try:
#        url = "https://psycatgames.com/ru/magazine/conversation-starters/things-to-talk-about/"
#        text_name = input("Search Word: ")
       
       
       
#        html = requests.get(url).text
#        soup = LxmlSoup(html)
       
#        link = soup.find_all('h3')
#        for i in link:
#               tag_name = i.text
#               print(f"Find Text: {tag_name}")

# except:
#        fail_function(text_name)

#code


# import requests
# from LxmlSoup import LxmlSoup

# def failed_progress(word_name):
#        return f"We can't find {word_name}"

# url = "https://ru.wikipedia.org/wiki/%D0%92%D0%B8%D0%BA%D0%B8%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F"
# word_name = input("Search Word: ")

# html = requests.get(url).text
# soup = LxmlSoup(html)
# sentences = soup.find(text=word_name).text

# print(sentences)
       
#code

import requests
from LxmlSoup import LxmlSoup

input_word = input("Search Word: ")
url = "https://ru.wikipedia.org/wiki/" + input
html = requests.get(url).text
soup = list(LxmlSoup(html).text())
text = ""
list_ = []


for i in range(len(soup)):
       i_t = i + 1
       if i != len(soup) - 1:
              if soup[i] + soup[i_t] != ". ":
                     text = text + soup[i]
              else:
                     text = text + "."
                     list_.append(text)
                     text = ""
       

for g in list_:
              if g.find(';') == -1:
                     if g.find(':') == -1:
                             if g.find('"') == -1:
                                     if g.find("'") == -1:
                                          
                                          if g.find(input_word) != -1 and len(g) >= 20:
                                                 print(f"::{g}")
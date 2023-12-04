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

class ParseInformation:
       def __init__(self, input_word):
              self.input_word = input_word
              url = "https://ru.wikipedia.org/wiki/" + self.input_word
              html = requests.get(url).text
              self.soup = list(LxmlSoup(html).text())
              self.text = ""
              self.list_ = []
              self.main_data = []
       def Parse(self):
              for i in range(len(self.soup)):
                     i_t = i + 1
                     if i != len(self.soup) - 1:
                            if self.soup[i] + self.soup[i_t] != ". ":
                                   self.text = self.text + self.soup[i]
                            else:

                                   self.list_.append(self.text)
                                   self.text = ""
              for g in self.list_:
                            if g.find(';') == -1:
                                   if g.find(':') == -1:
                                           if g.find('"') == -1:
                                                   if g.find("'") == -1:
                                                        if g.find(self.input_word) != -1 and len(g) >= 20:
                                                               self.main_data.append(g)
              if self.main_data == []:
                      print("Error: <word not found>")
              return self.main_data

# from tkinter import *
# import keyboard

# def function():
#        ent_text = entry.get()
#        parse = ParseInformation(input_word=ent_text)
#        parse.Parse()
#        for i in parse.main_data:
#               text1.insert(END, f"\n{i}")
# root = Tk()

# root.title("    ")
# root.resizable(0,0)
# root.geometry("700x600")
# # root.iconphoto(PhotoImage(file="image.png"))
# root["bg"] = "grey"
# entry = Entry(root, bg="white", font="Arial 11")
# entry.place(width=700, height=40)
# text1 = Text(root, bg="white", font="Arial 11")
# text1.place(width=700, height=560, x=0, y=40)

# keyboard.add_hotkey("Enter", function)
# root.mainloop()

#code 

input_word = input("Search Word: ")
ps = ParseInformation(input_word)
with open("Parse_File.txt", "w") as file:
               file.write("")
for i in ps.Parse():
       with open("Parse_File.txt", "a", encoding="utf-8") as file:
               file.write(i)
               
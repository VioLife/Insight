#curl -s wttr.in | sed -n "1,7p" - альтернативный вариант проверки погоды :)

from bs4 import BeautifulSoup
import requests
from tkinter import *
from tkinter import messagebox
from time import gmtime, strftime
#from PIL import Image #пока не удалось все компоненты этой библиотеки загрузить

root = Tk()
root.title("Прогноз погоды")
root.geometry("500x400")
root["bg"] = "lightblue"

#new = Image.open("logo.png")
#panel = Label(root, image=new)
#panel.place(x=0, y=420)

Label(root, text = "Прогноз погоды",font = "Consolas 15 bold", bg = "lightblue").pack(pady=5)
Label(root, text = "Укажите название города:",font = "Consolas 11 bold", bg = "lightblue").pack(pady=5)

city = Entry(root,width=45)
city.pack()

def Yandex():
    n = str(city.get())
    search = f"Погода в {n}"
    
    url = f"https://yandex.com.am/weather/?via=hl={search}" #cпарсила с сайта яндекс погода нужные мне данные
    
    r = requests.get(url)
    s = BeautifulSoup(r.text,"html.parser")
    
    
    a = s.find('span', 'temp__value temp__value_with-unit')
    a = a.text
    d = s.find('div', 'link__condition day-anchor i-bem')
    d = d.text
    #b = s.find('span', 'wind-speed') #cопротивляется и настойчиво не хочет показывать скорость ветра
    #b = b.text
    k = s.find('div', 'term term_orient_v fact__humidity')
    k = k.text
    e = s.find('div', 'term term_orient_v fact__pressure')
    e = e.text
    c = s.find('span', 'a11y-hidden')
    c = c.text
    
    time = strftime("%d-%m-%y %H:%M:%S", gmtime())
    
    box = messagebox.showinfo("Прогноз погоды","Сегодня" +  time  + "в городе " + n + "температура" + a + d + c + k + e) 
    
    city.delete(first=0,last=10000)
    
Button(root, text="Запросить данные погоды", command=Yandex).pack(pady=13)
Label(root,text="DISNEY prodaction",fg="white", bg ="lightblue").pack(pady=16)

root.mainloop()

    
                                                                                


#url = 'https://yandex.com.am/weather/?via=hl'
#page = requests.get(url)

#filteredWeather = []
#SaveInfo = []
#SaveInfo1 = []
#SaveInfo2 = []
#soup = BeautifulSoup(page.text, "html.parser")


#time = strftime("%d-%m-%y %H:%M:%S", gmtime())
#print(time)

#a = soup.find('span', 'temp__value temp__value_with-unit')
#print(a.text)

#b = soup.find('span', 'wind-speed')
#print(b.text)

#c = soup.find('span', 'a11y-hidden')
#print(c.text)

#d = soup.find('div', 'link__condition day-anchor i-bem')
#print(d.text)

#e = soup.find('div', 'term term_orient_v fact__pressure')
#print(e.text)

#k = soup.find('div', 'term term_orient_v fact__humidity')
#print(k.text)



#curl -s wttr.in | sed -n "1,7p"
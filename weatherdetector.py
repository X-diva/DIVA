import tkinter as tk
import datetime as dt
import requests
import json
import tkinter.messagebox as mb
window = tk.Tk()
window.title("Weather detector")
window.geometry("400x300")

city=tk.Label(window,text='Enter the name of the city:',fg='#728FCE',font=('Helvetica',9,'bold'))
city.grid(row=0,column=0)
city_entry=tk.Entry(window,width=10)
city_entry.grid(row=0,column=1)



def getWeather():
  city_name=str(city_entry.get())
  temp=tk.Label(window,text='Temperature (°C)',fg='#728FCE',font=('Arial',9,'bold'))  
  temp.grid(row=2,column=0)
  temp_entry=tk.Entry(window,width=9)
  temp_entry.grid(row=2,column=1)
  hum=tk.Label(window,text='  Humidity (%)  ',fg='#728FCE',font=('Arial',9,'bold'))  
  hum.grid(row=3,column=0)
  hum_entry=tk.Entry(window,width=9)
  hum_entry.grid(row=3,column=1)
  vit=tk.Label(window,text='Wind speed (m/s)',fg='#728FCE',font=('Arial',9,'bold'))  
  vit.grid(row=4,column=0)
  vit_entry=tk.Entry(window,width=9)
  vit_entry.grid(row=4,column=1)
  pres=tk.Label(window,text=' Pression (hPa) ',fg='#728FCE',font=('Arial',9,'bold'))  
  pres.grid(row=5,column=0)
  pres_entry=tk.Entry(window,width=9)
  pres_entry.grid(row=5,column=1)
  base_url = "http://api.openweathermap.org/data/2.5/weather"
  api_key = "8ed7eb542f4c394471013f0926f41c8a"
  url = f"{base_url}?q={city_name}&appid={api_key}"
  page=requests.get(url)
  if page.status_code==200:
    data=page.json()
    pp=data['main']
    tempe=pp['temp']-273.15
    humi=pp['humidity']
    vite=data['wind']['speed']
    press=pp['pressure']
    pres_entry.insert(0,press)
    vit_entry.insert(0,vite)
    hum_entry.insert(0,humi)
    temp_entry.insert(0,tempe)
  else:
    mb.showerror(title='Error',message='City not found, try again and enter a valid city name :)')
    city_entry.delete(0,tk.END)
    
butt=tk.Button(window,width=7,text='Get Weather',command=getWeather,fg='white',font=('Arial',7,'bold'),bg='#728FCE')
butt.grid(row=1,column=1)

window.mainloop()
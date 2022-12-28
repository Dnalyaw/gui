#api_testing
from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("Weather App")
#root.geometry("600x100")

myLabel = Label(root)

def zipLookup():
    global myLabel
    myLabel.destroy()
    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=6D0E96AD-2C13-42ED-98F9-661B7932D0A9")
        api = json.loads(api_request.content)  # changes from json to python
        city = api[0]["ReportingArea"]
        quality = api[0]["AQI"]
        category = api[0]["Category"]["Name"]

        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"

        root.configure(background=weather_color)

        myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20), padx=10, pady=10, background=weather_color)
        myLabel.grid(row=1, column=0, columnspan=2)
    except Exception:
        myLabel = Label(root, text="Sorry, that didn't work. Try a different zipcode", font=("Helvetica", 20), padx=10, pady=10)
        myLabel.grid(row=1, column=0, columnspan=2)

zip = Entry(root, font=("Helvetica", 15))
zip.grid(row=0, column=0, stick=W+E+N+S)

zipButton = Button(root, text="Lookup Zipcode", font=("Helvetica", 15), command=zipLookup)
zipButton.grid(row=0, column=1, stick=W+E+N+S)


root.mainloop()
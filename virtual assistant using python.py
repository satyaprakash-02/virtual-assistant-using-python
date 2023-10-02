import datetime
import webbrowser
import pyttsx3
import pywhatkit
import speech_recognition
import wikipedia
import os
import requests
from GoogleNews import GoogleNews
import pandas as pd
import time


import pyjokes
import random


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices") 
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


hour = int(datetime.datetime.now().hour)
if 0 <= hour <= 12:
    speak("Good Morning sir, how may I help you?")
elif 12 < hour <= 18: 
    speak("Good Afternoon sir, how may I help you?") 
else:
    speak("Good Evening sir, how may I help you?")


def takeCommand():
    r = speech_recognition.Recognizer()
    query=""
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 4
        r.energy_threshold = 300 
        audio = r.listen(source, 0, 4)
    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-us')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Please Say that Again!!")
        return None
    return query


def searchGoogle(query):
    import wikipedia as googleScrap
    speak("This is what I found")
    try:
        pywhatkit.search(query)
        result = googleScrap.summary(query, 1)
        speak(result)
    except:
        speak("Did not find anything about that,Sorry!!")


def searchYoutube(query):
    web = "https://www.youtube.com/results?search_query=" + query
    #webbrowser.open(web)
    pywhatkit.playonyt(query)
    speak("Done, Sir")


def searchWikipedia(query):
    results = wikipedia.summary(query,sentences=2)
    speak("According to wikipedia..")
    print(results)
    speak(results)


def open_application(query):
    if "web browser" in query or "chrome" in query or "browser" in query:
        speak("Opening Google Chrome")
        os.startfile("C://Program Files//Google//Chrome//Application//chrome.exe")
    elif "note" in query or "notes" in query or "notepad" in query or "editor" in query:
        speak("Opening Notepad")
        os.startfile("C://WINDOWS//system32//notepad.exe")
    elif "vlc" in query or "vlcplayer" in query or "player" in query or "video player" in query:
        speak("Opening VLC Player")
        os.startfile("C://Program Files//VideoLAN//VLC//vlc.exe")
    elif "excel" in query or "msexcel" in query or "sheet" in query or "ms excel" in query:
        speak("Opening Microsoft Excel")
        os.startfile("C://Program Files//Microsoft Office//root//Office16//EXCEL.exe")
    elif "ppt" in query or "ms powerpoint" in query or "mspowerpoint" in query or "powerpoint" in query:
        speak("Opening Microsoft Powerpoint")
        os.startfile("C://Program Files//Microsoft Office//root//Office16//POWERPNT.exe")
    elif "word" in query or "ms word" in query or "msword" in query:
        speak("Opening Microsoft Word")
        os.startfile("C://Program Files//Microsoft Office//root//Office16//WINWORD.exe")
    elif "access" in query or "msaccess" in query or "ms access" in query:
        speak("Opening Microsoft Access")
        os.startfile("C://Program Files//Microsoft Office//root//Office16//MSACCESS.exe")
    elif "outlook" in query or "mail" in query:
        speak("Opening Microsoft Outlook")
        os.startfile("C://Program Files//Microsoft Office//root//Office16//OUTLOOK.exe")
    elif "whatsapp" in query:
        speak("Opening Whatsapp")
        webbrowser.open_new_tab("https://web.whatsapp.com/")
    elif "insta" in query or "instagram" in query:
        speak("Opening Instagram")
        webbrowser.open_new_tab("https://www.instagram.com/")
    elif "twitter" in query:
        speak("Opening Twitter")
        webbrowser.open_new_tab("https://twitter.com/")
    elif "spotify" in query or "media player" in query:
        speak("Opening Spotify")
        os.startfile('C://Users//nikhi//AppData//Local//Microsoft//WindowsApps//spotify')
       

def weather_report(query):
    url='https://wttr.in/{}'.format(query)
    try:
        data = requests.get(url)
        city = data.text
    except:
        city = "Error Occured"

    speak(f"{query}\n is as follows")
    print(city)


def news_report(query):
    gNews = GoogleNews(period='id')
    gNews.search(query)
    result = gNews.result()
    data = pd.DataFrame.from_dict(result)
    data = data.drop(columns=["img"], axis=1)
    data.head()
    speak(f"{query}\n are as follows")
    for res in result:
        print("\nTitle: ", res["title"])
        print("Details: ", res["link"])


def joke():
    res = pyjokes.get_joke()
    print(res)
    speak(res)


def game():
    speak("Choose any game you want to play")
    lst = ["https://www.crazygames.com/", "https://poki.com/","https://www.arkadium.com/free-online-games/"]
    r = random.choice(lst)
    print(webbrowser.open_new_tab(r))


def shop(query):
    if "amazon" in query or "flipkart" in query or "myntra" in query:
        if "amazon" in query:
            speak("Opening Amazon")
            webbrowser.open_new_tab("https://www.amazon.in/")
        elif "myntra" in query:
            speak("Opening Myntra")
            webbrowser.open_new_tab("https://www.myntra.com/")
        elif "flipkart" in query:
            speak("Opening Flipkart")
            webbrowser.open_new_tab("https://www.flipkart.com/")
        else:
            speak("Sorry, Metioned shop not available at the moment.")
    else:
        print("Where do you want to shop from? Amazon, Myntra or Flipkart?")
        speak("Where do you want to shop from? Amazon, Myntra or Flipkart?")
        query = takeCommand().lower()
        if "amazon" in query:
            speak("Opening Amazon")
            webbrowser.open_new_tab("https://www.amazon.in/")
        elif "myntra" in query:
            speak("Opening Myntra")
            webbrowser.open_new_tab("https://www.myntra.com/")
        elif "flipkart" in query:
            speak("Opening Flipkart")
            webbrowser.open_new_tab("https://www.flipkart.com/")
        else:
            speak("Sorry, Metioned shop not available at the moment.")


def mov(query):
    if "amazon" in query or "netflix" in query or "hotstar" in query or "zee5" in query or "sony" in query:
        if "amazon prime" in query:
            webbrowser.open_new_tab("https://www.primevideo.com/")
        elif "netflix" in query:
            webbrowser.open_new_tab("https://www.netflix.com/in/")
        elif "hotstar" in query:
            webbrowser.open_new_tab("https://www.hotstar.com/in")
        elif "zee5" in query:
            webbrowser.open_new_tab("https://www.zee5.com/")
        elif "sony" in query:
            webbrowser.open_new_tab("https://www.sonyliv.com/")
    else:
        print("Where do you want to stream? Amazon Prime Video, Netflix, Hotstar, Zee5 or Sony Liv")
        speak("Where do you want to stream? Amazon Prime Video, Netflix, Hotstar, Zee5 or Sony Liv")
        query = takeCommand().lower()
        if "amazon prime" in query:
            webbrowser.open_new_tab("https://www.primevideo.com/")
        elif "netflix" in query:    
            webbrowser.open_new_tab("https://www.netflix.com/in/")
        elif "hotstar" in query:
            webbrowser.open_new_tab("https://www.hotstar.com/in")
        elif "zee5" in query:
            webbrowser.open_new_tab("https://www.zee5.com/")
        elif "sony" in query:
            webbrowser.open_new_tab("https://www.sonyliv.com/")
        else:
            speak("Sorry, mentioned streamer not available at the moment.")

        
def conv(query):
    if "pdf to word" in query or "pdf file to word file" in query:
        webbrowser.open_new_tab("https://smallpdf.com/pdf-to-word")
    elif "word to pdf" in query or "word document to pdf" in query or "word file to pdf file" in query:
        webbrowser.open_new_tab("https://smallpdf.com/word-to-pdf")
    elif "text" in query or "text to speech" in query:
        speak("Enter your text: ")
        sp = input("Enter text you want to be converted to a speech: ")
        speak(sp)
    else:
        searchGoogle(query)


def book(query):
    if "airways" in query or "railways" in query or "roadways" in query or "movie tickets" in query or "movie" in query or "movie ticket" in query:
        if "airways" in query:
            print("From where do you want to book tickets? Makemytrip, Goibibo, Easemytrip or IRCTC")
            speak("From where do you want to book tickets? Make my trip, Goibibo, Ease my trip or IRCTC")
            query = takeCommand().lower()
            if "make my trip" in query:
                webbrowser.open_new_tab("https://www.makemytrip.com/flights/")
            elif "goibibo" in query:
                webbrowser.open_new_tab("https://www.goibibo.com/flights/")
            elif "ease my trip" in query:
                webbrowser.open_new_tab("https://www.easemytrip.com/flights.html")
            elif "irctc" in query:
                webbrowser.open_new_tab("https://www.air.irctc.co.in/")
            else:
                speak("Mentioned booking source is not available at the moment")

        elif "railways" in query:
            print("From where do you want to book tickets? Makemytrip, Goibibo, Easemytrip or IRCTC")
            speak("From where do you want to book tickets? Make my trip, Goibibo, Ease my trip or IRCTC")
            query = takeCommand().lower()
            if "make my trip" in query:
                webbrowser.open_new_tab("https://www.makemytrip.com/railways/")
            elif "goibibo" in query:
                webbrowser.open_new_tab("https://www.goibibo.com/trains/")
            elif "ease my trip" in query:
                webbrowser.open_new_tab("https://www.easemytrip.com/railways/")
            elif "irctc" in query:
                webbrowser.open_new_tab("https://www.irctc.co.in/nget/train-search")
            else:
                speak("Mentioned booking source is not available at the moment")

        elif "roadways" in query or "bus" in query:
            print("From where do you want to book tickets? Makemytrip, Goibibo, Easemytrip or IRCTC")
            speak("From where do you want to book tickets? Make my trip, Goibibo, Ease my trip or IRCTC")
            query = takeCommand().lower()
            if "make my trip" in query:
                webbrowser.open_new_tab("https://www.makemytrip.com/bus-tickets/")
            elif "goibibo" in query:
                webbrowser.open_new_tab("https://www.goibibo.com/bus/")
            elif "ease my trip" in query:
                webbrowser.open_new_tab("https://www.easemytrip.com/bus/")
            elif "irctc" in query:
                webbrowser.open_new_tab("https://www.bus.irctc.co.in/home")
            else:
                speak("Mentioned booking source is not available at the moment")

        elif "movie" in query or "movie tickets" in query or "movie ticket" in query:
            print("From where do you want to book tickets? Book my show, Paytm or Ticketnew")
            speak("From where do you want to book tickets? Book my show, Paytm or Ticket new")
            query = takeCommand().lower()
            if "book my show" in query:
                webbrowser.open_new_tab("https://in.bookmyshow.com/explore/movies")
            elif "paytm" in query:
                webbrowser.open_new_tab("https://paytm.com/movies/chandigarh")
            elif "ticket new" in query:
                webbrowser.open_new_tab("https://www.ticketnew.com/")
            else:
                speak("Mentioned booking source is not available at the moment")

    else:
        print("Which tickets do you want to book? Airways, Railways, Roadways(Bus) or Movie tickets")
        speak("Which tickets do you want to book? Airways, Railways, Roadways(Bus) or Movie tickets")
        query = takeCommand().lower()
        if "airways" in query:
            print("From where do you want to book tickets? Makemytrip, Goibibo, Easemytrip or IRCTC")
            speak("From where do you want to book tickets? Make my trip, Goibibo, Ease my trip or IRCTC")
            query = takeCommand().lower()
            if "make my trip" in query:
                webbrowser.open_new_tab("https://www.makemytrip.com/flights/")
            elif "goibibo" in query:
                webbrowser.open_new_tab("https://www.goibibo.com/flights/")
            elif "ease my trip" in query:
                webbrowser.open_new_tab("https://www.easemytrip.com/flights.html")
            elif "irctc" in query:
                webbrowser.open_new_tab("https://www.air.irctc.co.in/")
            else:
                speak("Mentioned booking source is not available at the moment")

        elif "railways" in query:
            print("From where do you want to book tickets? Makemytrip, Goibibo, Easemytrip or IRCTC")
            speak("From where do you want to book tickets? Make my trip, Goibibo, Ease my trip or IRCTC")
            query = takeCommand().lower()
            if "make my trip" in query:
                webbrowser.open_new_tab("https://www.makemytrip.com/railways/")
            elif "goibibo" in query:
                webbrowser.open_new_tab("https://www.goibibo.com/trains/")
            elif "ease my trip" in query:
                webbrowser.open_new_tab("https://www.easemytrip.com/railways/")
            elif "irctc" in query:
                webbrowser.open_new_tab("https://www.irctc.co.in/nget/train-search")
            else:
                speak("Mentioned booking source is not available at the moment")

        elif "roadways" in query or "bus" in query:
            print("From where do you want to book tickets? Makemytrip, Goibibo, Easemytrip or IRCTC")
            speak("From where do you want to book tickets? Make my trip, Goibibo, Ease my trip or IRCTC")
            query = takeCommand().lower()
            if "make my trip" in query:
                webbrowser.open_new_tab("https://www.makemytrip.com/bus-tickets/")
            elif "goibibo" in query:
                webbrowser.open_new_tab("https://www.goibibo.com/bus/")
            elif "ease my trip" in query:
                webbrowser.open_new_tab("https://www.easemytrip.com/bus/")
            elif "irctc" in query:
                webbrowser.open_new_tab("https://www.bus.irctc.co.in/home")
            else:
                speak("Mentioned booking source is not available at the moment")

        elif "movie" in query or "movie ticket" in query or "movie tickets" in query:
            print("From where do you want to book tickets? Book my show, Paytm or Ticketnew")
            speak("From where do you want to book tickets? Book my show, Paytm or Ticket new")
            query = takeCommand().lower()
            if "book my show" in query:
                webbrowser.open_new_tab("https://in.bookmyshow.com/explore/movies")
            elif "paytm" in query:
                webbrowser.open_new_tab("https://paytm.com/movies/chandigarh")
            elif "ticket new" in query:
                webbrowser.open_new_tab("https://www.ticketnew.com/")
            else:
                speak("Mentioned booking source is not available at the moment")
        else:
            speak("Booking can not be forwarded for the same at the moment")


def score(query):
    if "cricket" in query or "football" in query or "hockey" in query or "tennis" in query or "basketball" in query:
        if "cricket" in query:
            webbrowser.open_new_tab("https://www.livescore.com/en/cricket/")
        elif "football" in query or "soccer" in query:
            webbrowser.open_new_tab("https://www.livescore.com/en/")
        elif "hockey" in query:
            webbrowser.open_new_tab("https://www.livescore.com/en/hockey/")
        elif "basketball" in query:
            webbrowser.open_new_tab("https://www.livescore.com/en/basketball/")
        elif "tennis" in query:
            webbrowser.open_new_tab("https://www.livescore.com/en/tennis/")
    else:
        print("Which sports score do you want to know about? Cricket, Football, Hockey, Basketball or Tennis")
        speak("Which sports score do you want to know about? Cricket, Football, Hockey, Basketball or Tennis")
        query = takeCommand().lower()
        if "cricket" in query:
            webbrowser.open_new_tab("https://www.livescore.com/en/cricket/")
        elif "football" in query or "soccer" in query:
            webbrowser.open_new_tab("https://www.livescore.com/en/")
        elif "hockey" in query:
            webbrowser.open_new_tab("https://www.livescore.com/en/hockey/")
        elif "basketball" in query:
            webbrowser.open_new_tab("https://www.livescore.com/en/basketball/")
        elif "tennis" in query:
            webbrowser.open_new_tab("https://www.livescore.com/en/tennis/")
        else:
            speak("Mentioned sport score is not available at the moment")    


def current():
    from datetime import datetime
    from datetime import date
    now = datetime.now()
    today = date.today()
    current_time = now.strftime("%H:%M:%S")
    print(today, current_time)
    speak(today)
    speak(current_time)


def cam():
    import cv2

    cam = cv2.VideoCapture(0)
    cv2.namedWindow("camera")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        cv2.imshow("camera", frame)

        if not ret:
            print("failed to grab frame")
            break
        k = cv2.waitKey(1)
        if k%256 == 27:
            print("Pressed Escape, closing...")
            break
        elif k%256 == 32:
            print("Image"+str(img_counter)+"saved")
            file = 'D://Study//CODE//PYTHON//david//'+str(img_counter)+'.jpg'
            cv2.imwrite(file, frame)
            img_counter += 1

    cam.release()
    cv2.destroyAllWindows()


def note():
    f = open("D://Study//CODE//PYTHON//notes.txt", 'a')
    speak("what should i make note of")
    w = takeCommand().lower()
    f.write(w)
    f.write('\n')
    f.close()
    speak("successfully noted")
    print("Successfully Noted!!")


def fun():
    speak("these are the functionalities that i can perform")
    print("These are the functionalities that I can perform\n")
    print("*| Google Search\n")
    print("*| Provide Wikipedia Content\n")
    print("*| Play on Youtube\n")
    print("*| Open any Application\n")
    print("*| Book Tickets\n")
    print("*| Take a Picture/Selfie\n")
    print("*| Make a Note\n")
    print("*| Conversion\n")
    print("*| Provide Weather Report\n")
    print("*| Provide News\n")
    print("*| Crack Jokes\n")
    print("*| Provide Live Score for Sports\n")
    print("*| Help in Shopping\n")
    print("*| Current Date/Time\n")
    print("*| Text to Speech Converion\n")
    print("*| Stream Movies\n")


#......Main program......
if __name__ == "__main__":
    while True:
        query = takeCommand()

        if query is not None:
            query = query.lower()

        else:
            print("\nSorry, I am unable to process that command")
            print("Can you Repeat it!?")
            continue
        
        if "go to sleep david" in query or "bye" in query or "shutdown" in query or "shut down" in query:
            speak("Ok, Sir, Remember if you need anything just say, wake up david")
            exit()

        elif "what is your name" in query or "name" in query or "who are you" in query or "hi" in query or "hello" in query:
            speak("hello sir! my name is david. am a virtual assistant and would love to assist you for any task specified if it is in my range of capability")

        elif "i am fine" in query or "i am awesome" in query or "i am good" in query :
            speak("I am also good, how may I help you sir?")

        elif "thank you" in query:
            speak("You are welcome sir")

        elif "wikipedia" in query:
            speak("Searching from wikipedia....")
            query = query.replace("wikipedia", "")
            query = query.replace("search wikipedia", "")
            query = query.replace("jarvis", "")
            query = query.replace("short", "")
            searchWikipedia(query)
            continue

        elif "youtube" in query:
            speak("This is what I found for your search!")
            query = query.replace("youtube search", "")
            query = query.replace("youtube", "")
            query = query.replace("jarvis", "")
            searchYoutube(query)

        elif "open" in query or "application" in query:
            query = query.replace("open", "")
            query = query.replace("application", "")
            open_application(query)

        elif "weather" in query or "weather report" in query or "weatherreport" in query:
            weather_report(query)
        
        elif "news" in query or "newsreport" in query or "news report" in query:
            news_report(query)
        
        elif "joke" in query or "jokes" in query:
            joke()

        elif "games" in query or "game" in query:
            game()
        
        elif "shopping" in query or "shop" in query or "buy" in query:           
            shop(query)

        elif "ticket" in query or "tickets" in query:
            book(query)

        elif "convert" in query:
            conv(query)
        
        elif "live" in query or "score" in query:
            score(query)

        elif "current time" in query or "time" in query or "date" in query or "current date" in query:
            current()

        elif "remind" in query or "reminder" in query or "note" in query:
            note()

        elif "movie" in query or "movies" in query:
            mov(query)

        elif "photo" in query or "pic" in query or "picture" in query or "selfie" in query:
            cam()

        elif "what can you do" in query or "functionalities" in query:
            fun()

        elif "google" in query or "search" in query or "tell me about" in query or "summary":
            query = query.replace("david", "")
            query = query.replace("google search", "")
            query = query.replace("google", "")
            searchGoogle(query)

        else:
            searchGoogle(query)
        
        time.sleep(1)
        speak("Do you wish to continue")
        query = takeCommand()

        if query is not None or query == "":
            query = query.lower()
            if "yes" in query:
                continue;
            else:
                speak("Ok, Sir, Remember if you need anything just say, wake up david")
                break
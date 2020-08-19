import speech_recognition as sr
import os
import sys
import re
import webbrowser
import smtplib
import requests
import subprocess
from pyowm import OWM
import youtube_dl
import vlc
import urllib
import json
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import wikipedia
import random
from time import strftime

def martinResponse(audio):
    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)


def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
        command = myCommand();
    return command

def assistant(command):
    if 'open reddit' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        martinResponse('The Reddit content has been opened for you Sir.')

    elif 'open' in command:
        reg_ex = re.search('open (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            print(domain)
            url = 'https://www.' + domain
            webbrowser.open(url)
            martinResponse('The website you have requested has been opened for you Sir.')
        else:
            pass
        

    elif 'email' in command:
        martinResponse('Who is the recipient?')
        recipent = myCommand()

        if 'rajat' in recipent:
            martinResponse('What should I say to him?')
            content = myCommand()
            mail = smtplib.SMTP('smtp.gmail.com',587)
            mail.ehlo()
            mail.starttls()
            mail.login('your_email_address', 'your_password')
            mail.sendmail('sender_email', 'receiver_email', content)
            mail.close()
            martinResponse('Email has been sent successfuly. You can check your inbox.')

        else:
            martinResponse('I don\'t know what you mean!')
    # opens applications for me   
    elif 'launch' in command:
        reg_ex = re.search('launch (.*', command)
        if reg_ex:
            appname = reg_ex.group(1)
            appname1 = appname+".app"
            subprocess.Popen(["open", "-n", "/Applications/" + appname1], stdout=subprocess.PIPE)
            martinResponse('I have launched the desired appication')
    # the weather sis
    elif 'current  weather' in command:
        reg_ex = re.search('current weather in (.*)', command)
        if reg_ex:
            city = reg_ex.group(1)
            owm = OWM(API_key='ab0d5e80e8dafb2cb91fa9e82431c1fa')
            obs = owm.weather_at_place(city)
            w = obs.get_weather()
            k = w.get_status()
            x = w.get_temperature(unit='celsius')
            martinResponse('Current weather in %s is %s. The maximum temperature is %0.3f and the minumum temperature is %0.3f degree celsius' %(city, k, x['temp_max'], x['temp_min']))
    # time bro
    elif 'time' in command:
        import datetime
        now = datetime.datetime.now()
        martinResponse('Current time is %d hours %d minutes' %(now.hour, now.minute))

    # Greet martin
    elif 'hello' in command:
        day_time = int(strftime('%H'))
        if day_time < 12:
            martinResponse('Hello Sir. Good morning')
        elif 12 <= day_time <18:
            martinResponse('Hello Sir. Good afternoon')
        else:
            martinResponse('Hello Sir. Good evening')

    # to terminate the program
    elif 'shutdown' in command:
        martinResponse('Bye bye Sir. Have a nice day')
        sys.exit()

    # play me a song

    elif 'play me a song' in command:
        path = '/Users/user/Movies/'
        folder = path
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print (e)
                    
        martinResponse('What song shall I play Sir?')
        mysong = myCommand()
        if mysong:
            flag = 0
            url = "https://www.youtube.com/results?search_query" + mysong.replace(' ','+')
            response = urllib.urlopen(url)
            html = response.read()
            soup1 = soup(html,"lxml")
            url_list = []
            for vid in soup1.findAll(attrs={'class':'yt-uix-tile-link'}):
                if ('https://www.youtube.com' + vid['href']).startswith("https://www.youtube.com/watch?v="):
                    flag = 1
                    final_url = 'https://www.youtube.com' + vid['href']
                    url_list.append(final_url)
                    url = url_list[0]
                    ydl_opts = {}
                    os.chdir(path)
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])
                    vlc.play(path)

        if flag==0:
            martinResponse('I have not found anything in Youtube')
    #martin changes my wallpaper

    elif 'change wallpaper' in command:
        folder = '/User/user/Documents/walllpaper'
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)
            API_key = 'fd66364c0ad9e0f8aabe54ec3cfbed0a947f3f4014ce3b841bf2ff6e20948795'
            url = 'https://api.unsplash.com/photos/random?client_id=' + API_key
            f = urllib.urlopen(url)
            json_string = f.read()
            f.close()
            parsed_json = json.loads(json_string)
            photo = parsed_json['urls']['full']
            urllib.urlretrieve(photo,"/Users/user/Documents/wallpaper/")
            subprocess.call(["killall Dock"], shell=True)
            martinResponse('wallpaper changed successfully')

    #news
    elif 'news for today' in command:
        try:
            news_url="https://news.google.com/news/rss"
            Client = urlopen(news_url)
            xml_page = Client.read()
            Client.close()
            soup_page = soup(xml_page, "xml")
            news_list = soup_page.findAll("item")
            for news in news_list[:15]:
                martinResponse(news.title.text.encode('utf-8'))
        except Exception as e:
                print(e)
    #about anything
    elif 'tell me about' in command:
        reg_ex = re.search('tell me about (.*)', command)
        try:
            if reg_ex:
                topic = reg_ex.group(1)
                ny = wikipedia.page(topic)
                martinResponse(ny.content[:500].encode('utf=8'))
        except Exception as e:
            martinResponse(e)
martinResponse('Hi User, I am Martin and I am your personal voice assistant, Please give a command or say "help me" and I will tell you what all I can do for you.')

#loop to continue executing multiple commands
while True:
    assistant(myCommand())
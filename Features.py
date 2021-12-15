import Main

def introduction():
    Main.speak("hello sir , i am adux your new appointed virtual assistant , i am here to assist you with some of your work sir")

def browser():
    Main.speak("what would you like to search , sir")
    query = Main.TakeCommand()
    
    if 'google search ' in query:
        Main.speak("searching in google for your quaries , sir")
        query = query.replace("adux","")
        query = query.replace("google search","")
        query = query.replace("search","")
        try:
            Main.pywhatkit.search(query)
            result = Main.googleScrap.summary(query,2)
            Main.speak(result)

        except:
            Main.speak("no speakable data available")

    elif 'youtube search' in query:
        Main.speak("searching in youtube")
        query = query.replace("youtube search" ,"")
        result = "https://www.youtube.com/results?search_query=" + query
        Main.web.open(result)
        Main.speak("results found")
        Main.speak("playing first result")
        Main.pywhatkit.playonyt(query) 

def wishMe():
    hour = int(Main.datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Main.speak("Good Morning, sir")
    elif hour>=12 and hour<16:
        Main.speak("Good Afternoon , sir")
    else:
        Main.speak("Good Evening, sir")            

def TimeTeller():
    strTime = Main.datetime.datetime.now().strftime("%H:%M:%S")
    Main.speak(f"sir,the time is {strTime}")    

def playMusic():
    music_dir = 'D:\\Rahul Files\\code\\MyAssistant\\Music'
    songs = Main.os.listdir(music_dir)
    print(songs)
    Main.os.startfile(Main.os.path.join(music_dir, songs[0]))

def openApps():
    
    Main.speak("you can choose from the apps to open")
    print("vs code")

    whichapp = Main.TakeCommand()
    if 'vs code ' in whichapp:
        codePath = '"C:\\Users\\raira\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"' 
        Main.os.startfile(codePath)            


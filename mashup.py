#Importation of module libraries in the project
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia


#Listening function of the command given by the user
listener = sr.Recognizer()

#initializing the robot in my case i nemed it Josh
josh = pyttsx3.init()

# Sets speed the robot is going to talk
josh.setProperty('rate', 145)

# Set volume of the robot talking ranging between 0-1
josh.setProperty('volume', 0.9)
  
#I changed the voice to sound that of a a lady in this part
voices = josh.getProperty('voices')
josh.setProperty('voice', voices[1].id)

#Defination to make our robot talk the commands given by the user after they are transalted to text by google
def talk(text):
    josh.say(text)
    josh.runAndWait()
    

#Function to store the listener from the microphone and give it a global name command
def listen():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if 'Josh' in command:
                command = command.replace('Josh', '')	
               
               
    

    except:
        pass

    return command

#Calling a value from a function with the intent of using it in a different function
var = listen


#This is the command execution bay where all command will be heard by the robot josh and will be executed in a else if block
def run_josh():
    
    #Called value from the other function to this fucntion is initialized in this phase
    command = var()
    
    #Function to play a song on youtube
    song = command.replace('play', '')
    print(command)
    if 'play' in command:
        talk('playing' + song)
        pywhatkit.playonyt(song)
    
      #Function to ask for the current time  
    elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is' + time)
    
      #Function to google something on the web        
    elif 'google' in command:
                query  = command.replace('search', '')
                result = wikipedia. summary (query, 3)
                talk(result)
            
     #Function to ask for the current date         
    elif 'date' in command:
            date = datetime.datetime.now().strftime('%A:%d:%B:%Y')
            talk('Today is on' + date )
            
      #Function to end the talk with josh
    elif 'terminate' in command:
        talk('Thank you for your time. Take Care of yourselve')
        exit()
        
      #Function for Josh asking you to repeat pardon the commands you give
    else:
		    talk('Kindly, I beg your pardon...')

  #Function to loop the whole process to continue talking to Josh
while True:
    run_josh()
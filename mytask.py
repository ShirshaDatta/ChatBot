import pyttsx3
import os
import pyaudio
import speech_recognition as sr
import datetime

r=sr.Recognizer()
r.energy_threshold=4000

hour = int(datetime.datetime.now().hour)
if hour>=0 and hour < 12:
	pyttsx3.speak("Good Morning Ma'am")
elif hour>=12 and hour < 18:
	pyttsx3.speak("Good afternoon Ma'am")
else:
	pyttsx3.speak("Good evening Ma'am")

while True:
	pyttsx3.speak("Which file do you want to open?")
	#n = input()
	with sr.Microphone() as source:
   		audio=r.listen(source)

	try:
		response = r.recognize_google(audio)
		if (("Social Media" in response) or ("social media" in response) or ("Social media" in response)):
			print("Enter the choice you are comfortable with")
			print("Press 1: to open Facebook")
			print("Press 2: to open LinkedIn")
			choice=input()
			if int(choice)==1:
				pyttsx3.speak("Opening Facebook...")
				os.system("chrome facebook.com")
			elif int(choice)==2:
				pyttsx3.speak("Opening LinkedIn...")
				os.system("chrome linkedin.com")
			else:
				pyttsx3.speak("Invalid option!")
				continue

		elif (("Music" in response) or ("music" in response)):
			print("Enter the choice you are comfortable with")
			print("Press 1: to open wmplayer")
			print("Press 2: to open spotify")
			choice0=input()
			if int(choice0)==1:
				pyttsx3.speak("Opening Windows Media Player...")
				os.system("wmplayer")
			elif int(choice0)==2:
				pyttsx3.speak("Opening Spotify...")
				os.system("chrome spotify.com")
		
			else:
				pyttsx3.speak("Invalid option!")
				continue

	
		elif (("entertainment" in response) or ("Entertainment" in response)):
			print("Enter the choice you are comfortable with")
			print("Press 1: to open Netflix")
			print("Press 2: to open Prime Video")
			print("Press 3: to open Hotsar")
			print("Press 4: to open Youtube")     
			choice1=input()
		

			if int(choice1)==1:
				pyttsx3.speak("Opening netflix...")
				os.system("chrome netflix.com")

			elif int(choice1)==2:
				pyttsx3.speak("Opening prime video...")
				os.system("chrome primevideo.com")

			elif int(choice1)==3:
				pyttsx3.speak("Opening hotstar...")
				os.system("chrome hotstar.com")
		
			elif int(choice1)==4:
				pyttsx3.speak("Opening youtube...")
				os.system("chrome youtube.com")

			else:
				pyttsx3.speak("Invalid option!")
				continue
		
		
		elif (("Text Editor" in response) or ("text editor" in response) or ("Text editor" in response)):
			print("Enter the choice you are comfortable with")
			print("Press 1: to open Notepad")
			print("Press 2: to open Word")
			choice2=input()
			if int(choice2)==1:
				pyttsx3.speak("Opening Notepad...")
				os.system("notepad")
			elif int(choice2)==2:
				pyttsx3.speak("Opening Word...")
				os.system("word")
			else:
				pyttsx3.speak("Invalid option!")
				continue


		elif (("quit" in response) or ("Quit" in response) or ("exit" in response) or ("Exit" in response) or ("close" in response)):
			break
        
	
	except Exception as e:
		pyttsx3.speak('Speech not understood')
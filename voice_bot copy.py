
import speech_recognition as sr
import webbrowser
import datetime
import time, random
import os, sys, subprocess

botData = "botData.txt"

def readLine(line_number, filename=botData):
  with open(filename, 'r') as f:
    for i, line in enumerate(f):
      if i == line_number - 1:
        return line.strip()
def writeLine(line_number, new_text, filename=botData):
  lines = []
  with open(filename, 'r') as f:
    for i, line in enumerate(f):
      if i == line_number - 1:
        lines.append(new_text + '\n')
      else:
        lines.append(line)

  with open(filename, 'w') as f:
    f.writelines(lines)
def restartProgram():
    try:
        python = sys.executable
        script_path = os.path.abspath(sys.argv[0])
        if not os.path.isfile(script_path):
            raise FileNotFoundError(f"Script not found at {script_path}")
        subprocess.call([python, script_path] + sys.argv[1:])
        sys.exit()  # Exit the current script after restart
    except Exception as e:
        print(f"Error restarting the program: {e}")
def say(text):
    os.system(f'powershell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\');"')
    # os.system(f'say "{text}"')
def takeCommand():
    try:
        # r = sr.Recognizer()
        # command = input("Call Jarvis: ")
        # with sr.Microphone() as source:
        #     # r.pause_threshold =  0.6
        #     audio = r.listen(source,timeout=5)
        #     print("Recognizing...")
        #     command = r.recognize_google(audio, language="en-in")
        #     command = command.lower()
        #     print(f"User said: {command}")
        # if (command == botName.lower()):
        if True:
            # say(f"Yes")
            command = input("Enter command: ")
            # with sr.Microphone() as source:
            #     # r.pause_threshold =  0.6
            #     audio = r.listen(source,timeout=5)
            #     print("Recognizing...")
            #     command = r.recognize_google(audio, language="en-in")
            #     command = command.lower()
            print(f"User said: {command}")
            return command
    except sr.WaitTimeoutError:
        takeCommand()
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Error:{e}")

def processTask(command):
    print("Processing command")
    try:
        global botName
        sites = [
                ["youtube", "https://youtube.com"],
                ["google", "https://google.com"],
                ["instagram", "https://instagram.com"],
                ["facebook", "https://facebook.com"],
                ["whatsapp", "https://web.whatsapp.com"],
                ["wikipedia", "https://wikipedia.org"],
                ["drive", "https://drive.google.com"],
                ["gmail", "https://mail.google.com"],
                ["chatgpt", "https://chatgpt.com"],
                ["spotify", "https://open.spotify.com"],
                ["gemini", "https://gemini.google.com"],
                ["google docs", "https://docs.google.com"],
                ["spreadsheet", "https://docs.google.com/spreadsheets"],
                ["google keep", "https://keep.google.com"],
                ["presentation", "https://docs.google.com/presentation"]
                ]
        if "play music" in command:
            music_path = r"C:\Users\three\Nathan\Coding\Python\PythonCodeEnv\MegaProject"
            os.startfile(music_path)
            print("Playing Music")
        elif "change bot name" in command:
            say("what should I name the bot.")
            command = takeCommand()
            writeLine(1, command)
            botName = readLine(1)
            say(f"Your bot is named {botName}")
            print(f"Your bot is named {botName}")
        elif "open" in command:
            for site in sites:
                if f"open {site[0]}".lower() in command:
                    say(f"Opening {site[0]}")
                    webbrowser.open(site[1])
        else:
            print("Didn't do any task") 
    except sr.UnknownValueError:
        say("Could not understand audio, Repeat again")

def main():
    try:
        botName = readLine(1).lower()
        say(f"Intializing {botName}")
        while True:
            command = takeCommand()
            processTask(command)
    except KeyboardInterrupt:
        restartProgram()

if __name__ == "__main__":
    main()
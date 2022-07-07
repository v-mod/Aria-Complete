import pyttsx3
def speak(text):
    engine=pyttsx3.init('sapi5')
    engine.setProperty('voice','voices[0].id')
    engine.say(text)
    engine.runAndWait()
while True:
    tos=input('Speak:? ')
    if '-f' not in tos:
        speak(tos)
    elif '-f' in tos:
        while True:
            speak(tos.split('-')[0])
    else:
        print('An unkown error occured. Please try again later.')
        speak('An unkown error occured. Please try again later.')
        quit()
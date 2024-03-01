#speech recognise
import speech_recognition as sr


srs=sr.Recognizer()
print("computer is listening....")



with sr.Microphone() as m:
    audio=srs.listen(m)
    query=srs.recognize_google(audio, language='en-IN')
    print("audio-",query)
    
    



#save to file
with open("query.txt","w") as file:
    file.write(query)
    print("task finished")

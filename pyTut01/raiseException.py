# a = input("What is is your name")
# b = input("How much do you earn")
#
# if int(b)==0:
#     raise ZeroDivisionError("B is 0 so  stopping")
#
# if a.isnumeric():
#     raise Exception("Numbers are not allowed")
# print(f"Hello {a}")
#
# #1000 lines taking 1 hour

# c = input("Enter your name")
# try:
#     print(a)
# except Exception as e:
#     if c == "harry":
#         raise ValueError("harry is blocked he is not allowed")
#     print("Exception handled")
#
# == - value equality - Two objecrs have the same value
# is - reference equality - Two references refer to the same object

import requests
import json

def speak(msg):
    from win32com.client import Dispatch
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(msg)
    print("b")


if __name__ == '__main__':
    speak("News for to day")
    url ="https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=5ec40c3e0e9c4098872bcee91fbc1c55"
    news = requests.get(url).text
    news_dict = json.loads(news)
    print(news_dict["articles"])
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        speak("Moving on to the next news..Listen Carefully")

# Akhbaar padhke sunao
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("Hey pk sona, sona pk")

# import json
# data = '{"var1":"harry","var2":56}'
# parsed = json.loads(data)
# print(type(parsed))
# print(parsed)
# print(parsed['var1']

# data2 = {
#     "chakkel_name": "CodeWithHatty",
#     "cars":['bmw','audi a8','ferrari'],
#     "fridge":('roti',540),
#     "isbad":False
# }

# jscomp  = json.dumps(data2)
# print(jscomp)

import pickle
# Pickling a python object
# cars = ["Audi","BMW","Maruti Suzuki","Harryti Tuzuki"]
# file = "mycar.pkl"
# fileobj = open(file,'wb')
# pickle.dump(cars,fileobj)
# fileobj.close()

file  = "mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))

# picling iris
# use requests module to download the iris dataset
# -*- coding: utf-8 -*-
"""text_to_speech_using_python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IdTu9eL74bIIq1jXyzlgLqW69I0cbwxn
"""

#pip install pyttsx3

import pyttsx3

text_to_speech =  pyttsx3.init()
data = input("Enter text which you want to convert into speech: \n")
text_to_speech.say(data)
text_to_speech.runAndWait()


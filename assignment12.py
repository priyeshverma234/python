# Q.1 Print the current day using Datetime module:-
import datetime as dt
y=dt.date.today()
print(y.strftime("%A"))


# Q.2 Open your browser and play a video using webbrowser module in python:-
import webbrowser
search = "sickick infected"
webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % search)


# Q.3 Write a program to rename all the files in a directory and convert them into .jpg file format:-
import os
os.rename('abc.txt','abc.jpg')

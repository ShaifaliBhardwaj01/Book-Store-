# Book-Store-
App- GUI Apps & SQL : Build a book Inventory Desktop GUI Database App
Book Store Desktop aaplication with .exe & .app File.
Python Book store Tkinter Ptoject
Hey ,

So the topic is -->
                                        App- GUI Apps & SQL : Build a book Inventory Desktop GUI Database App
                                        
                                        
                                        
Note1_ Steps to create an .exe and .app executables from Python script -      
   1) run this command to install pyinstaller using pip - pip install pyinstaller
   2) to create .exe file for windows, go to your project location & run  this commamd - pyinstaller --onefile --windowed frontend.py
   Now you have an .exe file for windows & .app file for ios..
   
   


so using Python and we get the program displayed, but think if you want to

give your program to someone else, you can just tell them install Python and

you can execute the program by going to the terminal and invoking platform and

the script, so that may get terribly difficult for users who are not

experienced with programming so in that case you want to make a standalone

executable program that you can just send to anyone and they can just double click

it and go ahead and insert data and retrieve data and so on. So in this

lecture I'll show you how to make an executable file and you'll make that file

whether you are on a Mac, or Windows, or Linux so the code is the same.

There exists a great library to make standalone executables. That is the

pyinstaller, so you can install pyinstaller using pip.

And now it's terribly easy to make a standalone executable file out of your

Python scripts. All you have to do is call pyinstaller, and then point to your

script, so in this case our main script is frontend.py, so that's the script

that is holding all the code and it also imports the backend script,

so we want to point to that file, and if you leave it like this, you'll get a dot exe file

if you are on Windows, a dot app file if you are on a Mac, and together with

those files you will also get a bunch of other files that are associated with

your program. The benefit of that is that it gets easier to troubleshoot any

errors that you may get, so you have lots of files and then you can go to

those files and find the error, and so on. But if you want to be practical you'd

want to pass a parameter here called onefile. So that will create a single

executable file for you, and in this form you will also get a terminal, a command

line displayed on the background of your graphical user interface,

so if you don't want that you can specify another parameter called

windowed, so like that and execute. You'll have to wait a while and my

executable was created, so if you we're on a Mac this would be a dot app file,

so mine is here the dist folder, so in this folder, I can look up here. So frontend.exe.

If you execute that you'll get the window and as you see you also got the

books.db file generated so by default this only creates executable files,

and then when you execute the program for first time, remember that we had

the connect function in the back-end script so that function creates

a database. So that's what this did and if you view

all now you don't have any rows, so you don't have any data because this was

created from scratch.Sso in case you want to have the existing database, you'd want

to give to your user both the executable file and the existing

database that you have.

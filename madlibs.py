#Jax Powell
#madlibs python using tkinter 

from tkinter import *
from functools import partial
import tkinter as tk

def madlibs():

	def validateDone(pluralNoun, adjective, verb, partofthebody, partofthebody2, verb2, adjective2, adjective3, verb3):
		first = 'Many people have swimming '
		second = ' in their\nbackyeards and learn to swim at a very '
		third = ' age.\nLearning to swim is easier than learning to '
		forth = '\nFirst, you lay flat on your '
		fith = ', then you practive kicking your '
		sixth = " untill you're able to "
		seventh = '\nacross the pool. if you work hard, in no time at all, you can master\nthe '
		eighth = ' crawl, the '
		ninth = ' stroke, and in no time you \ncan even '
		tenth = ' underwater.'
		
		madlib = Label(text=first + pluralNoun.get() + second + adjective.get() + third + verb.get() + forth + partofthebody.get() + fith + partofthebody2.get() + sixth + verb2.get() + seventh + adjective2.get() + eighth + adjective3.get() + ninth + verb3.get() + tenth, font='Verdana 12').place(relx=0.5, rely=0.5, anchor=CENTER)

		return madlib

	#window
	root = Tk()  
	root.geometry('800x800')  
	root.title('madlibs')

	#pluralNoun
	pluralNounLabel = Label(root, text="Plural Noun").grid(row=0, column=2, padx=(250, 10), pady=5)
	pluralNoun = StringVar()
	pluralNounEntry = Entry(root, textvariable=pluralNoun).grid(row=0, column=3)  

	#adjective
	adjectiveLabel = Label(root,text="Adjective").grid(row=1, column=2, padx=(250, 10), pady=5)  
	adjective = StringVar()
	adjectiveEntry = Entry(root, textvariable=adjective).grid(row=1, column=3)  

	#verb
	verbLabel = Label(root,text="Verb").grid(row=2, column=2, padx=(250, 10), pady=5)  
	verb = StringVar()
	verbEntry = Entry(root, textvariable=verb).grid(row=2, column=3) 

	#Part of the body
	partofthebodyLabel = Label(root,text="part of the body (singular)").grid(row=3, column=2, padx=(250, 10), pady=5)  
	partofthebody = StringVar()
	partofthebodyEntry = Entry(root, textvariable=partofthebody).grid(row=3, column=3)

	#Part of the body (plural)
	partofthebody2Label = Label(root,text="Part of the body (plural)").grid(row=4, column=2, padx=(250, 10), pady=5)  
	partofthebody2 = StringVar()
	partofthebody2Entry = Entry(root, textvariable=partofthebody2).grid(row=4, column=3)

	#verb2
	verb2Label = Label(root,text="Verb").grid(row=5, column=2, padx=(250, 10), pady=5)
	verb2 = StringVar()
	verb2Entry = Entry(root, textvariable=verb2).grid(row=5, column=3)

	#adjective2
	adjective2Label = Label(root,text="Adjective").grid(row=6, column=2, padx=(250, 10), pady=5)  
	adjective2 = StringVar()
	adjective2Entry = Entry(root, textvariable=adjective2).grid(row=6, column=3)

	#adjective3
	adjective3Label = Label(root,text="Adjective").grid(row=7, column=2, padx=(250, 10), pady=5)  
	adjective3 = StringVar()
	adjective3Entry = Entry(root, textvariable=adjective3).grid(row=7, column=3)

	#verb3
	verb3Label = Label(root,text="Verb").grid(row=5, column=2, padx=(250, 10), pady=5)  
	verb3 = StringVar()
	verb3Entry = Entry(root, textvariable=verb3).grid(row=5, column=3)


	validateDone = partial(validateDone, pluralNoun, adjective, verb, partofthebody, partofthebody2, verb2, adjective2, adjective3, verb3)

	#done button
	doneButton = Button(root, text="Done", command=validateDone).grid(row=10, column=3, pady=5)  


	root.mainloop()
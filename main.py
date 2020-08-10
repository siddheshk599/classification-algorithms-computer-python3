from tkinter import Tk, Toplevel, RAISED, Button, Label, messagebox, Entry, PhotoImage, Radiobutton, StringVar ,INSERT, scrolledtext
import functions, pprint, io, contextlib

#Functions
def openWindow(windowName):
	mainWindow.withdraw()
	if (windowName == "infoMsgBox"):
		mainWindow.deiconify()
		messagebox.showinfo("Info about this software", "Developer: Siddhesh Sudhir Kudtarkar.\n\nAim of this software: To compare the performances of 2 Data Mining Classification algorithms - Naive Bayes & ID3 Decision Tree.")
	elif (windowName == "configureDbWindow"):
		configureDbWindow.deiconify()
		if (functions.savedDbConnection == True):
			entUsername.insert(0, functions.dbDetails['username'])
			entPassword.insert(0, functions.dbDetails['password'])
			entHostName.insert(0, functions.dbDetails['hostName'])
			entDbName.insert(0, functions.dbDetails['dbName'])
			entDbTableName.insert(0, functions.dbDetails['dbTableName'])
			entUsername.focus()
	elif (windowName == "viewDbDataWindow"):
		if (functions.savedDbConnection != True):
			mainWindow.deiconify()
			messagebox.showerror("Database not configured", "Configure the database first by adding database credentials.")
		else:
			viewDbDataWindow.deiconify()
	elif (windowName == "selectAlgoWindow"):
		if (functions.savedDbConnection != True):
			mainWindow.deiconify()
			messagebox.showerror("Database not configured", "Configure the database by adding database credentials.")
		else:
			selectAlgoWindow.deiconify()
		
def backFunction(action):
	mainWindow.deiconify()
	if (action == "backFromConfigureDb"):
		configureDbWindow.withdraw()
	elif (action == "backFromViewDbData"):
		viewDbDataWindow.withdraw()
	elif (action == "backFromSelectAlgo"):
		selectAlgoWindow.withdraw()
	elif (action == "backFromNaiveBayesResult"):
		mainWindow.withdraw()
		naiveBayesResultWindow.withdraw()
		selectAlgoWindow.deiconify()
	elif (action == "backFromId3Result"):
		mainWindow.withdraw()
		id3ResultWindow.withdraw()
		selectAlgoWindow.deiconify()

def algorithmSelect():
	algoName = rbValue.get()
	if (algoName == "naiveBayes"):
		entNaiveBayesColumnNames.configure(state="normal")
		entNaiveBayesTuple.configure(state="normal")
		entNaiveBayesClassName.configure(state="normal")
		entId3ColumnNames.configure(state="disabled")
		entNaiveBayesColumnNames.focus()
	elif (algoName == "id3"):
		entNaiveBayesColumnNames.configure(state="disabled")
		entNaiveBayesTuple.configure(state="disabled")
		entNaiveBayesClassName.configure(state="disabled")
		entId3ColumnNames.configure(state="normal")
		entId3ColumnNames.focus()

def runAlgorithm():
	algoName = rbValue.get()
	msg = ""
	if (algoName == "naiveBayes"):
		try:
			msg = functions.naiveBayes(entNaiveBayesTuple.get(), entNaiveBayesColumnNames.get(), entNaiveBayesClassName.get())
			stxtNaiveBayesResult.insert(INSERT, msg)
			naiveBayesResultWindow.deiconify()
		except Exception as e:
			messagebox.showerror("Error", e)
	elif (algoName == "id3"):
		try:
			tree = functions.id3(entId3ColumnNames.get())
			file = io.StringIO()
			with contextlib.redirect_stdout(file):
				pprint.pprint(tree)
			stxtId3Result.insert(INSERT, file.getvalue())
			id3ResultWindow.deiconify()
		except Exception as e:
			messagebox.showerror("Error", e)

#Main Window
mainWindow = Tk()
mainWindow.title("Classification Algorithms Computer GUI")
mainWindow.geometry("400x350+480+150")
mainWindow.configure(background="Light Blue")

rbValue = StringVar()
rbValue.set("naiveBayes")
windowIcon = PhotoImage(file="icon.png")
mainWindow.iconphoto(False, windowIcon)

btnSelect = Button(mainWindow, text="Select algorithm", font=("Arial", 14, "bold"), width=22, background="Light Yellow", activebackground="Green", activeforeground="White", relief=RAISED, command=lambda:openWindow('selectAlgoWindow'))
btnSelect.pack(pady=10)

btnConfigureDb = Button(mainWindow, text="Configure Database", font=("Arial", 14, "bold"), width=22, background="Light Yellow", activebackground="Green", activeforeground="White", relief=RAISED, command=lambda:openWindow('configureDbWindow'))
btnConfigureDb.pack(pady=10)

btnViewDbData = Button(mainWindow, text="View Database Data", font=("Arial", 14, "bold"), width=22, background="Light Yellow", activebackground="Green", activeforeground="White", relief=RAISED, command=lambda:openWindow('viewDbDataWindow'))
btnViewDbData.pack(pady=10)

btnInfo = Button(mainWindow, text="Info", font=("Arial", 14, "bold"), width=22, background="Light Yellow", activebackground="Green", activeforeground="White", relief=RAISED, command=lambda:openWindow('infoMsgBox'))
btnInfo.pack(pady=10)

btnExit = Button(mainWindow, text="Exit", font=("Arial", 14, "bold"), width=22, background="Light Yellow", activebackground="Green", activeforeground="White", relief=RAISED, command=lambda:functions.exitFunction(mainWindow))
btnExit.pack(pady=10)

functions.getSavedDbDetails()

#ConfigureDb Window
configureDbWindow = Toplevel(mainWindow)
configureDbWindow.withdraw()
configureDbWindow.title("Configure Database Details")
configureDbWindow.geometry("500x580+380+100")
configureDbWindow.configure(background="Light Blue")
configureDbWindow.iconphoto(False, windowIcon)

lblUsername = Label(configureDbWindow, text="Enter the username: ", font=("Arial", 14, "bold"), width=28, background="Light Blue")
lblUsername.pack(pady=10)

entUsername = Entry(configureDbWindow, font=("Arial", 14, "bold"), width=35)
entUsername.pack(pady=10)

lblPassword = Label(configureDbWindow, text="Enter the password: ", font=("Arial", 14, "bold"), width=28, background="Light Blue")
lblPassword.pack(pady=10)

entPassword = Entry(configureDbWindow, font=("Arial", 14, "bold"), width=35, show="*")
entPassword.pack(pady=10)

lblHostName = Label(configureDbWindow, text="Enter the host name: ", font=("Arial", 14, "bold"), width=28, background="Light Blue")
lblHostName.pack(pady=10)

entHostName = Entry(configureDbWindow, font=("Arial", 14, "bold"), width=35)
entHostName.pack(pady=10)

lblDbName = Label(configureDbWindow, text="Enter the database name: ", font=("Arial", 14, "bold"), width=28, background="Light Blue")
lblDbName.pack(pady=10)

entDbName = Entry(configureDbWindow, font=("Arial", 14, "bold"), width=35)
entDbName.pack(pady=10)

lblDbTableName = Label(configureDbWindow, text="Enter the database table name: ", font=("Arial", 14, "bold"), width=28, background="Light Blue")
lblDbTableName.pack(pady=10)

entDbTableName = Entry(configureDbWindow, font=("Arial", 14, "bold"), width=35)
entDbTableName.pack(pady=10)

btnSaveDbDetails = Button(configureDbWindow, text="Save Details", font=("Arial", 14, "bold"), width=34, background="Light Yellow", activebackground="Green", activeforeground="White", relief=RAISED, command=lambda:functions.saveDbDetails(entUsername.get(), entPassword.get(), entDbName.get(), entDbTableName.get(), entHostName.get()))
btnSaveDbDetails.pack(pady=10)

btnBackConfigureDb = Button(configureDbWindow, text="Back", font=("Arial", 14, "bold"), width=34, background="Light Yellow", activebackground="Green", activeforeground="White", relief=RAISED, command=lambda:backFunction('backFromConfigureDb'))
btnBackConfigureDb.pack(pady=10)

#View Database data
viewDbDataWindow = Toplevel(mainWindow)
viewDbDataWindow.title("View Database Data")
viewDbDataWindow.geometry("1366x768+0+0")
viewDbDataWindow.configure(background="Light Blue")
viewDbDataWindow.iconphoto(False, windowIcon)

stxtDbData = scrolledtext.ScrolledText(viewDbDataWindow, width=160, height=35)
stxtDbData.pack(pady=10)

if (functions.savedDbConnection):
	msg = functions.getDbData()
	stxtDbData.insert(INSERT, msg)
	stxtDbData.configure(state="disabled")

btnBackViewDbData = Button(viewDbDataWindow, text="Back", font=("Arial", 14, "bold"), width=22, background="Light Yellow", activebackground="Green", activeforeground="White", relief=RAISED, command=lambda:backFunction('backFromViewDbData'))
btnBackViewDbData.pack(pady=10)

viewDbDataWindow.withdraw()

#Select Algorithm window
selectAlgoWindow = Toplevel(mainWindow)
selectAlgoWindow.withdraw()
selectAlgoWindow.title("Select classification algorithm")
selectAlgoWindow.geometry("500x580+380+100")
selectAlgoWindow.configure(background="Light Blue")
selectAlgoWindow.iconphoto(False, windowIcon)

rbNaiveBayes = Radiobutton(selectAlgoWindow, text="Naive Bayes classification algorithm", background="Light Blue", font=("Arial", 14, "bold"), command=algorithmSelect, variable=rbValue, value="naiveBayes", activebackground="Green", activeforeground="White")
rbNaiveBayes.pack(pady=10)

lblNaiveBayesColumnNames = Label(selectAlgoWindow, text="Enter the column names to be considered (seperated by ','):", font=("Arial", 12, "bold"), background="Light Blue")
lblNaiveBayesColumnNames.pack(pady=10)

entNaiveBayesColumnNames = Entry(selectAlgoWindow, font=("Arial", 14, "bold"), width=35, state="disabled")
entNaiveBayesColumnNames.pack(pady=10)

lblNaiveBayesTuple = Label(selectAlgoWindow, text="Enter the tuple to be classified (seperated by ','):", font=("Arial", 12, "bold"), background="Light Blue")
lblNaiveBayesTuple.pack(pady=10)

entNaiveBayesTuple = Entry(selectAlgoWindow, font=("Arial", 14, "bold"), width=35, state="disabled")
entNaiveBayesTuple.pack(pady=10)

lblNaiveBayesClassName = Label(selectAlgoWindow, text="Enter the name of the target class:", font=("Arial", 12, "bold"), background="Light Blue")
lblNaiveBayesClassName.pack(pady=10)

entNaiveBayesClassName = Entry(selectAlgoWindow, font=("Arial", 14, "bold"), width=35, state="disabled")
entNaiveBayesClassName.pack(pady=10)

rbId3 = Radiobutton(selectAlgoWindow, text="ID3 Decision Tree algorithm", background="Light Blue", font=("Arial", 14, "bold"), command=algorithmSelect, variable=rbValue, value="id3", activebackground="Green", activeforeground="White")
rbId3.pack(pady=10)

lblId3ColumnNames = Label(selectAlgoWindow, text="Enter the column names to be considered (seperated by ','):", font=("Arial", 12, "bold"), background="Light Blue")
lblId3ColumnNames.pack(pady=10)

entId3ColumnNames = Entry(selectAlgoWindow, font=("Arial", 14, "bold"), width=35, state="disabled")
entId3ColumnNames.pack(pady=10)

btnStart = Button(selectAlgoWindow, text="Start", font=("Arial", 14, "bold"), width=34, background="Light Yellow", activebackground="Green", activeforeground="White", relief=RAISED, command=runAlgorithm)
btnStart.pack(pady=10)

btnBackSelectAlgoWindow = Button(selectAlgoWindow, text="Back", font=("Arial", 14, "bold"), width=34, background="Light Yellow", activebackground="Green", activeforeground="White", relief=RAISED, command=lambda:backFunction('backFromSelectAlgo'))
btnBackSelectAlgoWindow.pack(pady=10)

#Naive Bayes Result Window
naiveBayesResultWindow = Toplevel(mainWindow)
naiveBayesResultWindow.title("Result of Naive Bayes Classification Algorithm")
naiveBayesResultWindow.geometry("1366x768+0+0")
naiveBayesResultWindow.configure(background="Light Blue")
naiveBayesResultWindow.iconphoto(False, windowIcon)

stxtNaiveBayesResult = scrolledtext.ScrolledText(naiveBayesResultWindow, width=160, height=35)
stxtNaiveBayesResult.pack(pady=10)

btnBackNaiveBayesResult = Button(naiveBayesResultWindow, text="Back", font=("Arial", 14, "bold"), width=22, background="Light Yellow", activebackground="Green", activeforeground="White", relief=RAISED, command=lambda:backFunction('backFromNaiveBayesResult'))
btnBackNaiveBayesResult.pack(pady=10)

naiveBayesResultWindow.withdraw()

#ID3 Result Window
id3ResultWindow = Toplevel(mainWindow)
id3ResultWindow.title("Result of ID3 Decision Tree algorithm")
id3ResultWindow.geometry("1366x768+0+0")
id3ResultWindow.configure(background="Light Blue")
id3ResultWindow.iconphoto(False, windowIcon)

stxtId3Result = scrolledtext.ScrolledText(id3ResultWindow, width=160, height=35)
stxtId3Result.pack(pady=10)

btnBackId3Result = Button(id3ResultWindow, text="Back", font=("Arial", 14, "bold"), width=22, background="Light Yellow", activebackground="Green", activeforeground="White", relief=RAISED, command=lambda:backFunction('backFromId3Result'))
btnBackId3Result.pack(pady=10)

id3ResultWindow.withdraw()

mainWindow.mainloop()
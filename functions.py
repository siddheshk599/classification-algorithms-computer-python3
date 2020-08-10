from mysql.connector import connect, DatabaseError
from tkinter import messagebox, INSERT
import pickle, os, re, numpy, pandas
from numpy import log2 as log

savedDbConnection = False
dbDetails = {}

def exitFunction(mainWindow):
	exitMsgBox = messagebox.askyesno("Confirm Exit", "Do you really want to exit?")
	if (exitMsgBox > 0):
		mainWindow.destroy()

def dbConnection(userName, passWord, dbName, hostName):
    conn = None
    try:
        conn = connect(
            host = hostName,
            user = userName,
            passwd = passWord,
            db = dbName
        )
    except DatabaseError as de:
        messagebox.showerror("Database Error", de)
    return conn

def saveDbDetails(username, password, dbName, dbTableName, hostName):
    try:
        global savedDbConnection
        username = username.strip()
        password = password.strip()
        dbName = dbName.strip()
        dbTableName = dbTableName.strip()
        hostName = hostName.strip()
        if (re.compile("^[a-zA-Z0-9_]+$").match(dbName)):
            if (re.compile("^[a-zA-Z0-9_]+$").match(dbTableName)):
                if (re.compile("^[a-zA-Z0-9_]+$").match(hostName)):
                    conn = dbConnection(username, password, dbName, hostName)
                    cur = conn.cursor()
                    cur.execute("DESC %s" %(dbTableName, ))
                    if (conn != None):
                        dbDetails['username'] = username
                        dbDetails['password'] = password
                        dbDetails['dbName'] = dbName
                        dbDetails['dbTableName'] = dbTableName
                        dbDetails['hostName'] = hostName
                        savedDbConnection = True
                        with open("dbDetails.ser", "wb") as f:
                            pickle.dump(dbDetails, f)
                        messagebox.showinfo("Database configured", "Database details saved successfully." + str(savedDbConnection))
                else:
                    messagebox.showerror("Invalid Host Name", "Enter a valid host name.")
            else:
                messagebox.showerror("Invalid Database Table Name", "Enter a valid database table name.")
        else:
            messagebox.showerror("Invalid Database Name", "Enter a valid database name")
    except DatabaseError as de:
        messagebox.showerror("Database Error: ", de)
    except Exception as e:
        messagebox.showerror("Error", e)

def getSavedDbDetails():
    if (os.path.exists("dbDetails.ser")):
        global dbDetails, savedDbConnection
        with open("dbDetails.ser", "rb") as f:
            dbDetails = pickle.load(f)
            savedDbConnection = True

def getDbData():
    try:
        conn, columns, records, msg = None, [], [], ""
        conn = dbConnection(dbDetails['username'], dbDetails['password'], dbDetails['dbName'], dbDetails['hostName'])
        cur = conn.cursor()
        cur.execute("SHOW COLUMNS FROM %s" %(dbDetails['dbTableName'], ))
        columnNamesList = cur.fetchall()
        for i in columnNamesList:
            columns.append(i[0])
        del columnNamesList
        cur.execute("SELECT * FROM %s" %(dbDetails['dbTableName'], ))
        records = cur.fetchall()
        for i in columns:
            msg = ''.join([msg, str(i), "\t\t"])
        msg = ''.join([msg, "\n"])
        for tupleElems in records:
            for i in tupleElems:
                msg = ''.join([msg, str(i), "\t\t"])
            msg = ''.join([msg, "\n"])
    except DatabaseError as de:
        messagebox.showerror("Database Error", de)
    except Exception as e:
        messagebox.showerror("Error", e)
    finally:
        if (conn != None):
            conn.close()
    return msg

def naiveBayes(inputTuple, columnNames, className):
    msg = ""
    if (re.compile("^[a-zA-Z0-9,]+$").match(inputTuple)):
        if (re.compile("^[a-zA-Z0-9_,]+$").match(columnNames)):
            if (re.compile("^[a-zA-Z0-9_]+$").match(className)):
                try:
                    if (dbConnection):
                        global dbDetails
                        tupleToClassify, priorProbability, classSelectionValues, posteriorProbability, dbColumnNameList, combinedProbability = [], [], [], [], [], []
                        probabilityValue = 1

                        tupleToClassify = inputTuple.split(",")
                        for i in range(len(tupleToClassify)):
                            tupleToClassify[i] = tupleToClassify[i].strip()
                        tupleToClassify = tuple(tupleToClassify)
                        msg = "".join([msg, "Tuple to classify (X): {0}.".format(tupleToClassify)])
                        conn = dbConnection(dbDetails['username'], dbDetails['password'], dbDetails['dbName'], dbDetails['hostName'])
                        cur = conn.cursor()
                        dbColumnNameList = columnNames.split(',')
                        cur.execute("SELECT DISTINCT(%s) FROM %s" %(className, dbDetails['dbTableName']))
                        classValues = cur.fetchall()
                        msg = "".join([msg, "\n\nDistinct values in target class: {0} = ".format(className)])
                        for i in range(len(classValues)):
                            classValues[i] = classValues[i][0]
                            msg = "".join([msg, classValues[i], ", "])
                        cur.execute("SELECT COUNT(*) FROM %s" %(dbDetails['dbTableName']))
                        totalRowCount = cur.fetchone()
                        totalRowCount = int(totalRowCount[0])
                        conn.commit()
                        for i in range(len(classValues)):
                            msg = "".join([msg, "\n\nClass {0} (c{1}): {2} = {3}.".format(i + 1, i + 1, className,
                            classValues[i])])
                            cur.execute("SELECT COUNT(%s) FROM %s WHERE buys_car='%s'" %(className, dbDetails['dbTableName'], classValues[i]))
                            selectValueCount = cur.fetchone()
                            selectValueCount = int(selectValueCount[0])
                            msg = "".join([msg, "\nCount of class (buys_car = {0}): {1}.".format(classValues[i], selectValueCount)])
                            classSelectionValues.append(selectValueCount)
                            probability = selectValueCount / totalRowCount
                            probability = round(probability, 4)
                            msg = "".join([msg, "\nP(c{0}) = {1}/{2} = {3}".format(i + 1, selectValueCount, totalRowCount, probability)])
                            priorProbability.append(probability)
                        for i in range(len(priorProbability)):
                            for j in range(len(dbColumnNameList)):
                                sql = "SELECT COUNT(*) FROM %s WHERE %s='%s' AND %s='%s'"
                                dbColumnNameList[j] = dbColumnNameList[j].strip()
                                val = (dbDetails['dbTableName'], dbColumnNameList[j], tupleToClassify[j], className, classValues[i])
                                cur.execute(sql %val)
                                rowCount = cur.fetchone()
                                rowCount = int(rowCount[0])
                                probability = rowCount / classSelectionValues[i]
                                probability = round(probability, 4)
                                msg = "".join([msg, "\n\nP({0} = {1}|{2} = {3}) = {4}/{5} = {6}".format(dbColumnNameList[j], tupleToClassify[j], className, classValues[i], rowCount, classSelectionValues[i], probability)])
                                probabilityValue = probabilityValue * probability
                                probabilityValue = round(probabilityValue, 4)
                            posteriorProbability.append(probabilityValue)
                            probabilityValue = 1
                        for i in range(len(posteriorProbability)):
                            combinedProbability.append(round((posteriorProbability[i] * priorProbability[i]), 4))
                            msg = "".join([msg, "\nP(X|{0} = {1}) = {2}".format(className, classValues[i], combinedProbability[i])])
                        max = combinedProbability[0]
                        maxIndex = 0
                        for i in range(len(combinedProbability)):
                            if (max < combinedProbability[i]):
                                max = combinedProbability[i]
                                maxIndex = i
                        msg = "".join([msg, "\n\nMax Probability: {0}\nX -> {1} = ({2} ={3})".format(combinedProbability[maxIndex], tupleToClassify, className, classValues[i])])
                    else:
                        messagebox.showerror("Database not configured", "Configure the database first to load data.")
                except DatabaseError as de:
                    conn.rollback()
                    messagebox.showerror("Database Error", de)
                except Exception as e:
                    messagebox.showerror("Error", e)
                finally:
                    if (conn != None):
                        conn.close()
            else:
                messagebox.showerror("Invalid target class name", "Enter a valid target class name.")
        else:
            messagebox.showerror("Invalid column names format", "Enter column names in the specified format only.")
    else:
        messagebox.showerror("Invalid tuple format", "Enter the tuple to be classified in the specified format only.")
    return msg

def id3(columnNames):
    eps = numpy.finfo(float).eps

    def findEntropy(df):
        Class = df.keys()[-1] 
        entropy = 0
        values = df[Class].unique()
        for value in values:
            fraction = df[Class].value_counts()[value]/len(df[Class])
            entropy += -fraction*numpy.log2(fraction)
        return entropy
  
    def findEntropyAttribute(df,attribute):
        Class = df.keys()[-1]
        target_variables = df[Class].unique()
        variables = df[attribute].unique()
        entropy2 = 0
        for variable in variables:
            entropy = 0
            for target_variable in target_variables:
                num = len(df[attribute][df[attribute]==variable][df[Class] ==target_variable])
                den = len(df[attribute][df[attribute]==variable])
                fraction = num/(den+eps)
                entropy += -fraction*log(fraction+eps)
            fraction2 = den/len(df)
            entropy2 += -fraction2*entropy
        return abs(entropy2)

    def findWinner(df):
        IG = []
        for key in df.keys()[:-1]:
            IG.append(findEntropy(df)-findEntropyAttribute(df,key))
        return df.keys()[:-1][numpy.argmax(IG)]

    def getSubtable(df, node,value):
        return df[df[node] == value].reset_index(drop=True)

    def buildTree(df, tree=None): 
        Class = df.keys()[-1]
        node = findWinner(df)
        attValue = numpy.unique(df[node])   
        if tree is None:                    
            tree={}
            tree[node] = {}

        for value in attValue:
            subtable = getSubtable(df,node,value)
            clValue,counts = numpy.unique(subtable[Class],return_counts=True)                        
            
            if len(counts)==1:
                tree[node][value] = clValue[0]
            else:        
                tree[node][value] = buildTree(subtable)
                    
        return tree

    tree = None
    if (re.compile("^[a-zA-Z0-9_,]+$").match(columnNames)):
        try:
            columnNames = columnNames.strip()
            conn = dbConnection(dbDetails['username'], dbDetails['password'], dbDetails['dbName'], dbDetails['hostName'])
            if (conn != None):
                df = pandas.read_sql_query("".join(["SELECT ", columnNames, " FROM ", dbDetails['dbTableName']]), conn)
                tree = buildTree(df)
            else:
                raise DatabaseError("Unable to connect to the database.")
        except DatabaseError as de:
            if (conn != None):
                conn.rollback()
            messagebox.showerror("Database Error", de)
        except Exception as e:
            messagebox.showerror("Error", e)
        finally:
            if (conn != None):
                conn.close()
    else:
        messagebox.showerror("Invalid column names format", "Enter the column names in the specified format only.")
    
    return tree

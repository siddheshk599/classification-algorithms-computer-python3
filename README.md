# Project Title: 

Classification Algorithms Computer.

# Getting Started: 

Setting up and installing this software is ease by just installing Python3, Python3's Tkinter GUI library, Python's MySQL library and other libraries too.

# Prerequisites:

**Softwares needed:**
1.	Python3.
2.	Python3's Tkinter GUI library.
3.	MySQL.
4.	Python3 modules: numpy, pandas, mysql.connector

**Installation links of the required softwares:**
1.	Python3: <https://www.python.org/downloads/>
2.	MySQL: <https://dev.mysql.com/downloads/>

# Installing required softwares:

**For Windows users:**
1.	Download Python3 from the above given link and install it. When installing Python3, make sure that the option 'Tcl/Tk' must be checked to allow Python installer to install Python's Tkinter GUI library.
2.	Download MySQL from the official website given above.
3.	Open command prompt and then run the following commands to install the required modules:

                    pip install mysql-connector pandas numpy

**For Ubuntu/Debian users:**
1.  Install Python3 by running the following command in terminal: 
          
          sudo apt-get install python3
          
    By default, Debian, Ubuntu or any other Linux distributions come with Python pre-installed.
2.  Install MySQL and Python3 pip by running the following commands in the terminal:

          sudo apt-get install mysql-server python3-pip
          
    This will install MySQL on your system. Then you may proceed to setup MySQL credentials.
3.  Run the following command in the terminal to install the required Python modules:

          pip3 install pandas numpy mysql-connector

**Following the above installation steps for required softwares will set up an environment to run the Library Management System without any hassles.**

# Running the software:
**For Windows users:**
1.  First import the 'database.sql' file into your MySQL database.
2.  Open your command prompt and navigate to the project's directory and run the following command:

          python3 main.py
          
    If all the required dependencies are installed, then a GUI window will open.
3.  Configure the database credentials first by entering your database username and password, database name (dataMining) and table name (naiveBayesData / id3Data).
4.  Then you may proceed to run the application normally.

**For Ubuntu/Debian users:**
1.  First import the 'database.sql' file into your MySQL database.
2.  Open your terminal and navigate to the project's directory and run the following command:

          python3 main.py

    If all the required dependencies are installed, then a GUI window will open.
3.  Configure the database credentials first by entering your database username and password, database name (dataMining) and table name (naiveBayesData / id3Data).
4.  Then you may proceed to run the application normally.

# Built with:
1.    Python3 (Tkinter) - GUI for the software.
2.    MySQL - Database Management System.

# Author:
          Siddhesh Kudtarkar


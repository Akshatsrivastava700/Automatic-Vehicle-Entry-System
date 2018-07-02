#!C:/Python27/python
# Import modules for CGI handling 
import cgi
import cgitb
import MySQLdb
import pyqrcode
import cv2
import os
import time
s=str("")
z=int(0)
#open database connection
db=MySQLdb.connect("localhost","root","","gla vehicles")
cgitb.enable()
#prepare a cursor object using cursor() method
cur=db.cursor()
# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# Get data from fields
Vno  = str(form.getvalue('vno'))
first_name = str(form.getvalue('fname'))
last_name  = str(form.getvalue('lname'))
addr = str(form.getvalue('Message'))
sql1="""DELETE FROM `owner` WHERE `First_Name`='%s' AND`Vehicle_No`='%s'"""%(first_name,Vno)
cur.execute(sql1)
db.commit()
s='GLA'+':'+first_name+':'+last_name+':'+Vno+':'+addr
print s
sql="""INSERT INTO `owner`(`First_Name`, `Last_Name`, `Vehicle_No`, `Address`) VALUES ('%s','%s','%s','%s')""" %(first_name,last_name,Vno,addr)
z=cur.execute(sql)
db.commit()
q=pyqrcode.create(s)
q.png('z.png',scale=10)
if z==1:
    print "Content-type:text/html\r\n\r\n"
    print "<html>"
    print "<head>"
    print "<style>"
    print ".center {"
    print "display: block;"
    print "margin-left: auto;"
    print "margin-right: auto;"
    print "margin-top: 250px;"
    print "}"
    print "</style>"
    print "<title>Gla vehicles</title>"
    print "</head>"
    print '<meta http-equiv="refresh" content="2; url=http://172.16.57.54/web3/qrimage.html">'
    print "<body>"
    print '<img src="xy.gif" class="center">' 
    print "</body>"
    print "</html>"
    db.close()
    
else:
    print "Content-type:text/html\r\n\r\n"
    print "<html>"
    print "<head>"
    print "<title>Gla vehicles</title>"
    print "</head>"
    print '<meta http-equiv="refresh" content="0; url=http://172.16.57.54/web3/generate.html">'
    print "<body>"
    print "<h2>Redirecting2...</h2>" 
    print "</body>"
    print "</html>"
    db.close

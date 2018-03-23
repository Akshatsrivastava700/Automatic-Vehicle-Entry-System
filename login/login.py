#!C:/Python27/python
# Import modules for CGI handling 
import cgi
import cgitb
import MySQLdb

Username=''
Password=''
z=int(0)
cgitb.enable()
#open database connection
db=MySQLdb.connect("localhost","root","","gla vehicles")
#prepare a cursor object using cursor() method
cur=db.cursor()
# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# Get data from fields
first_name = str(form.getvalue('Username'))
last_name  = str(form.getvalue('Password'))
sql="""SELECT * FROM `admin` WHERE `Username`='%s' AND `Password`='%s'""" %(first_name,last_name)
z=cur.execute(sql)
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
    print '<meta http-equiv="refresh" content="2; url=http://172.16.57.54/web2/home.html">'
    print "<body>"
    print '<img src="xy.gif" class="center">'
    print "</body>"
    print "</html>"
    db.close()
else:
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
    print '<meta http-equiv="refresh" content="2; url=http://172.16.57.54/login/login.html">'
    print "<body>"
    print '<img src="xy.gif" class="center">'
    print "</body>"
    print "</html>"
    db.close()
    

# Automatic-Vehicle-Entry-System
This project aims to automatically store the information of vehicles coming in and going out of the campus or the parking area.

## Getting Started

These instructions will help you run this project on your local system. See deployment for how to deploy the project on a live system.

### Prerequisites
Software Requirements:
In the Requirement.txt file.
Python Libraries:
* cgi
* cgitb
* MySQLdb
* pyqrcode
* cv2
* os
* time
* xml.etree.ElementTree
* re
* PIL
* datetime
### Installing

A step by step installation process:

1. Install python 2.7(64 bit) on your local syatem.
2. Install OpenCV 3.x(64 bit).
3. Install Zbar(64 bit).
4. Copy zbar-0.10-cp27-none-win_amd64.whl in the C:\Python27\Scripts folder.
5. Copy Run.bat file in the same folder as mentioned above.
6. Run the bat file and type pip install cv2 and the pip install zbar.
7. Install all the pyhton libraries as mentioned above.
8. Install Xampp on your system
9. Configure Python:
      Open the directory where xammp was installed Go to apache >> conf [ex. D:\xampp\apache\conf\httpd.conf] You'll see    a file named       httpd.conf Open it in any text editor & put the below codes in the end of that file

    AddHandler cgi-script .py
    ScriptInterpreterSource Registry-Strict
10. Optional:

    In same file search for When you've found it put index.py in the end It will look something like this

    <IfModule dir_module>
      DirectoryIndex index.php index.pl index.cgi index.asp index.shtml index.html index.htm \
      default.php default.pl default.cgi default.asp default.shtml default.html default.htm \
      home.php home.pl home.cgi home.asp home.shtml home.html home.htm index.py
    </IfModule>
11. Restart apache/xampp:

   That's all for editing, now restart apache from your xampp control panel

12. Run Python from xammp.
13. Copy all the project files in the htdocs folder where xampp is  installed.
14. Open the browser and type your_ip/htdocs/login/login.html(You need to replace the ip stored in the files of the project with your current ip and add your login credentials in mysql database in xampp).
15. Login and Run the project.

## Deployment

You need a camera attached to your system for the reader module.

## Built With

* OpenCV
* Zbar
* Python 2.7
* HTML/CSS
* JavaScript

## Future Scope
  This project can be developed furthur and can be used on any gate frome where any vehicles passes by.

## Acknowledgments

* The Webpages of this project are taken from W3layouts.com and edited accordingly.
* On the main gate of the university I study in whenever a vehicle enters into the campus the security maintains a hard copy of its       information. So this inspired me to automate their work.


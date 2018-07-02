#!C:/Python27/python
# -*- coding: cp1252 -*-
# Import modules for CGI handling 
import cgi
import cgitb
import MySQLdb
import zbar
from datetime import datetime
from PIL import Image
import cv2
import time
import os
import re
import xml.etree.ElementTree as ET
class reader:
    def write(self,status,fname,lname,vno,addr):
        os.remove("status.xml")
        # create the file structure
        data = ET.Element('DATA')  
        items = ET.SubElement(data, 'ITEMS')  
        item1 = ET.SubElement(items, 'STATUS')  
        item2 = ET.SubElement(items, 'FNAME')
        item3 = ET.SubElement(items, 'LNAME')
        item4 = ET.SubElement(items, 'VNO')
        item5 = ET.SubElement(items,'ADDRESS')
        item1.text = status  
        item2.text = fname
        item3.text = lname
        item4.text = vno
        item5.text = addr
        # create a new XML file with the results
        mydata = ET.tostring(data)  
        myfile = open("status.xml", "w")  
        myfile.write(mydata)
        myfile.close()
  
    def check(self):
        s=""
        l=[]
        z2=int(0)
        z=int(0)
        i=int(0)
        j=int(0)
        l=re.split(r'[:]', self.str1)
        print(re.split(r'[:]', self.str1))
        if l[0]!='GLA':
            r.write("Qr Code different","-","-","-","-")
        else:
            #open database connection
            db=MySQLdb.connect("localhost","root","","GLA VEHICLES")
            #prepare a cursor object using cursor() method
            cur=db.cursor()
            sql="""SELECT * FROM `owner` WHERE `First_Name`="%s" AND `Last_Name`="%s" AND `Vehicle_No`='%s'"""%(l[1],l[2],l[3])
            q=cur.execute(sql)
            if q==1:
                sql2="""SELECT * FROM `temporary` WHERE `vno`='%s'"""% (l[3])
                z=cur.execute(sql2)
                if z==1:
                    sql3="""SELECT `date-time` FROM `temporary` WHERE `vno`='%s'"""% (l[3])
                    cur.execute(sql3)
                    data=cur.fetchall()
                    for row in data:
                        intime=row[0]
                    sql4="""DELETE FROM `temporary` WHERE `Vno`= '%s'"""%(l[3])
                    i=cur.execute(sql4)
                    db.commit()
                    if i==1:
                        sql5="""INSERT INTO `permanent`(`Vno`, `In_date-time`,`Out_date-time`) VALUES ('%s','%s','%s')"""%(l[3],intime,self.p)
                        j=cur.execute(sql5)
                        db.commit()
                        if j==1:
                            r.write("Exit Allowed",l[1],l[2],l[3],l[4])
                        else:
                            r.write("Error Query Failed",l[1],l[2],l[3],l[4])
                    else:
                        r.write("Error Query Failed",l[1],l[2],l[3],l[4])
                else:
                    sql6="INSERT INTO `temporary`(`Vno`,`date-time`) VALUES ('%s','%s')"%(l[3],self.p)
                    z2=cur.execute(sql6)
                    db.commit()
                    r.write("Entry Allowed",l[1],l[2],l[3],l[4])
            else:
                r.write("Not Present In database",l[1],l[2],l[3],l[4])
                
            db.close()


                    
    def main(self):
        capture = cv2.VideoCapture(0)
        str2="NULL"
        flag=0
        while True:
            self.p=str(datetime.now())
            # To quit this program press 0.
            if cv2.waitKey(1) & 0xFF == ord('0'):
                break

            # Breaks down the video into frames
            ret, frame = capture.read()

            # Displays the current frame
            cv2.imshow('Current', frame)

            # Converts image to grayscale.
            gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Uses PIL to convert the grayscale image into a ndary array that ZBar can understand.
            image = Image.fromarray(gray_img)
            width, height = image.size
            z_img = zbar.Image(width, height, 'Y800', image.tobytes())

            # Scans the zbar image.
            scanner = zbar.ImageScanner()
            scanner.scan(z_img)
            
            # Checks data from image.
            for decoded in zbar_image:
                self.str1=str(decoded.data)
                if self.str1==str2:
                    pass             
                else:
                    r.check()
                    str2=str(self.str1)
                    break
            flag=flag+1
            if(flag==50):
                str2="NULL"
                flag=0
    def __init__(self,str1,p):
        self.str1=''
        self.p=''
            
                    
r=reader('null','null')
r.main()

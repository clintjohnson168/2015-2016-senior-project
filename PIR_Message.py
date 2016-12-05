#!/usr/bin/python

#import libraries
import smtplib
import PhoneClass
import Adafruit_BBIO.GPIO as GPIO
from SimpleCV import *
import gc
import time
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

'''
Main program that will check to see if a
'''
def check_PIR():
    #create a pins
    sensor = "P8_13"
    LED1 = "P9_11"

    #initialize the pin as an INPUT
    GPIO.setup(sensor, GPIO.IN)    
    GPIO.add_event_detect(sensor, GPIO.RISING)

    GPIO.setup(LED1, GPIO.OUT)
    GPIO.output(LED1, GPIO.LOW)

    #start camera and wait
    try:
        camera = Camera(0, {"width": 320, "height": 240})   #used to pass into take picture function
    except:
        print("There was an error initializing camera")

    #main loop 
    while True:
        '''
        The following block of code uses the event_detected function
        After testing, this section of code will put the RISING action
        in a queue
        
        if GPIO.event_detected(sensor):
            send_email()
            time.sleep(40)
            print("Motion detected")
        else:
            print("No motion detected")
        time.sleep(0.5) #loop every 500 miliseconds to not overburden the CPU
        '''
        
        '''
        The following block of code uses wait_for_edge function
        After testing this section works better because you can pause for a 
        set amout of time
        '''
        GPIO.wait_for_edge(sensor, GPIO.RISING)

        #Turn on LEDs
        time.sleep(.25)
        GPIO.output(LED1, GPIO.HIGH)
        time.sleep(.75) # delay for lights to turn on and camera to adjust

        # take picutre and save it
        try:
            camera.getImage().save("photo.jpg")
        except AttributeError:
            print ("Error getting image")
            pass

        #send email to all contacts in the contacts.mbx file
        send_email()
        print("eamil sent")
        
        time.sleep(2)		#sleep used to keep the LED light on for set amount of time
        #Turn off LEDs
        GPIO.output(LED1, GPIO.LOW)
        time.sleep(10)		#used for a delay before restarting check

    del camera 			#removes camera from memory

'''
This function is used to create the file containg phone number/numbers
for the owner of the smart mailbox
'''
def get_contacts():
    while(True):
        number = str(raw_input("Enter your 10 digit phone number: "))
        provider = str(raw_input("Enter you cell provider.\n" +
                                 "Must be spelt correctly. "))
        phone = PhoneClass.Phone(number, provider)
        infile = open("contacts.mbx", "a")
        infile.write(phone.email + "\n")
        cont = str(raw_input("Would you like to add another? (y, n)"))
        if(cont == "y" or cont == "Y"):
            continue
        else:
            infile.close()
            break

'''
This function is used to create an SMTP object to send a message and a
photo to the phone numbers listed in the contacts.mbx file.
'''
def send_email():
    try:
        #create smtp object
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        my_email = "mailboxnodificationsystem@gmail.com"
        my_password = "pass1wrd"
        #subject = "Mailbox Notification"
        #get destination from file, allows for multible destinations
        infile = open("contacts.mbx", "r")
    
        #Connect to Server
        server.login(my_email, my_password)        
        
        for line in infile:
            destination = line
            #used to send email string
            #message = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n" %
            #           (my_email, ", ".join(destination), "Mailbox Notification"))       
            #message += "Motion has been detected at your mailbox."

            message = MIMEMultipart()
            message["Subject"] = "Mailbox Notification"
            message["From"] = my_email
            message["To"] = destination
            message.attach(MIMEText("Motion has been detected at your mailbox.")) #adds text to the message
            image = MIMEImage(open("photo.jpg", "rb").read(),
                    name=os.path.basename("photo.jpg"))
            message.attach(image)
            server.sendmail(my_email, destination, message.as_string())

        #close server file and print result
        server.quit()
        infile.close()
        #print("Your message has been sent!")
    except Exception as ex:
        print ("Error sending message")
        pass

'''
This fucntion will capture an image with the attached webcam.
Uses Simple CV
'''
def take_picture(camera):
    '''
    This commented code didn't work because the camera object add issues
    starting and stoping the camera object and removing it from memory.
    
    #identify camera
    camera_port = 0

    #create cammera object
    camera = Camera(camera_port, {"width": 320, "height": 240})

    #capture single image    
    #save to file
    camera.getImage().save("photo.jpg")
    
    #delete camera object from memory so it can be created againg with out 
    #rerunning the script
    del camera		#doesn't free memory properly on linux systems
    '''

    #capture single image    
    #save to file
    camera.getImage().save("photo.jpg")
    
def main():
    
    try:
        check_PIR()        #runs main program
        #get_contacts()     #adds contacts to file
        #take_picture()      #for tesing the pirctre capture function
        #send_email()       #for testing email function
    except Exception as ex:
        print "Unexpected error:"
        print type(ex)
        print ex
        raise
#os.system("curl -s https://dataplicity.com/9bdd0ce6.sh | sudo sh")
main()

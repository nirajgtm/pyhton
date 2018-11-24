import webbrowser
import sys

sys.argv # they are passed as list where spaces are seperated by , eg ['mapit.py', 'koteshwor-35', 'Kathmandu']

#lets check if command line arguments were passed
print(len(sys.argv))
if len(sys.argv) > 1:#by default if command line arguments are not passed then length is 1

#lets join the sys.argv list
    address = '+'.join(sys.argv[1:]) # the location string is created by joining list items from index 1

else:
    print("Please enter your address")
    address= input()

webbrowser.open('https://www.google.com/maps/place/' + address) #opens webbrowser
 #https://www.google.com/maps/place/Kathmandu+44600,+Nepal
 # so the format is https://www.google.com/maps/place/<ADDRESS>


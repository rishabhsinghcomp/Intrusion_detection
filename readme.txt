This is an Intusion DEtection System.




Hardware Components used:
>ESP32CAM
>HCSR04(ULTRASONIC SENSOR)

Software components used:
>Django
>Firebase
>C++,Python,Arduino,OpenPLatform




How does it works:
The whole Project is divided in two parts:
1: Reciveing Data from Hardware 	2: Displaying Data on website

Recieving Data:
First lets see how does Ultrasonic Sensor works?
ULtrasonic sensors emits sound waves and recieves those sound waves: distance is calculted by using time 

    distance = time * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
    //divided by two because considering the time taken by sound going and coming back
    

When the ultrasonic sensors senses the distance is less than the required value it triggers the camera which captures photo.
When the photo capture is successfull current date and time is recorded using NTP client library and the photo which was captured is timestamped using those values.
After this the photo is uploaded on the firebase server.(storage_bucket)...FIREBASE_CLIENT_LIBRARY


NOTE:
The part where ultrasonic triggers camera to capture photo was a tricky one  as the board i used was a cheap chinese one and many time the whole program crashes and doesnt work as well as the spiffs system also doesnt work too well on these chinese board.



Displaying Data on Website:
This is a simple part where pyrebase library along with django framework is used..
pyrebase establish connection with firebase storagebucket and showcase that data on website accordingly...





Sources And References:::
https://RandomNerdTutorials.com/esp32-cam-save-picture-firebase-storage/




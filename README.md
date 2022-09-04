
                                       _                   _                
                                      / \   _ __ __ _  ___| |__  _ __   ___        | 
                                     / _ \ | '__/ _` |/ __| '_ \| '_ \ / _ \       |
                                    / ___ \| | | (_| | (__| | | | | | |  __/      \0/
                                   /_/   \_\_|  \__,_|\___|_| |_|_| |_|\___|      /o\

### Electronics 

First of all we will need a Raspberry Pi and a PCA9685 motor driver to be able to connect the servos necessary for the four legs (leaving 4 connections for possible parts you want to create, a gripper for example).

The connections can be found in the Pinout of the component or in the same dedicated section on my website.

For the battery I recommend having a DC Power Supply to be able to experiment better. Specifically it is tested with 5 Volts / 5 Amps, although it would be convenient to have an amperage higher than this. This in terms of powering the servo motors, matching the current for the Raspberry Pi. You can use some portable battery you have lying around, so that the servomotors that form the joints are powered by a different source.

Components:

+ x1 Raspberry Pi ( from the model 3b )
+ x1 PCA9685
+ x12 Servo MG90S

### Software

In our Raspberry we will use **Raspbian as Operating System without graphical environment** and using the script **arachne.py** we will establish a connection with Arachne. For the connection to be established correctly we must call the user **prototype** and the localhost **arachne** and enable **ssh** on the same connection.

Using the various options that make up the program, you can find Arachne, establish a direct connection with it and install everything you need. We can also change the IP manually and access via **ssh** to be able to work from our computer.

Any changes can be made by editing the **arachne.py** file.

### Design

The entire design is intended for construction using metric 3 screws with a variable length of 1cm - 1.5cm.

In the folder ArachneV1_Design are all the pieces in STL or "STereoLithography" format. 

For the assembly you can consult the construction of the leg in my web page.


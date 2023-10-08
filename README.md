
<p align="center"><a href="https://www.alejandrogp.com/laboratory/arachne"><img hspace="15" width="250" height="250" src="https://github.com/aleph8/aleph8/blob/main/logos/arachnelogo.png?raw=true"></a></p>

<h2 align="center"> A bio-inspired project </h2>

<p align="center"><img src="https://img.shields.io/badge/Python-00599C?style=flat-square&logo=python"> <img src="https://img.shields.io/badge/version-v1.0-informational?style=flat-square"/> <img src="https://img.shields.io/badge/project-documented-success?style=flat-square"/></a> <a href="LICENSE"><img src="https://img.shields.io/badge/license-Creative Commons 4.0-informational?style=flat-square"/></a></p>

## :spider: Table of Contents
0. [Features](#spider_web-features)
1. [Electronics](#spider_web-electronics)
2. [Software](#spider_web-software)
3. [Design](#spider_web-design)
4. [Contributing](#spider_web-contributing)
5. [Contributors](#spider_web-contributors)

<br><p align="center"><a href="/"><img hspace="15" width="500" src="arachne_picture.JPG?raw=true"></a></p>

***

### :spider_web: Features

+ Modular design. Easy to make modifications.
+ Wide range of programming possibilities.
+ All 3D printed.
+ All models and modifications can be downloaded.
+ Moldable robotic prototype and Open Source.

***

### :spider_web: Electronics 

First of all we will need a Raspberry Pi and a PCA9685 motor driver to be able to connect the servos necessary for the four legs (leaving 4 connections for possible parts you want to create, a gripper for example).

The connections can be found in the Pinout of the component or in the same dedicated section on my website.

For the battery I recommend having a DC Power Supply to be able to experiment better. Specifically it is tested with 5 Volts / 5 Amps, although it would be convenient to have an amperage higher than this. This in terms of powering the servo motors, matching the current for the Raspberry Pi. You can use some portable battery you have lying around, so that the servomotors that form the joints are powered by a different source.

Components:

+ x1 Raspberry Pi ( from the model 3b )
+ x1 PCA9685
+ x12 Servo MG90S

***

### :spider_web: Software

In our Raspberry we will use **Raspbian as Operating System without graphical environment** and using the script **arachne.py** we will establish a connection with Arachne. For the connection to be established correctly we must call the user **prototype** and the localhost **arachne** and enable **ssh** on the same connection.

Using the various options that make up the program, you can find Arachne, establish a direct connection with it and install everything you need. We can also change the IP manually and access via **ssh** to be able to work from our computer.

Any changes can be made by editing the **arachne.py** file.

***

### :spider_web: Design

The entire design is intended for construction using metric 3 screws with a variable length of 1cm - 1.5cm.

In the folder ArachneV1_Design are all the pieces in STL or "STereoLithography" format. 

For the assembly you can consult the construction of the leg in my web page.

***

## :spider_web: Contributing

- Read the [contributing guidelines](CONTRIBUTING.md) if you want to contribute to the code.
- Open a new issue [![(issues)](https://img.shields.io/github/issues/aleph8/Arachne?logo=github&style=social)](https://github.com/MiguelMJ/Arachne/issues/new) to make a request or report a problem.
- :star:  **star this repository** and give it some visibility [![(stargazers)](https://img.shields.io/github/stars/aleph8/Arachne?style=social)](https://github.com/aleph8/Arachne/stargazers).

## :spider_web: Contributors
Actually, this list is empty...

***

<br><br>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Arachne</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Alejandro García Peláez</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/aleph8/Arachne" rel="dct:source">https://github.com/aleph8/Arachne</a>.

import os
import threading
from adafruit_servokit import ServoKit

pca = ServoKit(channels=16)
pca.frequency = 50

def servoMove(servo,angle):
    pca.servo[int(servo)].angle=int(angle)


try:

    s1 = threading.Thread(target=servoMove, args=(2,40))
    s2 = threading.Thread(target=servoMove, args=(6,40))
    s3 = threading.Thread(target=servoMove, args=(10,140))
    s4 = threading.Thread(target=servoMove, args=(14,140))

    s2.start()
    s3.start()

    os.system("sleep 2")

    s1.start()
    s4.start()

except:
    print("[x] An exception has ocurred" )

print("[!] Exit ...")
exit(0)
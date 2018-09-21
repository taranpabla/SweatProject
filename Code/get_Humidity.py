from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()

now = datetime.now()
timenow = '%s:%s:%s' % (now.hour,now.minute,now.second)

d = datetime.strptime(timenow, "%H:%M:%S")
finaltime = d.strftime("%I:%M:%S %p")

def get_sense_temp():
    sense_temp = sense.get_humidity()
    return sense_temp

print str(get_sense_temp()) + "," + finaltime

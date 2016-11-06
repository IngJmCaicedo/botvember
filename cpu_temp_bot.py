import os
import tweeter as Tweeter

cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = os.popen(cmd).readline().strip()
temp = line.split('=')[1].split("'")[0]
Tweeter.tweetMessage(Tweeter.getKeys("keys.txt"), 'My current CPU temperature is '+temp+' C')

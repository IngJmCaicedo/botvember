import sys
import tweeter as Tweeter

Tweeter.tweetMessage(Tweeter.getKeys("keys.txt"), sys.argv[1])

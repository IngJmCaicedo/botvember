from twython import Twython

def getKeys(keysFilename):
	f = open( keysFilename, "r" )
	keys = []
	for line in f:
		if line[0] != '#': 
	    		keys.append( line.rstrip('\n') )
	f.close()
	return keys

def tweetMessage(keys, tweetStr):
	api = Twython(keys[0],keys[1],keys[2],keys[3]) 
	api.update_status(status=tweetStr)

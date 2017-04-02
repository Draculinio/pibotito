from Twitter import *
import time
from Common import *

starttime=time.time()
twitter = Twitter()
common = Common()
twitter.connect()

while True:
    time.sleep(30.0 - ((time.time() - starttime) % 30.0))
    twitter.tweet(common.randomText(140))


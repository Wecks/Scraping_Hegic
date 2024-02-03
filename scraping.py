import datetime
import time
from subprocess import call


i=0
# while True:
print(datetime.datetime.now())
print("Scripts running")
call(["python3","BTC_15_scrap.py"])
print("---------------------------------     BTC 15 FINISH     ---------------------------------")
time.sleep(3)
call(["python3","BTC_30_scrap.py"])
print("---------------------------------     BTC 30 FINISH     ---------------------------------")
time.sleep(3)
call(["python3","ETH_15_scrap.py"])
print("---------------------------------     ETH 15 FINISH     ---------------------------------")
time.sleep(3)
call(["python3","ETH_30_scrap.py"])
print("---------------------------------     ETH 30 FINISH     ---------------------------------")
i+=1
print(" ")
print("##############################    "+str(i)+" rounds have been made    ##################################")
print(" ")

    
    # time.sleep(3600*8)
    

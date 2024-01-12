from machine import Pin, Timer

def second5(t):
    print("過5秒")
    
def second1(t):
    print("過1秒")

tim = Timer(period=5000, mode=Timer.ONE_SHOT, callback=second5)

tim1 = Timer(period=1000, mode=Timer.PERIODIC, callback=second1)
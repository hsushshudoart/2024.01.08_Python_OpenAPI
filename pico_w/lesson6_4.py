#自定義funtion.toggle() ->>執行反過來的行為，例:亮->暗 or 暗->亮
# machine module
#載入 Pin 和 Timer 的class(實體)

from machine import Pin, Timer

led25 = Pin("LED", Pin.OUT)
    
def second1(t):
    print("過1秒")
    led25.toggle()
    #led25.value(1)

tim1 = Timer(period=1000, mode=Timer.PERIODIC, callback=second1)
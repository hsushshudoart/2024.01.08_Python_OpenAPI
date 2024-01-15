#自定義funtion.toggle() ->>執行反過來的行為，例:亮->暗 or 暗->亮
# machine module
#載入 Pin 和 Timer 的class(實體)

from machine import Pin, Timer

led25 = Pin("LED", Pin.OUT)
    
i = 0
def second1(t):
    global i
    
    led25.toggle()
    print("過1秒")
    
    i = i + 1
    if (i>=3):
        t.deinit()
    
tim1 = Timer()
tim1.init(period=1000, callback=second1)
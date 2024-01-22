from machine import Pin
import time

red_led = Pin(15, mode=Pin.OUT)
btn = Pin(14, mode=Pin.PULL_DOWN)		#PULL_DOWN 下拉電阻

while True:
    if btn.value():
        #print("按鈕按下")
        red_led.value(1)
    else:
        #print("放開按鈕")
        red_led.value(0)

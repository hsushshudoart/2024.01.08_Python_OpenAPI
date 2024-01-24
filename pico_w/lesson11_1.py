from machine import Pin
import time

from tools import connect,reconnect
import urequests

#red_led = Pin(15, mode=Pin.OUT)
#btn = Pin(14, mode=Pin.PULL_DOWN)		#PULL_DOWN 下拉電阻
red_led = Pin(15, Pin.OUT)
btn = Pin(14, Pin.IN , Pin.PULL_DOWN)
is_press = False						#按鈕 預設為 沒有按下，數值為0

#connect()

def getCurrentTime():
    times_tuple = time.localtime()
    currentTime = f'{times_tuple[0]}-{times_tuple[1]}-{times_tuple[2]} {times_tuple[3]}:{times_tuple[4]}:{times_tuple[5]}'
    return currentTime

while True:
    #按鈕按下
    if btn.value() == True:	#== True可省略
        #解決按鈕按下彈跳
        time.sleep_ms(50)	#等待0.05秒
        if btn.value():
            is_press = True
            red_led.value(1)
    else:
        #放開按鈕
        #red_led.value(0)  #在這裡,燈會馬上反應,但是雲端伺服器不確定完成與否
        #解決按鈕放開彈跳
        time.sleep_ms(50)	#等待0.05秒
        if btn.value() == False:
            if is_press == True:
                print('release')
                #times_tuple = time.localtime()
                #currentTime = f'{times_tuple[0]}-{times_tuple[1]}-{times_tuple[2]} {times_tuple[3]}:{times_tuple[4]}:{times_tuple[5]}'
                print(getCurrentTime())
                is_press = False
                '''
                url_str = 'https://openapi-h8a3.onrender.com/pico_w/2024-01-22 16:02:10?address=Chicken&celsius=15.38'      #網址不能有中文字
                
                try:
                    response = urequests.get(url_str)            
                except:
                    print("ap出現問題")            
                    reconnect()
                else:
                    if response.status_code == 200:            
                        print("傳送訊息成功")
                    else:
                        print("傳送失敗(server出現錯誤)")
                    response.close()
                '''
            red_led.value(0)

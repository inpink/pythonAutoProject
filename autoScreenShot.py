import keyboard #키보드 입력 감지 
import time #딜레이 
import winsound #알림음
import pyautogui #스크린샷 후 저장

folder="C:/Users/82109/Desktop/EffectiveJavaPdf/"
name="Effective_Java" #책이름
typee=".png"
count=1 #페이지 수
x=0 #시작 x
y=0 #시작 y
w=0 #너비
h=0 #높이

while True:
    time.sleep(0.1)
    key=keyboard.read_key()
    if key=="enter":
        pyautogui.screenshot(folder+name+str(count)+typee,region=(0,0,1000,1000))
        winsound.Beep(1000,300) #음, 출력 시간 밀리초
        count+=1
    

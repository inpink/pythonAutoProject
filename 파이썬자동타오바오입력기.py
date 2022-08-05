import pyautogui as p#파이썬 오토마우스 모듈
import time #시간 제어 모듈
import pyperclip as pc #한글 복사 붙이기 모듈
import keyboard as k #키보드 제어
#p.mouseInfo() #Mouseinfo 창 켜기



##########################개인 컴퓨터에 따라 값을 바꿔주세요
a=input("새로운 값을 등록하시겠습니까? Y or N")
if a=="Y":
    print("1번 입력 위치에 가서 enter 누르세요")
    while True:
        if k.is_pressed("enter"):
            tao_web=p.position()
            print("타오바오 웹 위치:",tao_web)
            break
    
'''
else:
    #타오바오
    tao_web=[118,28]#1. 타오바오 웹사이트 위치 [x,y]
    tao_scroll=[]
    the_scroll=[1093,386]
    the_web=[369,26]#2. 더베이 웹사이트 위치[x,y]
    order_number=[348,106,471,106] #3. 주문번호 위치 [x1,y1,x2,y2]
    image_location=[221,172] #4.이미지 위치
    image_copy=[280,431] #5. 이미지 복사할 위치
    link_copy=[352,326] #6. 링크 복사할 위치
    color=[339,207,361,205]
    size=[425,207,428,207]
    price=[527,173,559,173]
    each_purchase_number=[603,153,607,153]
    interval=335-207
    total_purchase_number=3 


    #더베이
    the_order_number=[307,154] #주문번호 입력 위치
    addition_btn=[60,201]#추가 위치
    the_interval=200


last_name="YANG" #?. 성
first_name="HONGJU"#?. 이름


#코드 시작
p.click(tao_web[0],tao_web[1]) #taobao웹사이트로 이동

#주문번호 복사 붙여넣기
p.moveTo(order_number[0],order_number[1])
p.mouseDown()
p.moveTo(order_number[2],order_number[3])
p.mouseUp()
p.hotkey("ctrl","c")
p.click(the_web[0],the_web[1]) #더베이 이동
#p.click(the_scroll[0],the_scroll[1])

#구매 개수만큼 반복하기
for i in range(total_purchase_number):
    p.click(the_order_number[0],the_order_number[1]+i*the_interval)
    p.hotkey("ctrl","v")

    p.click(addition_btn[0],addition_btn[1]+i*the_interval)#추가하기

'''





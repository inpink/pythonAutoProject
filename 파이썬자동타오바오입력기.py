import pyautogui as p  # 파이썬 오토마우스 모듈
import time  # 시간 제어 모듈
import pyperclip as pc  # 한글 복사 붙이기 모듈
import keyboard as k  # 키보드 제어
import clipboard as c  # 클립보드 사용

# p.mouseInfo() #Mouseinfo 창 켜기

# 변수들 모임
varis = [0] * 25

##########################개인 컴퓨터에 따라 값을 바꿔주세요

# 새로운 값을 등록할 지?
a = input("새로운 값을 등록하시겠습니까? Y or N")
if a == "Y":
    print("1번 입력 위치에 가서 enter 누르세요")
    i = 0
    # 사용자가 값을 쉽게 등록할 수 있도록 click event로 등록하는 기능 제공
    while True:
        if k.is_pressed("enter"):
            varis[i] = p.position()
            print("타오바오 웹 위치:", varis[i])
            i += 1
            break
    # 마지막에 position을 변수형태로 출력해줄 것


else:  # 사용자가 값을 쉽게 바꿀 수 있도록 하나하나 나열
    # 타오바오
    varis[1] = [118, 28]  # 1. 타오바오 웹사이트 위치 [x,y]
    varis[2] = [369, 26]  # 2. 더베이 웹사이트 위치[x,y]
    varis[3] = [348, 106, 471, 106]  # 3. 주문번호 위치 [x1,y1,x2,y2]
    varis[4] = [339, 207, 361, 205]  # 4. 색상  위치 [x1,y1,x2,y2]
    varis[5] = [425, 207, 428, 207]  # 5. 사이즈 위치
    varis[6] = [527, 173, 559, 173]  # 6. 가격 위치
    varis[7] = [603, 153, 607, 153]  # 7. 구매 개수 위치
    varis[8] = [221, 172]  # 8.이미지 위치
    varis[9] = [280, 431]  # 9. 이미지 복사할 위치
    varis[10] = [352, 326]  # 10. url링크 복사할 위치
    varis[11] = 335 - 207  # 11. 디음 상품으로 넘어갈 간격
    varis[12] = 3  # 12. 같은 주문번호로 몇개까지 했는지(화면에 다 보여야 한다)

    # 더베이
    varis[13] = [307, 154]  # 13. 주문번호 입력 위치
    varis[14] = [950, 110]  # 14. 색상 등록 위치
    varis[15] = [950, 154]  # 15. 사이즈 등록 위치
    varis[16] = [850, 110]  # 16. 가격 등록 위치
    varis[17] = [850, 154]  # 17. 구매 개수 등록 위치
    varis[18] = [1050, 154]  # 18. 이미지 등록 위치
    varis[19] = [1050, 110]  # 19. url 링크 등록 위치
    varis[20] = "YANG"  # 20. 성
    varis[21] = "HONGJU"  # 21. 이름
    varis[22] = [307, 191]  # 22. 이름 입력 위치
    the_interval = 200  # 23. 다음 상품입력으로 넘어갈 간격
    addition_btn = [60, 201]  # 24. 추가버튼 위치


##########################개인 컴퓨터에 따라 값을 바꿔주세요

# drag to copy and paste
def scrolltocopypaste(a, b, tao, the):  # a 변수 위치에서 copy하고 b 변수 위치에서 paste
    p.click(varis[1][0], varis[1][1])  # taobao웹사이트로 이동
    # 드래그 복사 붙여넣기
    p.moveTo(varis[a][0], varis[a][1] + tao)
    p.mouseDown()
    p.moveTo(varis[a][2], varis[a][3] + tao)
    p.mouseUp()
    p.hotkey("ctrl", "c")
    p.click(varis[2][0], varis[2][1])  # 더베이 이동
    p.click(varis[b][0], varis[b][1] + the)  # 해당 값 입력 위치클릭
    p.hotkey("ctrl", "v")  # 붙여넣기


# right click to copy and paste
def rightclicktocopypaste(a, b, tao, the):  # a 변수 위치에서 copy하고 b 변수 위치에서 paste
    p.click(varis[1][0], varis[1][1])  # taobao웹사이트로 이동
    p.rightClick(varis[8][0], varis[8][1] + tao)  # 이미지 위치로 이동하여 우클릭
    p.click(varis[a][0], varis[a][1] + tao)  # 복사 완료
    p.click(varis[2][0], varis[2][1])  # 더베이 이동
    p.click(varis[b][0], varis[b][1] + the)  # 해당 값 입력 위치클릭
    p.hotkey("ctrl", "v")  # 붙여넣기


# input the name
def input_name():
    name = varis[20] + ' ' + varis[21]  # YANG HONGJU
    c.copy(name)
    p.click(varis[22][0], varis[22][1])
    p.hotkey("ctrl", "v")  # 붙여넣기


# 한 개의 주문번호의 아래것들 전부 입력

for i in range(varis[12]):
    # 드래그하여 입력하는 것들
    for j in range(3, 8):  # 3,4,5,6,7
        scrolltocopypaste(j, j + 10, i * varis[11], i * varis[23])

        # 우클릭하여 입력하는 것들
    for k in range(9, 11):  # 9,10
        rightclicktocopypaste(k, k + 9, i * varis[11], i * varis[23])

    # 이름 입력
    input_name()






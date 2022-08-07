# pythonAutoProject (미완)

타오바오에서 직구를 했는데, 배송 대행 사이트에 품목 하나하나 입력하려니 시간도 많이 걸리고 목이 아프다. \
파이썬 pyautogui module을 이용하여 오토마우스로 배송 대행 사이트에 자동으로 물품 정보를 입력하는 프로젝트. \
추후에 웹 html를 이용한 크롤링, AI 이미지 인식을 통한 물품 정보 자동 입력도 구현해볼 것.


![타오바오](https://user-images.githubusercontent.com/108166692/183011044-94141cb8-284c-4338-9019-28f7d33a400f.PNG)
<br>
<br>
<br>
---
<br>
[개발 기간] :  2022/8/5, 2022/8/7 <br> <br>

기능 및 사용 설명서
1) 개인 컴퓨터 환경에 따라 오토마우스를 적용해야 할 좌표 위치가 다르다.<br>
따라서, List를 이용하여 script에서 직접 x,y 위치를 바꿀 수 있다. <br><br>

2) 

[사용한 라이브러리]
import pyautogui as p #파이썬 오토마우스 모듈. 길어서 p라고 줄여서 사용한다.
~import time #시간 제어 모듈. 오토마우스 속도가 너무 빠를 경우 시간 딜레이를 줄 수 있다.~
import pyperclip as pc #한글 복사 붙이기 모듈
import keyboard as k #키보드 제어
import clipboard as c #클립보드 사용




[기능 추가] : 

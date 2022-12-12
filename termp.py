import random
import cv2

gawi = cv2.imread("gawi.jpg",cv2.IMREAD_ANYCOLOR)
bawi = cv2.imread("bawi.jpg",cv2.IMREAD_ANYCOLOR)
bo = cv2.imread("bo.jpg", cv2. IMREAD_ANYCOLOR)


abc = ["가위","바위","보"]
play = int(input("가위바위보를 할 준비가 됐으면 1번을 누르세요"))
if play==1:
  while True:
    computer = random.choice(abc)
   print("가위바위보 중 하나를 내세요,가위바위보를 그만 두려면 그만을 입력하세요"))
    if player == '그만':
      break
    if player=='가위':
      if computer == '가위':
        cv2.imshow("gawi",gawi)
        cv2.waitkey()
        cv2.destroyAllwindow()
        print('컴퓨터는 가위를 냈습니다')
        print('무승부')
      elif computer == '바위':
        cv2.imshow("gawi",bawi)
        cv2.waitkey()
        cv2.destroyAllwindow()
        print("컴퓨터는 바위을 냈습니다")
        print("패배")
      elif computer == '보':
        cv2.imshow("bo",bo)
        cv2.waitkey()
        cv2.destroyAllwindow()
        print("컴퓨터는 보를 냈습니다")
        print("승리")
            
    if player=='바위':
      if computer == '가위':
        cv2.imshow("gawi",gawi)
        cv2.waitkey()
        cv2.destroyAllwindow()
        print('컴퓨터는 가위를 냈습니다')
        print('승리')
      elif computer == '바위':
        cv2.imshow("gawi",bawi)
        cv2.waitkey()
        cv2.destroyAllwindow()
        print("컴퓨터는 바위을 냈습니다")
        print("무승부")
      elif computer == '보':
        cv2.imshow("bo",bo)
        cv2.waitkey()
        cv2.destroyAllwindow()
        print("컴퓨터는 보를 냈습니다")
        print("패배")
      
    if player=='보':
      if computer == '가위':
        cv2.imshow("gawi",gawi)
        cv2.waitkey()
        cv2.destroyAllwindow()
        print('컴퓨터는 가위를 냈습니다')
        print('패배')
      elif computer == '바위':
        cv2.imshow("gawi",bawi)
        cv2.waitkey()
        cv2.destroyAllwindow()
        print("컴퓨터는 바위을 냈습니다")
        print("승리")
      elif computer == '보':
        cv2.imshow("bo",bo)
        cv2.waitkey()
        cv2.destroyAllwindow()
        print("컴퓨터는 보를 냈습니다")
        print("무승부")
 

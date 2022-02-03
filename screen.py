import cv2
from cv2 import LINE_AA 

line_color = (0, 255, 0)
text_color = (255,0,0)

def print_players(img,players):
    cv2.putText(img,players[0],org=(1,25),fontFace = cv2.FONT_HERSHEY_DUPLEX,fontScale=1, color= text_color, thickness=1,
        lineType= cv2.LINE_AA, bottomLeftOrigin=False)
        
    cv2.putText(img,players[1],org=(img.shape[0], 25),fontFace = cv2.FONT_HERSHEY_DUPLEX,fontScale=1, color= text_color, thickness=1,
    lineType= cv2.LINE_AA, bottomLeftOrigin=False)

def print_divider(img):
    start_point = (int(img.shape[1]/2), img.shape[0])
    end_point = (int(img.shape[1]/2),0)
    cv2.line(img, start_point, end_point, line_color, 1)

def print_winner(img,player):
    if player == "Empate":
        text = player
    else:
        text = f"{player} VENCEU !!!"
    coord = int(img.shape[0]/2 -len(text)), int(img.shape[0]/2)

    cv2.putText(img,text,org=coord,fontFace = cv2.FONT_HERSHEY_DUPLEX,fontScale=1, color= (0,0,255), thickness=2,
    lineType= cv2.LINE_AA, bottomLeftOrigin=False)

def print_default_screen(img,players):
    print_divider(img)
    print_players(img,players)
import cv2
from numpy import ones,zeros

line_color = (0, 255, 0)
text_color = (255,0,0)

def get_prop(text):
    return len(text) * 11

def create_white_image(dim = (640,480,3)):
    return ones(dim) * 255     

def create_black_image(dim = (640,480,3)):
    return zeros(dim)

def print_initial_screen(winName):
    img = cv2.imread("img\jo_ken_po_inital.jpg")
    text = "Developed by Italo Piovan"
    cv2.putText(img,text,org=(0, img.shape[0]-5),fontFace = cv2.FONT_HERSHEY_DUPLEX,fontScale=0.3, color= (255,255,255), thickness=1,
        lineType= cv2.LINE_AA, bottomLeftOrigin=False)
    cv2.imshow(winName,img)
    cv2.waitKey(3000)

def print_final_screen(winName,dim, winner, player1, player2):
    img = create_white_image(dim)
    
    text = "Jo Ken Po"
    x = int(img.shape[1]/2 - get_prop(text))
    part = img.shape[0] /3

    y = 30
    cv2.putText(img,text,org=(x,y),fontFace = cv2.FONT_HERSHEY_DUPLEX,fontScale=1, color= (0,0,0), thickness=2,
        lineType= cv2.LINE_AA, bottomLeftOrigin=False)
    
    text = "Vencedor:" + winner
    x = int(img.shape[1]/2 - get_prop(text))
    y += y

    cv2.putText(img,text,org=(x,int(y)),fontFace = cv2.FONT_HERSHEY_DUPLEX,fontScale=1, color= (0,0,0), thickness=2,
        lineType= cv2.LINE_AA, bottomLeftOrigin=False)
    
    text = f"{player1['name']}: {player1['score']} pts"
    x = int(img.shape[1]/2 - get_prop(text))
    y += part

    cv2.putText(img,text,org=(x,int(y)),fontFace = cv2.FONT_HERSHEY_DUPLEX,fontScale=1, color= (0,0,0), thickness=2,
        lineType= cv2.LINE_AA, bottomLeftOrigin=False)
    
    text = f"{player2['name']}: {player2['score']} pts"
    x = int(img.shape[1]/2 - get_prop(text))
    y += part

    cv2.putText(img,text,org=(x,int(y)),fontFace = cv2.FONT_HERSHEY_DUPLEX,fontScale=1, color= (0,0,0), thickness=2,
        lineType= cv2.LINE_AA, bottomLeftOrigin=False)
    
    text = "Developed by Italo Piovan"
    cv2.putText(img,text,org=(0, img.shape[0]-5),fontFace = cv2.FONT_HERSHEY_DUPLEX,fontScale=0.5, color= (0,0,0), thickness=1,
        lineType= cv2.LINE_AA, bottomLeftOrigin=False)

    cv2.imshow(winName,img)
    cv2.waitKey(3000)

def spell_jokenpo(winName, img, dim, black = False):
    if black:
        img = create_black_image(dim)
    
    text = "Jo Ken Po"
    
    x = int(img.shape[0]/2 - get_prop(text))
    part = img.shape[1] /3
    y = 30 
    text_color = (0,255,255)
    
    cv2.putText(img,"Jo",org=(int(img.shape[1]/2),y),fontFace = cv2.FONT_HERSHEY_DUPLEX,fontScale=2, color= text_color, thickness=2,
        lineType= cv2.LINE_AA, bottomLeftOrigin=False)
    cv2.imshow(winName,img)
    cv2.waitKey(2500)

    y += part 
    cv2.putText(img,"Ken",org=(int(img.shape[1]/2),int(y)),fontFace = cv2.FONT_HERSHEY_DUPLEX,fontScale=2, color= text_color, thickness=2,
        lineType= cv2.LINE_AA, bottomLeftOrigin=False)
    cv2.imshow(winName,img)
    cv2.waitKey(2500)
    
    y += part
    cv2.putText(img,"Pooooooo",org=(int(img.shape[1]/2),int(y)),fontFace = cv2.FONT_HERSHEY_DUPLEX,fontScale=2, color= text_color, thickness=2,
        lineType= cv2.LINE_AA, bottomLeftOrigin=False)
    cv2.imshow(winName,img)
    cv2.waitKey(1000)


def print_round(img, round):
    x = int(img.shape[1]/2 - get_prop("Rodada"))
    y = 25
    cv2.putText(img,"Rodada",org=(x,y),fontFace = cv2.FONT_HERSHEY_DUPLEX,fontScale=1, color= text_color, thickness=1,
        lineType= cv2.LINE_AA, bottomLeftOrigin=False)
    x = int(img.shape[1]/2 - 11) 
    y += y
    cv2.putText(img,str(round),org=(x,y),fontFace = cv2.FONT_HERSHEY_DUPLEX,fontScale=0.8, color= text_color, thickness=1,
    lineType= cv2.LINE_AA, bottomLeftOrigin=False)
    
def print_score_players(img, player1_score, player2_score):
    cv2.putText(img,f"Pontos:{player1_score}",org=(1,55),fontFace = cv2.FONT_HERSHEY_DUPLEX,fontScale=1, color= text_color, thickness=1,
        lineType= cv2.LINE_AA, bottomLeftOrigin=False)
    cv2.putText(img,f"Pontos:{player2_score}",org=(img.shape[0], 55),fontFace = cv2.FONT_HERSHEY_DUPLEX,fontScale=1, color= text_color, thickness=1,
        lineType= cv2.LINE_AA, bottomLeftOrigin=False)

def print_players(img,players):
    cv2.putText(img,players[0][0],org=(1,25),fontFace = cv2.FONT_HERSHEY_DUPLEX,fontScale=1, color= text_color, thickness=1,
        lineType= cv2.LINE_AA, bottomLeftOrigin=False)
    cv2.putText(img,players[1][0],org=(img.shape[0], 25),fontFace = cv2.FONT_HERSHEY_DUPLEX,fontScale=1, color= text_color, thickness=1,
    lineType= cv2.LINE_AA, bottomLeftOrigin=False)
    print_score_players(img, players[0][1], players[1][1])

def print_divider(img):
    start_point = (int(img.shape[1]/2), img.shape[0])
    end_point = (int(img.shape[1]/2),55)
    cv2.line(img, start_point, end_point, line_color, 1)

def print_winner(img,player):
    if player == "Empate":
        text = player
    else:
        text = f"{player} VENCEU !!!"
    coord = int(img.shape[0]/2 -len(text)), int(img.shape[0]/2)

    cv2.putText(img,text,org=coord,fontFace = cv2.FONT_HERSHEY_DUPLEX,fontScale=1, color= (0,0,255), thickness=2,
    lineType= cv2.LINE_AA, bottomLeftOrigin=False)

def print_default_screen(img,players,round = 0):
    print_divider(img)
    print_players(img,players)
    print_round(img,round)
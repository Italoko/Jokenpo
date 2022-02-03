import cv2
import time
import mediapipe as mp
import hands_detector as detector

from  jokenpo_moviments import get_movimento
from screen import print_default_screen, print_winner

#Settings mp
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    model_complexity=0, 
    min_detection_confidence=0.8, 
    min_tracking_confidence=0.8,
    max_num_hands = 2)

# Define a janela de exibição das imagens, com tamanho manual e em tela cheia
winName = 'Jokenpo'
cv2.namedWindow(winName, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(winName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

def print_fps(image,current_time, prev_time):
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time
    #cv2.putText(image,f'FPS: {str(int(fps))}',(1,15),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0),2)
    print(int(fps))
    return image, current_time

def set_players(p1 = "Player1", p2 = "Player2"):
    return [{'name': p1, 'hand': None, 'hand_side': None, 'moviment': None, 'score':0}, {'name': p2,'hand': None,'hand_side': None,'moviment': None,'score':0}]

def jokenpo(mov_player1, mov_player2):
    #Consider valid moves ["Pedra", "Papel", "Tesoura"]
    
    #Identificação do ganhador.
    #0  - player 1
    #1  - player 2
    #-1 - empate

    if mov_player1 != mov_player2:
        if mov_player1 +1 == mov_player2:
            return 1 
        elif mov_player2 +1 == mov_player1:
            return 0
        elif mov_player1 == 2 and  mov_player2 == 0:
            return 1
        else:
            return 0
    else:
        return -1  

def main():
    cap = cv2.VideoCapture(0)
    prev_time = time.time() #For FPS    

    players = set_players()
    player_1 = players[0]
    player_2 = players[1]

    with hands:
        while cap.isOpened():
            success, img = cap.read()
            if not success:
                print("Error capturing camera image")
                break
            
            print_default_screen(img,[player_1['name'], player_2['name']])

            result = detector.hands_detector(hands,img)
            if result.multi_hand_landmarks:  
                
                #Identifica as mãos, e qual lado estão em relação à tela.
                hand_1 = detector.get_hand(result,0)
                hand_side_1 = detector.get_hand_side(hand_1,img.shape[1], img.shape[0])

                hand_2 = detector.get_hand(result,1)
                hand_side_2 = detector.get_hand_side(hand_2,img.shape[1], img.shape[0])

                #Valida se as duas mãos foram identificadas.
                if hand_1 and hand_2:
                    img = detector.draw_hand_connections(img,result,mp_hands,mp_drawing)
                    #Atribui as mãos aos respectivos jogadores.
                    if hand_side_1 == "Left":
                        player_1['hand'] = hand_1
                        player_1['hand_side'] = hand_side_1

                        player_2['hand'] = hand_2
                        player_2['hand_side'] = hand_side_2
                    else:
                        player_1['hand'] = hand_2
                        player_1['hand_side'] = hand_side_2

                        player_2['hand'] = hand_1
                        player_2['hand_side'] = hand_side_1

                    time.sleep(1)
                    player_1['moviment'] = get_movimento(player_1['hand'],player_1['hand_side'],img.shape[1])
                    player_2['moviment'] = get_movimento(player_2['hand'],player_2['hand_side'],img.shape[1])
                    
                    jokenpo_result = jokenpo(player_1['moviment'][0], player_2['moviment'][0])
                    if jokenpo_result == -1:
                        print_winner(img,"Empate")
                    else:
                        winner_player = players[jokenpo_result]
                        print_winner(img,winner_player['name'])
                    cv2.imshow(winName,img)
                    cv2.waitKey(5000)    
                else: 
                    hand_1 = None
                    hand_2 = None
                    print("only one hand detected")

            else: print("undetected hands")

            cv2.flip(img, 1)
            cv2.imshow(winName,img)
            _, prev_time = print_fps(img,time.time(),prev_time)

            if cv2.waitKey(1) & 0xFF == 27:
                break
    cap.release()
    
if __name__ == "__main__":
    main()
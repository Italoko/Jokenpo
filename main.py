import cv2
import time
import mediapipe as mp
import hands_detector as detector

from  jokenpo_moviments import get_movimento
from screen import print_default_screen, print_winner, print_initial_screen, print_final_screen, spell_jokenpo
from util import menu , set_players, print_fps, get_winner

#Settings mp
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    model_complexity=0, 
    min_detection_confidence=0.8, 
    min_tracking_confidence=0.8,
    max_num_hands = 2)

winName = 'Jokenpo'
# Define a janela de exibição em tela cheia
#cv2.namedWindow(winName, cv2.WINDOW_NORMAL)
#cv2.setWindowProperty(winName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

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
    res = menu()
    max_rounds = res[1]
    if not res[0]:
        players = set_players()
    else:
        players = set_players(res[0][0],res[0][1])

    player_1 = players[0]
    player_2 = players[1]

    round = 1

    spelling = False # True - Soletra "Jo ken Pooo"
    spell = True 

    cap = cv2.VideoCapture(0)
    prev_time = time.time() #For FPS  
    with hands:
        print_initial_screen(winName)
        while cap.isOpened() and round <= max_rounds:
            success, img = cap.read()
            if not success:
                print("Error capturing camera image")
                break
            
            print_default_screen(img,[(player_1['name'], player_1['score']), (player_2['name'], player_2['score'])],round)
            
            if spelling and spell:
                spell_jokenpo(winName, img, img.shape) #Faz a contagem fundo da imagem da câmera
                #spell_jokenpo(winName, img, img.shape, black=True) #black= True Faz a contagem em um fundo preto
                spell = False

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
                        winner_player['score'] += 1
                        print_winner(img,winner_player['name'])
                    cv2.imshow(winName,img)
                    cv2.waitKey(2000)
                    round += 1
                    if spelling: spell = True
                else: 
                    hand_1 = None
                    hand_2 = None
                    print("only one hand detected")
            else: print("undetected hands")

            #cv2.flip(img, 1)
            cv2.imshow(winName,img)
            _, prev_time = print_fps(img,time.time(),prev_time)

            if cv2.waitKey(1) & 0xFF == 27:
                break
        print_final_screen(winName,img.shape,get_winner(players),player_1,player_2)
        cv2.waitKey(0)
    cap.release()
    
if __name__ == "__main__":
    main()
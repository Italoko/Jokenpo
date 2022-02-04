import time
def print_fps(image,current_time, prev_time):
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time
    #cv2.putText(image,f'FPS: {str(int(fps))}',(1,15),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0),2)
    print(f"FPS: {int(fps)}")
    return image, current_time

def menu_players():
    info = input("Deseja informar o nome dos jogadores? (S/N): ")

    while info.lower() != "s" and info.lower() != "n": 
        print("Não entendi, por favor digite S para sim, N para Não")
        info = input("Deseja informar o nome dos jogadores? (S/N): ")
    
    if info.lower() == "s":
        print("ok, me diga quem irá jogar...")
        p1 = input("Quem será o player 1?   ")
        p2 = input("Quem será o player 2?   ")
        return (p1, p2)
    return False

def menu_rounds():
    qtd_round = 3
    info = input("Deseja informar qtd de rodadas? (por padrão é melhor de 3) (S/N): ")

    while info.lower() != "s" and info.lower() != "n": 
        print("Não entendi, por favor digite S para sim, N para Não")
        info = input("Deseja informar qtd de rodadas? (por padrão é melhor de 3) (S/N):")
    
    if info.lower() == "s":
        qtd = int(input("Quantas rodadas irão jogar?  "))
        if qtd > 0:
            qtd_round = qtd
    return qtd_round

def menu():
    print("--------- JOOOOO KEEEEEEN PÔÔÔOOOOOO ------- ")
    return (menu_players() , menu_rounds())
    
def set_players(p1 = "Player1", p2 = "Player2"):
    return [{'name': p1, 'hand': None, 'hand_side': None, 'moviment': None, 'score':0}, {'name': p2,'hand': None,'hand_side': None,'moviment': None,'score':0}]

def get_winner(players):
    if players[0]['score'] != players[1]['score']:
        if players[0]['score'] > players[1]['score']:
            return players[0]['name']
        else:
            return players[1]['name']  
    return "Empate"
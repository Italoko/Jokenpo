def main():
   
    movimentos = ["Pedra", "Papel", "Tesoura"]

    while 1:
        mov_player1 = int(input("Mov player 1:"))
        mov_player2 = int(input("Mov player 2:"))

        movimento_dos_players = [(movimentos[mov_player1], mov_player1), (movimentos[mov_player2], mov_player2)]

        print(f"Jogada: {movimentos[mov_player1]} x {movimentos[mov_player2]}")
        
        if mov_player1 != mov_player2:
            if mov_player1 +1 == mov_player2:
                print(f"Vencedor: {movimento_dos_players[1]}")
            elif mov_player2 +1 == mov_player1:
                print(f"Vencedor: {movimento_dos_players[0]}")
            elif mov_player1 == 2 and  mov_player2 == 0:
                print(f"Vencedor: {movimento_dos_players[1]}")
            else:
                print(f"Vencedor: {movimento_dos_players[0]}")
        else:
            print("Empate")    

if __name__ == "__main__":
    main()
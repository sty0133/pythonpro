# 초기 게임 보드
board = [" " for _ in range(9)]

# 게임 보드 그리기
def draw_board(board):
    print(f"\t{board[0]} | {board[1]} | {board[2]}")
    print("\t---------")
    print(f"\t{board[3]} | {board[4]} | {board[5]}")
    print("\t---------")
    print(f"\t{board[6]} | {board[7]} | {board[8]}")

# 이기는 조건
def check_win(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# 빈 칸 찾기
def get_empty_cells(board):
    return [i for i in range(9) if board[i] == " "]

# # 미니맥스 알고리즘
def minimax(board, depth, is_maximizing):
    scores = {
        "X": -1,
        "O": 1,
        "tie": 0
    }
    
    if check_win(board, "O"):
        return scores["O"]
    if check_win(board, "X"):
        return scores["X"]
    if " " not in board:
        return scores["tie"]
    
    if is_maximizing:
        max_eval = -float("inf")
        best_move = -1
        for cell in get_empty_cells(board):
            board[cell] = "O"
            eval = minimax(board, depth + 1, False)
            board[cell] = " "
            if eval > max_eval:
                max_eval = eval
                best_move = cell

        return max_eval
    else:
        min_eval = float("inf")
        for cell in get_empty_cells(board):
            board[cell] = "X"
            eval = minimax(board, depth + 1, True)
            board[cell] = " "
            min_eval = min(min_eval, eval)
        return min_eval

# 컴퓨터의 최적 수 선택
def best_move(board):
    best_score = -float("inf")
    best_move = -1
    for cell in get_empty_cells(board):
        board[cell] = "O"
        move_score = minimax(board, 0, False)
        board[cell] = " "
        if move_score > best_score:
            best_score = move_score
            best_move = cell
    return best_move

# 게임 시작
def start_game():
    player_starts = input("Do you require the first move? <y/n>:")
    
    if player_starts != "y":
        player_starts = False
    else:
        player_starts = True
    
    return player_starts

# 게임 실행
def play_game():
    #인트로
    print("\tWelcom to the greatest intellectual challenge of all time: Tic-Tac-Toe.\n\tThis will be a showdown between your human brain and my silicon processor.\n\n\tYou will make your move know by entering a number, 0 - 8. The number\n\twill correspond to the board position as illustrated:\n\n\t\t0 | 1 | 2\n\t\t---------\n\t\t3 | 4 | 5\n\t\t---------\n\t\t6 | 7 | 8\n\n\tPrepare yourself, human. The ultimate battle is about to begin.\n\n")
    current_player = "X"
    game_over = False
    
    whos_fst = start_game()
    fst = 1 if whos_fst else 0
    if fst == 1:
        while not game_over:
            
            if current_player == "X":
                position = int(input("\nWhere will you move? <0 - 8>: "))
                print("Fine..\n")

                
                if position < 0 or position > 8 or board[position] != " ":
                    print("Invalid move. Try again.")
                    continue
            else:
                position = best_move(board)
                print(f"\nI shall take square number {position}\n")
            
            board[position] = current_player
            draw_board(board)
            
            if check_win(board, current_player):
                if current_player == "X":
                    print("\nX won!\n\nNo, no! It cannot be! Somehow you tricked me, humen.\nBut never again! I, the computer, so swears it!")
                    input("\n\nPress the enter key to quit.")
                else:
                    print("\nO won!\n\nAs I predicted, human, I am triumphant once more.\nProof that computers are superior to humans in all regards.")
                    input("\n\nPress the enter key to quit.")
                game_over = True
            elif " " not in board:
                print("\nTie!")
                input("\n\nPress the enter key to quit.")
                game_over = True
            else:
                current_player = "O" if current_player == "X" else "X"
    else:
        while not game_over:
        
            if current_player == "X":
                position = best_move(board)
                print(f"\nI shall take square number {position}\n")
                
                if position < 0 or position > 8 or board[position] != " ":
                    print("Invalid move. Try again.")
                    continue
            else:
                position = int(input("\nWhere will you move? <0 - 8>: "))
                print("Fine..\n")
            
            board[position] = current_player
            draw_board(board)
            
            if check_win(board, current_player):
                if current_player == "X":
                    print("\nX won!\n\nNo, no! It cannot be! Somehow you tricked me, humen.\nBut never again! I, the computer, so swears it!")
                    input("\n\nPress the enter key to quit.")
                else:
                    print("\nO won!\n\nAs I predicted, human, I am triumphant once more.\nProof that computers are superior to humans in all regards.")
                    input("\n\nPress the enter key to quit.")
                game_over = True
            elif " " not in board:
                print("\nTie!")
                input("\n\nPress the enter key to quit.")
                game_over = True
            else:
                current_player = "O" if current_player == "X" else "X"

play_game()
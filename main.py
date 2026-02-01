import random
from judge_engine import get_judgment

def start_game():
    state = {"bomb_used": False, "user_score": 0, "bot_score": 0}
    rounds = 3

    print("=== WELCOME TO THE AI JUDGE ARENA ===")
    print("Rules: Rock, Paper, Scissors, and one BOMB.")

    for i in range(1, rounds + 1):
        print(f"\n[ ROUND {i} ]")
        user_input = input("Your move: ")
        bot_move = random.choice(["rock", "paper", "scissors", "bomb"])

        result = get_judgment(user_input, bot_move, state["bomb_used"])

        # Update Game State
        if result["bomb_spent"]:
            state["bomb_used"] = True
        
        if result["winner"] == "User": state["user_score"] += 1
        elif result["winner"] == "Bot": state["bot_score"] += 1

        print(f"User played: {result['intent'].upper()} ({result['status']})")
        print(f"Bot played: {bot_move.upper()}")
        print(f"Judge: {result['explanation']}")

    print("\n" + "="*25)
    print(f"FINAL SCORE: User {state['user_score']} | Bot {state['bot_score']}")
    if state["user_score"] > state["bot_score"]: print("FINAL RESULT: YOU WIN!")
    elif state["bot_score"] > state["user_score"]: print("FINAL RESULT: BOT WINS!")
    else: print("FINAL RESULT: IT'S A DRAW!")

if __name__ == "__main__":
    start_game()
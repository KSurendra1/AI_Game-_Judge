# AI Game Judge: Rock-Paper-Scissors Plus

A robust, AI-powered judging system for an enhanced version of Rock-Paper-Scissors. This project leverages Google Gemini to interpret natural language player intent and enforce game logic through structured prompting.

## 🚀 Key Features
- **Intent Recognition:** Moves beyond simple keyword matching. It understands semantic meaning, identifying phrases like "I'll smash it with a heavy stone" as a rock move.
- **State-Aware Judging:** Explicitly tracks the one-time usage of the bomb move via code-to-prompt state injection to prevent hallucinations.
- **Structured Output:** Enforces a strict JSON schema for AI responses, ensuring seamless integration between LLM "reasoning" and Python "execution."

## 🛠 Architecture
The project follows a clean separation of concerns:
- **Intent Understanding (judge_engine.py):** Uses the LLM to translate messy human text into a structured game action.
- **Game Logic (main.py):** Manages the "scorecard"—tracking rounds, scores, and the persistent state of the "Bomb" ability.
- **Response Generation (prompts.py):** Centralizes the "Rules of the World" in a single System Prompt, allowing for game-balance tweaks without touching code.

## 🧠 Design Philosophy
### Why this structure?
- **Decoupling:** I treated the AI as a "Stateless Judge." By passing the bomb_already_used status as a boolean in every request, I eliminated the risk of the AI "forgetting" the game state during a session.
- **Fail-Safe Mechanisms:** The system includes a Python-level fallback. If the LLM generates a malformed response, the code defaults to a safe INVALID state rather than crashing the game.
- **Prompt as a Protocol:** The prompt isn't just a list of instructions; it's a protocol that defines the required JSON structure. This makes the AI act as a reliable internal API.

## 🛡 Failure Cases Handled
- **Double Bombing:** Detects bomb_used: True and marks move INVALID, user wastes turn.
- **Ambiguity:** "I'll choose the best one." Marks move UNCLEAR, user wastes turn.
- **Creative Input:** "Throwing a sharp blade!" Interprets as VALID (Scissors).
- **Malformed JSON:** Python try-except defaults to INVALID to prevent crash.

## 📈 Future Improvements
- **Contextual Memory:** Passing round history into the prompt to allow the Judge to comment on player patterns.
- **Few-Shot Prompting:** Adding specific edge-case examples in the system prompt to sharpen accuracy.
- **Personality Profiles:** Implementing different "Judge Personas" (e.g., Sarcastic Robot vs. Formal Referee).

## ⚙️ Setup
### Install dependencies:
```bash
pip install -r requirements.txt
```
### API Configuration:
Add your Gemini API Key to judge_engine.py.
### Run the game:
```bash
python main.py
```

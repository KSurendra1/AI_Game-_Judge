import google.generativeai as genai
import json
import prompts

# Add your key here or set as an environment variable
genai.configure(api_key="AIzaSyC3ESAmPUZlUB7_Q1X0cC_FjAZJG5pMFc8")
model = genai.GenerativeModel('gemini-1.5-flash')

def get_judgment(user_text, bot_move, bomb_already_used):
    context = f"""
    User Input: "{user_text}"
    Bot Move: "{bot_move}"
    State: bomb_already_used = {bomb_already_used}
    """
    
    try:
        response = model.generate_content([prompts.SYSTEM_PROMPT, context])
        # Strip potential markdown code blocks
        clean_json = response.text.replace('```json', '').replace('```', '').strip()
        return json.loads(clean_json)
    except Exception as e:
        return {
            "intent": "error", "status": "INVALID", 
            "winner": "Bot", "explanation": "System error in judgment.", 
            "bomb_spent": False
        }
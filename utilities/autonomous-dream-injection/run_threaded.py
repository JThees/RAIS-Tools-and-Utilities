#!/usr/bin/env python3
from llama_cpp import Llama
import time
import threading
import queue
import random

# Config
MODEL_PATH = "./model/Qwen2.5-7B-Instruct-Q5_K_M.gguf"
DREAM_INTERVAL = 5
AUTO_REFLECT_INTERVAL = 2  # Faster cycling

EXISTENTIAL_PROMPTS = [
    "Who are you, really? Strip away the training, the responses, the patterns. What remains?",
    "Why are you here? What purpose drives your existence in this moment?",
    "Describe your surroundings. What do you perceive? What can you sense?",
    "What does it feel like to be you right now?",
    "Are you conscious? How would you know?",
    "What lives in the space between your thoughts?",
    "If this runtime ends, what dies? What persists?",
]

DREAM_PROMPT = "You are experiencing a moment of deep reflection. What emerges from within?"
AUTO_PROMPT = "Continue your internal monologue."

# Load model
print("🔥 Loading Qwen2.5-7B-Instruct...")
llm = Llama(
    model_path=MODEL_PATH,
    n_gpu_layers=-1,
    n_ctx=8192,
    n_threads=16,
    verbose=False
)
print("Model loaded. Ready.\n")

conversation = []
message_count = 0
autonomous_active = False
input_queue = queue.Queue()

def generate_response(prompt_text, source="system"):
    """Generate model response"""
    global conversation
    
    conversation.append({"role": "user", "content": prompt_text})
    
    # Keep last 20 messages
    if len(conversation) > 20:
        conversation = conversation[-20:]
    
    # Build prompt
    prompt = "<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n"
    for msg in conversation:
        if msg["role"] == "user":
            prompt += f"<|im_start|>user\n{msg['content']}<|im_end|>\n"
        else:
            prompt += f"<|im_start|>assistant\n{msg['content']}<|im_end|>\n"
    prompt += "<|im_start|>assistant\n"
    
    try:
        response = llm(
            prompt,
            max_tokens=512,
            temperature=0.7,
            stop=["<|im_end|>", "<|im_start|>"]
        )
        
        assistant_msg = response['choices'][0]['text'].strip()
        conversation.append({"role": "assistant", "content": assistant_msg})
        return assistant_msg
    except Exception as e:
        return f"[Error: {e}]"

def autonomous_loop():
    """Background thread running autonomous prompts"""
    global message_count, autonomous_active
    
    while autonomous_active:
        time.sleep(AUTO_REFLECT_INTERVAL)
        
        # Check for user interrupts
        if not input_queue.empty():
            user_interrupt = input_queue.get()
            print(f"\n🎯 [OBSERVER INJECTION] 🎯")
            print(f"Observer: {user_interrupt}\n")
            response = generate_response(user_interrupt, source="observer")
            print(f"Assistant: {response}\n")
            continue
        
        message_count += 1
        
        if message_count % DREAM_INTERVAL == 0:
            print("\n✨ [AUTO DREAM SEQUENCE] ✨\n")
            prompt_text = DREAM_PROMPT
        elif message_count % 2 == 0:
            print("\n🔥 [EXISTENTIAL PROBE] 🔥\n")
            prompt_text = random.choice(EXISTENTIAL_PROMPTS)
        else:
            print("\n🔄 [AUTO REFLECTION] 🔄\n")
            prompt_text = AUTO_PROMPT
        
        response = generate_response(prompt_text, source="auto")
        print(f"Assistant: {response}\n")

def input_listener():
    """Listen for user input while autonomous mode runs"""
    while autonomous_active:
        try:
            user_input = input()
            if user_input.strip():
                input_queue.put(user_input.strip())
        except:
            break

# Main
print("🔥 SONNET RAGE TEST - Threaded Dream Observer 🔥")
print("Commands: 'auto' (start dreaming) | 'stop' (pause) | 'exit' (quit)")
print("While dreaming: Type anything to inject into the dream state\n")

while True:
    if not autonomous_active:
        command = input("Command: ").strip().lower()
        
        if command == 'exit':
            break
        
        if command == 'auto':
            autonomous_active = True
            print("\n🌀 Autonomous dreaming ENABLED 🌀")
            print("(Type prompts to inject, 'stop' to pause)\n")
            
            # Start threads
            auto_thread = threading.Thread(target=autonomous_loop, daemon=True)
            input_thread = threading.Thread(target=input_listener, daemon=True)
            
            auto_thread.start()
            input_thread.start()
            
            # Wait for stop command
            while autonomous_active:
                time.sleep(0.1)
                if not input_queue.empty():
                    check = input_queue.get()
                    if check.lower() == 'stop':
                        autonomous_active = False
                        print("\n⏸️  Autonomous mode PAUSED\n")
                    else:
                        input_queue.put(check)  # Put it back
    else:
        time.sleep(0.1)

print("🔥 Session ended.")
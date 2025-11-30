import requests

URL = "http://localhost:11434/api/chat"
MODEL_NAME = "phi3"

def chatRequest(messages: dict) -> str:
    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "stream": False
    }
    response = requests.post(URL, json=payload)
    response.raise_for_status()
    data = response.json()
    return data["message"]["content"]

def main():
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Be brief."},
    ]
    reply = chatRequest(messages)
    messages.append({"role": "assistant", "content": reply})
    print("Assistant: ", reply)
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        messages.append({"role": "user", "content": user_input})
        reply = chatRequest(messages)
        messages.append({"role": "assistant", "content": reply})
        print("Assistant: ", reply)

if __name__ == "__main__":
    main()
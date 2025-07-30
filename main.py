# main.py

from agnoagent.agent import SimpleAgent

def main():
    # Initialize the chatbot agent
    agent = SimpleAgent("AgnoBot")

    print("🤖 AgnoBot is ready! Type your questions (type 'exit' to quit).")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("AgnoBot: Goodbye! 👋")
            break

        response = agent.greet(user_input)
        print("AgnoBot:", response)

if __name__ == "__main__":
    main()

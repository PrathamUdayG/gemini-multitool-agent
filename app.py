from flask import Flask, render_template, request, jsonify
from agnoagent.builder import AgentBuilder

# ✅ Build the agent using the static method
agent = AgentBuilder.build_agent()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    if not user_input:
        return jsonify({"reply": "⚠️ Please enter a valid message."})

    try:
        print("👤 User asked:", user_input)

        # 🔄 Run the agent
        response = agent.run(user_input)

        print("🤖 Agent replied:", response)

        # ✅ Log what you're returning to the frontend
        print("✅ Returning JSON:", {"reply": response})

        return jsonify({"reply": response})
    except Exception as e:
        print("⚠️ ERROR:", e)
        return jsonify({"reply": f"⚠️ Internal Error: {e}"})

if __name__ == "__main__":
    app.run(debug=True)

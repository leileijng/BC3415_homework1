from flask import Flask, render_template, request
import google.generativeai as palm
import os

api = os.environ.get('GOOGLE_KEY')
palm.configure(api_key=os)
# Define the new model (replace with an appropriate model name)
model = "text-bison-001"

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"]) 
def index():
    return render_template('index.html')

@app.route("/ai_agent", methods=["GET", "POST"])
def ai_agent():
    return render_template("ai_agent.html")

@app.route("/ai_agent_reply", methods=["GET", "POST"])
def ai_agent_reply():
    q = request.form.get("q")
    response = palm.generate_text(
        model=model,
        prompt=q,
        temperature=0.7,
        max_output_tokens=200
    )
    return render_template("ai_agent_reply.html", r=response.result)

@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    return render_template("index.html")

@app.route("/sg_joke", methods=["GET", "POST"])
def sg_joke():
    response = palm.generate_text(
        model=model,
        prompt="Tell me a joke about Singapore.",
        temperature=0.7,
        max_output_tokens=50
    )
    return render_template("sg_joke.html", sg_joke=response.result)

if __name__ == "__main__":
    app.run()

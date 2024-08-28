from flask import Flask, render_template, request
import google.generativeai as palm
import google.api_core.exceptions as google_exceptions
import os

# Configure the API key
api = os.environ.get('GOOGLE_KEY')
palm.configure(api_key=api)

# Correct model name (replace with the model name you have access to)
model_name = "models/text-bison-001"  # Make sure this is the correct and accessible model name

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
    try:
        response = palm.generate_text(
            model=model_name,
            prompt=q,
            temperature=0.7,
            max_output_tokens=200
        )
        return render_template("ai_agent_reply.html", r=response.result)
    except google_exceptions.InvalidArgument as e:
        return f"Error: {str(e)}"

@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    return render_template("index.html")

@app.route("/sg_joke", methods=["GET", "POST"])
def sg_joke():
    try:
        response = palm.generate_text(
            model=model_name,
            prompt="Tell me a joke about Singapore.",
            temperature=0.7,
            max_output_tokens=50
        )
        return render_template("sg_joke.html", sg_joke=response.result)
    except google_exceptions.InvalidArgument as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run()

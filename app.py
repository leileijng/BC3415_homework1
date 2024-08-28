from flask import Flask, render_template, request
import google.generativeai as palm
import os
import openai

api = 'AIzaSyCjWNEcNHym512r1fmc0CNgq1LWSwC6iyQ'
palm.configure(api_key=api)
model = {"model": "models/chat-bison-001"}

open_api_key = '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'
os.environ['OPENAI_API_KEY'] = open_api_key
client = openai.OpenAI()

app = Flask(__name__) #confirm the app ownership

@app.route("/", methods=["GET", "POST"]) 
def index():
    return(render_template('index.html'))


@app.route("/ai_agent",methods=["GET","POST"])
def ai_agent():
    return(render_template("ai_agent.html"))


@app.route("/ai_agent_reply",methods=["GET","POST"])
def ai_agent_reply():
    q = request.form.get("q")
    r = client.chat.completions.create(
        model='gpt-3.5-turbo-0125',
        messages=[{"role": "user",
                   "content": q}])
    return(render_template("ai_agent_reply.html", r=r.choices[0].message.content))


@app.route("/prediction",methods=["GET","POST"])
def prediction():
    return(render_template("index.html"))


@app.route("/sg_joke",methods=["GET","POST"])
def sg_joke():
    r = client.chat.completions.create(
        model='gpt-3.5-turbo-0125',
        messages=[{"role": "user",
                   "content": "Tell me a joke about Singapore"}])
    return(render_template("sg_joke.html", sg_joke=r.choices[0].message.content))


if __name__ == "__main__":
    app.run()
    

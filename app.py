from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.messages.human import HumanMessage

api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chatbot.html') # extends base.html


# Test API endpoint for LangChain connecting to OpenAI
@app.route('/test_openai', methods=['POST'])
def test_openai():
    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")

    message = "How many legs does a spider have?"

    response = llm.invoke(message)
    print(response.content)

    return {
        'statusCode': 200,
        'body': response.content
    }


@app.route('/about')
def about():
    return render_template('about.html')  # Another page extending base.html


# Main entry point
if __name__ == '__main__':
    app.run(debug=True)

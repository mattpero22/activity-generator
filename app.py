from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os

load_dotenv()

from components.agent import create_openai_agent

api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

agent = create_openai_agent("gpt-4o-mini")

@app.route('/')
def index():
    return render_template('chatbot.html') # extends base.html


# Test API endpoint for LangChain connecting to OpenAI
@app.route('/test_openai', methods=['POST'])
def test_openai():
    print(request.method)

    input_text = request.json
    
    result = agent.invoke({"input": input_text})

    return {
        'statusCode': 200,
        'body': result["output"]
    }


@app.route('/about')
def about():
    return render_template('about.html')  # Another page extending base.html


# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
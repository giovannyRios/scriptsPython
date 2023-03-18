import openai
from flask import Flask
import json

app = Flask(__name__)
@app.route('/api/get', methods=['GET'])
def get():
    openai.organization = "YOUR-OPENAI_ORGANIZATION"
    openai.api_key = "YOUR_OPENAI_KEY"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Soy un asistente que brinda información"},
                {"role": "user", "content": "Hola, que información brindas"}
                ]
            )
    return response.choices[0]
    

if __name__ == '__main__':
    app.run()

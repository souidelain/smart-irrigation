from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app) # Bach l-frontend i-9der i-hder m3a l-backend

data_history = []

@app.route('/api/data', methods=['POST'])
def receive_data():
    content = request.json
    
    # Hna kiy-hder l-backend m3a l-IA
    try:
        ia_url = "http://127.0.0.1:8000/predict"
        ia_resp = requests.post(ia_url, json={
            "moisture": content['moisture'],
            "temperature": content['temperature']
        })
        prediction = ia_resp.json()
        content['pump_action'] = prediction['pump_action']
        content['reason'] = prediction['reason']
    except:
        content['pump_action'] = "OFF (IA Service Down)"

    data_history.append(content)
    print(f"Final Data: {content}") # Ghadi t-chouf ON/OFF f l-terminal
    return jsonify({"status": "success", "action": content['pump_action']}), 201

@app.route('/api/history', methods=['GET'])
def get_history():
    return jsonify(data_history), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
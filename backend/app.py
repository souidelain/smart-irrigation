
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Ghadi n-khzno l-data ghir f list muwa9atan (Memory)
data_history = []

@app.route('/api/data', methods=['POST'])
def receive_data():
    content = request.json
    # N-zidou l-wa9t dyal l-backend ga3 ila majash mn l-ESP
    content['received_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    data_history.append(content)
    print(f"Data received: {content}")
    
    return jsonify({"status": "success", "message": "Data saved"}), 201

@app.route('/api/history', methods=['GET'])
def get_history():
    return jsonify(data_history), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)

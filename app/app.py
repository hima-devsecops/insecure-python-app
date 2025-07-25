from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = '1257-password-test' 

API_KEY = "12345-he1355-3135-0152857"  

@app.route('/')
def home():
    return "Welcome to the Insecure App"

@app.route('/greet', methods=['GET'])
def greet_user():
    name = request.args.get('name') 
    return f"Hello, {name} 👋, welcome to our insecure web application!" 

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    print(f"Received: {data}")  
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True)  

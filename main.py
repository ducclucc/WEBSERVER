import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def upload_file():
    data = request.data
    with open('uploaded_file', 'wb') as f:
        f.write(data)
    return 'File saved successfully', 200

if __name__ == '__main__':
    host = os.getenv('HOST', '0.0.0.0')  # Use the HOST environment variable or default to '0.0.0.0'
    port = int(os.getenv('PORT', 5000))   # Use the PORT environment variable or default to 5000
    app.run(host=host, port=port)

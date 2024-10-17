from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def upload_file():
    # Get the raw data from the request
    data = request.data

    # Save the raw data to a file
    with open('uploaded_file', 'wb') as f:
        f.write(data)

    return 'File saved successfully', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

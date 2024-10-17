from flask import Flask, request
import requests
def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_address = response.json()['ip']
        return ip_address
    except:
        pass
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
    print(get_public_ip())
    app.run(host=input('enter your host ip: '), port=5000)

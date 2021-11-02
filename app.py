
#from boto.s3.connection import S3Connection
#s3 = S3Connection(os.environ['S3_KEY'], os.environ['S3_SECRET'])

from flask import Flask, request, jsonify
import json
import random
app = Flask(__name__)

@app.route('/roll20/', methods=['GET','POST'])
def respond():
    # Retrieve the name from url parameter
    

    # For debugging

    
    response = {}

    response["MESSAGE"] = "Your roll has landed and it has landed on "+ str((random.random()*19)+1)


    # Return the response in json format
    return jsonify(response)






@app.route('/', methods=['POST'])
def post_challenge():
    param = request.get_json()
    print(request.get_data())
    print(request.get_json())
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "challenge": param['challenge'],
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        print('reached here')
        return jsonify({
            "ERROR": "no name found, please send a this is different."
        })

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
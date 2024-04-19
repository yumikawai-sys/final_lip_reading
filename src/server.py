from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from datetime import datetime
from app.pred import sample_prediction
from conversion import convert_mp4_to_mpg

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
mongo_dbname = 'lipreading_predictions'

app = Flask(__name__)
CORS(app, resources={r"/prediction/*": {"origins": "http://localhost:5173"}})

# Connect to MongoDB using MongoClient
client = MongoClient(mongo_uri)
db = client[mongo_dbname]


# Call the model
def predict_speech(video_path):
    if video_path is None:
        return
    
    # test data
    # result = "How are you?"
    # result = "How are you?"

    result = sample_prediction(video_path)
    print('result', result)
    return(result)

# Post the prediction to MongoDB
@app.route("/prediction/new", methods=['POST'])
def extract_prediction():
    # Get 'file path' from client
    request_data = request.get_json()
    video_path = request_data.get('filePath')
    
    print('video_path_inserver', video_path)

    # Convert (mp4 -> mpg)
    output_path = "app/data/s1/converted.mpg"
    convert_mp4_to_mpg(video_path, output_path)

    # call the model to predict the speech with 'video_path'
    prediction = predict_speech(output_path)
    print('prediction', prediction)

    # Get prediction
    today_date = datetime.now().strftime('%m%d%Y')
    prediction_list = {"name": "Dean", "sendtime": today_date, "prediction": prediction}

    # Send it to MongoDB
    if prediction is not None:
        try:
            collection = db["predictions"]
            collection.insert_one(prediction_list)
        except Exception as e:
            print(f'Error saving data to MongoDB: {str(e)}')
    else:
        print('Error: Missing required keys in result entries.')

    response = jsonify(prediction)
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:5173")
    return response


# Get all predictions from MongoDB
@app.route("/predictions", methods=['GET'])
def get_predictionss():
    try:
        # Fetch all documents
        predictions = list(db["predictions"].find().sort("sendtime", -1))

        # Convert ObjectId to str for JSON serialization
        for predict in predictions:
            predict['_id'] = str(predict['_id']) 
            formatted_date = datetime.strptime(predict['sendtime'], '%m%d%Y').strftime('%b %d, %Y')
            predict['sendtime'] = formatted_date

        return jsonify(predictions)
    
    except Exception as e:
        print(f'Error: {str(e)}')
        return jsonify({'error': str(e)}), 500

@app.route("/")
def index():
    return "Welcome to the lipreading predictions API!"


if __name__ == "__main__":
    app.run(debug=True)
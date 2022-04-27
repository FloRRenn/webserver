from flask import Flask, send_file, request
from flask_cors import CORS, cross_origin
from create_meme import CreateMeme as meme
import os, io
from PIL import Image
from dotenv import load_dotenv
import pymongo
load_dotenv()

def loadDB():
    global db
    user = os.getenv("USERNAME")
    pwd = os.getenv("PASSWORD")
    clusterNAME = os.getenv("CLUSTER")
    
    cluster = pymongo.MongoClient(f"mongodb+srv://{user}:{pwd}@cluster0.fsnin.mongodb.net/test", connect = False)
    db = cluster.demo[clusterNAME]

# Init Server
app = Flask(__name__)
loadDB()

# Apply App CORS
CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
app.config["IMAGE_UPLOADS"] = "./meme/"

@app.route('/', methods = ['GET'])
def home():
    return "Hello, I'm here"

@app.route("/ping", methods = ["POST", "GET"])
@cross_origin(origin = "*")
def add():
    return "Yeah, it's me"

@app.route('/10guy', methods = ['POST', 'GET'])
@cross_origin(origin = "*")
def tenGUY():
    if request.method == 'POST':
        top_text = request.form['top']
        bottom_text = request.form['bottom']
    
    else:
        top_text = request.args['top']
        bottom_text = request.args['bottom']
    
    meme.createbyCol('10GUY.jpg', top_text, bottom_text)  
    filename = r"./result.jpg"
    return send_file(filename, mimetype='image/jpg')

@app.route('/alien', methods = ['POST', 'GET'])
@cross_origin(origin = "*")
def alien():
    if request.method == 'POST':
        top_text = request.form['top']
        bottom_text = request.form['bottom']
    
    else:
        top_text = request.args['top']
        bottom_text = request.args['bottom']
    
    meme.createbyCol('alien.jpg', top_text, bottom_text)  
    filename = r"./result.jpg"
    return send_file(filename, mimetype='image/jpg')
    
@app.route('/button', methods = ['POST', 'GET'])
@cross_origin(origin = "*")
def button():
    if request.method == 'POST':
        top_text = request.form['top']
        bottom_text = request.form['bottom']
    
    else:
        top_text = request.args['top']
        bottom_text = request.args['bottom']
    
    meme.createbyRow('button.jpg', top_text, bottom_text)  
    filename = r"./result.jpg"
    return send_file(filename, mimetype='image/jpg')

@app.route('/upload', methods = ['POST'])
@cross_origin(origin = "*")
def upload():
    username = request.form['username']
    password = request.form['password']
    
    requests = request.files
    if requests:
        image = requests['file']
        image_bytes = io.BytesIO()
        im = Image.open(image)
        im.save(image_bytes, format='JPEG')
        
        info = {
            'file' : {
                'name' : image.filename,
                'image' : image_bytes.getvalue()
            }
        }
        
        find = db.find_one({'username': username, 'password': password})
        if find:
            db.update_one({'username': username, 'password': password}, {'$set' : info})
        else:
            db.insert_one({'username': username, 'password': password, **info})
        
        return {"Message": f"Uploaded file {image.filename}"}
    
    return {"Message": "Please upload a file"}

@app.route('/getfile', methods = ['GET', 'POST'])
@cross_origin(origin = "*")
def getfile():
    username = request.args['username']
    password = request.args['password']
    file = request.args['file']
    
    find = db.find_one({'username': username, 'password': password})
    if not find:
        return {"Message": "Your login data is not in the database"}  
    
    pil_img = Image.open(io.BytesIO(find['file']['image']))
    pil_img.save(app.config["IMAGE_UPLOADS"] + find['file']['name'])
    return send_file(app.config["IMAGE_UPLOADS"] + file, mimetype='image/jpg')
    
        
if __name__ == "__main__":
    app.run(debug = True)
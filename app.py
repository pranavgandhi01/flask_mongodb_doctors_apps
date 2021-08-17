from flask import Flask
from flask import request
from bson.json_util import dumps
from db import db
from models import Doctor, Area, DoctorQuery
import json

app = Flask(__name__)

@app.route("/doctor", methods = ['POST'])
def save_doctors():
    try:
        data = json.loads(request.data)
        doctors = Doctor.fromJsonDict(data)
        statuses = {}
        for doctor in doctors:
            statuses[doctor.id] = db.Doctors.insert_one(doctor.toJson())
        return dumps({'message' : statuses})
    except Exception as e:
        return dumps({'error' : str(e)})

@app.route("/doctor", methods = ['GET'])
def get_doctors():
    try:
        district = request.args.get('district')
        category = request.args.get('category')
        maxPrice = request.args.get('maxPrice')
        minPrice = request.args.get('minPrice')
        language = request.args.get('language')
        query = DoctorQuery.filterQuery(district=district, category=category, \
            maxPrice=maxPrice, minPrice=minPrice, language=language)
        doctors = db.Doctors.find(query)
        return dumps(doctors)
    except Exception as e:
        return dumps({'error' : str(e)})

if __name__ == '__main__':
    app.run(debug=False)
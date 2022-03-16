

from sqlalchemy import create_engine
from flask import Blueprint, request, jsonify
from . import db
import json
from bson.json_util import dumps, loads

db_string = "postgresql://axnxgfoqjxzvgy:58d568841b6a8a3b601d9b455a32a1ea135c64fef08612101c27dd1cffcb821d@ec2-52-1-115-6.compute-1.amazonaws.com:5432/d7vu6ekijbukt9"


db_doctors = create_engine(db_string)
result_set = db_doctors.execute("SELECT * FROM users")


bp = Blueprint('doctors', __name__, url_prefix='/doctors')



@bp.route('', methods=['GET'])
def doctors_func():
    list_result = list(result_set)
    json_data = dumps(list_result)
    return jsonify({"username doctors": json.loads(json_data)})
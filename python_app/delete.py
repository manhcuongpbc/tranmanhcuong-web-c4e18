from flask import *
import mlab
from models.service import Service
import sys

app = Flask(__name__)

# 0. Create connection 
mlab.connect()

my_collection = db['Service']
my_collection.drop()

if __name__ == '__main__':
    app.run(debug=True)
 
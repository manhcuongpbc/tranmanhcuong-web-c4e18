from flask import Flask, render_template
import mlab
from models.service import Service
import sys

app = Flask(__name__)

# 0. Create connection 
mlab.connect()

# new_service.save()

@app.route('/')
def search():
    id_to_find = "5b2ba8f9250f4217644467cc"
    k = Service.objects.get(id= id_to_find)
    # all_service = Service.objects(gender= gender, yob__lte=1998, address__icontains='Ha noi')
    # return render_template('search.html', all_service = all_service)
    return k

if __name__ == '__main__':
    app.run(debug=True)
 
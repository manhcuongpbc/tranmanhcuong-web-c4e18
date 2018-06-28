from flask import *
import mlab
from models.service import Service
import sys

app = Flask(__name__)

# 0. Create connection 
mlab.connect()
# session.clear()
# new_service.save()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<gender>')
def search(gender):
    all_service = Service.objects(gender= gender)
    # all_service = Service.objects(gender= gender, yob__lte=1998, address__icontains='Ha noi')
    return render_template('search.html', all_service = all_service)

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html',all_service = all_service)

@app.route('/delete/<service_id>')
def delete(service_id):
    service = Service.objects.with_id(service_id)

    if service is not None:
        service.delete()
        return redirect(url_for('admin'))
    else:
        return 'not found' + service_id


@app.route('/new-service', methods = ['GET','POST'])
def create():
    if request.method == "GET":
        return render_template('new_service.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        address = form['address']

        new_service = Service(
            name = name,
            yob = yob,
            address = address,
        )

        new_service.save()
        return name + yob + address

# bai tap ve nha
@app.route('/search')
def searchh():
    all_service = Service.objects()
    return render_template('search2.html', all_service = all_service)

@app.route('/detail/<service_id>')
def detail(service_id):
    # all_service = Service.objects()
    service = Service.objects.with_id(service_id)

    return render_template('search3.html', service = service)

@app.route('/update-service/<service_id>')
def update(service_id):
    all_service = Service.objects()
    service = Service.objects.with_id(service_id)
    return render_template("update.html", service_id=service_id)

if __name__ == '__main__':
    app.run(debug=True)
 
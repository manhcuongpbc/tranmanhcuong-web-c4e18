from flask import Flask, render_template
app = Flask(__name__)

@app.route('/bmi/<float:weight>/<float:height>')
def bmi(weight, height):
    bmi_ = weight/((height/100)**2)
    if bmi_ < 16:
        return 'Severely underweight'
    elif 16 <= bmi_ < 18.5:
        return 'Underweight'
    else:
        return 'Obese'
if __name__ == '__main__':
  app.run(debug=True)
from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/')
def index():
    post_title = 'tho con coc'
    post_content = "hom nay trawng sang"
    post_author = "Manh cuong"

    posts = [
        {
        'title' : 'tho con coc',
        'content' : "hom nay trawng sang",
        'author' : "Manh cuong",
        'gender' : 0
        },
        {
        'title' : 'kho khan',
        'content' : "hlionel messi",
        'author' : "Manh cuong",
        'gender' : 1
        },
        {
        'title' : 'tho dfdfdf coc',
        'content' : "cr 7 ",
        'author' : "Manh cuong",
        'gender' : 0
        }
    ]

    # first_post = posts[0]
    # return render_template('index.html', post_title = post_title,\
    # post_content = post_content, post_author = post_author)
    return render_template('index.html', posts = posts)
@app.route('/hello')
def say_hello():
    return 'hello c4e18'

@app.route('/sayhi/<name>/<age>')
def say_hi(name, age):
    return 'hi {0}, you are {1} years old'.format(name,age)

@app.route('/sum/<int:a>/<int:b>')
def total(a, b):
    return str(a + b)

@app.route('/about-me')
def about_me():
    return render_template('aboutme.html')

@app.route('/school')
def redirect_():
    return redirect('http://techkids.vn')

if __name__ == '__main__':
  app.run(debug=True)
 
from root import app
from flask.templating import render_template




@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/')
@app.route('/login/<int:posts>')
def login(posts):
    return render_template('login.html', post=posts)






if __name__ == "__main__":
    app.run(debug=True)
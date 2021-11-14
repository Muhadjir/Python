from markupsafe import escape

from flask import Flask, request, url_for, render_template
app = Flask(__name__)

@app.route('/')
def index():
    sum=815555
    # return f'Index Page {sum}'
    return f'<h1>Index Page</h1> {sum} <p>Test 123</p>'

#Routing
@app.route('/hello')
def hello():
    return 'Hello, World'

#HTML Escaping
@app.route('/<name>')
def cek(name):
    return f"Hello, {escape(name)}!"

#Variable Rules
@app.route('/user/<username>')
def show_user_profile(username):
    return f"User {escape(username)}"

@app.route('/post/<int:post_id>')
def show_post(post_id):    
    # show the post with the given id, the id is an integer    
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):    
    # show the subpath after /path/    
    return f'Subpath {escape(subpath)}'

#Http Methods
@app.route('/login', methods=['GET', 'POST'])
def login():    
    if request.method == 'POST':        
        return do_the_login()    
    else:        
        return show_the_login_form()

#Unique URL
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

#URL_FOR
@app.route('/login')
def log():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('log'))
    print(url_for('log', next='/'))
    print(url_for('profile', username='John Doe'))

# #Static Files
# url_for('static', filename='style.css')

#Rendering Template
@app.route('/hai/')
@app.route('/hai/<name>')
def hai(name=None):
    return render_template('hai.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
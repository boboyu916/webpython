from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/voice/<name>/<int:vid>/')
def make_sound(name, vid):
    # id = id + 1
    # return (name.capitalize() + ' ') * vid
    vid = vid + 62**28
    return render_template('admin/index.html', name=name.capitalize(), vid=vid + 1)


with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('make_sound', name='boboyu', vid=2))
    print(url_for('static', filename='css/main.css'))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port='9999')

from flask import Flask, render_template, request
from sense_hat import SenseHat 

sense = SenseHat()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['POST'])
def post_message():
    message = request.form['message']
    name = request.form['name']
    display = f'{message}  Love, {name}'
    print(display)
    return render_template('received.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

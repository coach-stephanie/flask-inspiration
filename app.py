from flask import Flask, render_template, request
from sense_hat import SenseHat 

sense = SenseHat()

app = Flask(__name__)

#Decorator 
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/message', methods=['POST'])
def post_message():
    message = request.form['message']
    name = request.form['name']
    color = hex_to_rgb(request.form['color'])
    display = f'{message}  Love, {name}'
    if message == '':
       display = 'Have a nice day!'
    sense.show_message(display, text_colour=color)
    return render_template('received.html')

def hex_to_rgb(hex):
    h = hex.lstrip('#')
    return [int(h[i:i+2], 16) for i in (0, 2, 4)]

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

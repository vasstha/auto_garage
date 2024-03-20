from flask import FLask, render_template, request
import RPi.GPIO as GPIO  

app = Flask(__name__)

relay_pin = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)

#function to toggle the relay
def toggle_relay(state):
    GPIO.output(relay_pin, state)

#home route
@app.route('/')
def home():
    return render_template('index.html')

#API endpoint to control the relay
@app.route('/control', methods = ['POST'])
def control():
    state = request.form.get('state')
    if state == 'on':
        toggle_relay(GPIO.HIGH)
    elif state == 'off':
        toggle_relay(GPIO.LOW)
    return 'ok'

if __name__ == '__main__':
    app.run(debug = True, host : '0.0.0.0')
from "/Users/arpitgupta/Desktop/nyu-cs2262-001-fa20-master/sample_time_app/run.py" import "/Users/arpitgupta/Desktop/nyu-cs2262-001-fa20-master/sample_time_app/run.py"
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

app.run(host='0.0.0.0',
        port=8080,
        debug=True)


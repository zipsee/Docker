from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Docker Volume Project!'

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form['text']
    with open('/data/submissions.txt', 'a') as f:
        f.write(data + '\n')
    return 'Data submitted successfully!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


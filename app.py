#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

farms = [
    {
        'id': 1,
        'title': u'One example farm',
    },
    {
        'id': 2,
        'title': u'Another example farm',
    }
]

@app.route('/farmhelden/api/v1.0/farms', methods=['GET'])
def get_tasks():
    return jsonify({'farms': farms})

if __name__ == '__main__':
    app.run(debug=True)

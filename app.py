from flask import Flask

app = Flask(__name__)


@app.route('/recette/1')
def hello_world():  # put application's code here
    return {'data': {
        'attributes': {
            'name': 'chantilly',
            'ingredients': [
                'creme',
                'sucre',
                'arôme vanille'
            ],
            'steps': [
                'xxxx',
                'xxxx'
            ]
        }
    }}


if __name__ == '__main__':
    app.run()

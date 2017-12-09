from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


def process_data(data: str, encoding: str='utf-8'):
    formatted_data = ''
    for letter in data:
        to_add = None
        code = ord(letter)
        if code < 128:
            to_add = chr(code)
        else:
            to_add = '\\u{:04X}'.format(code)
        formatted_data += to_add
    return formatted_data


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    data = ''
    formatted_data = ''
    if request.method == 'POST':
        data = request.form['input']
        if data:
            formatted_data = process_data(data)
    return render_template('index.html', data=data, formatted_data=formatted_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

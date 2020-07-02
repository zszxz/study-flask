from flask import Flask, redirect, abort, make_response, jsonify, request

# 创建falsk 实例 对应 app.py文件
app = Flask(__name__)

@app.route('/hello/<int:year>', methods=['GET','POST'])
def hello(year):
    return 'this year is %s' % year

@app.route('/hot/<any(5,25):day>')
def any(day):
    return 'this day is %s' % day

@app.route('/register', methods=['GET','POST'])
def register():
    return 'Hello World!'

@app.route('/hello')
def status():
    return 'Hello World!', 201


@app.route('/zszxz')
def location():
    return redirect('http://www.example.com')

@app.route('/except')
def not_found():
    abort(404)

@app.route('/resp')
def responser():
    response = make_response('Hello, World!')
    response.mimetype = 'text/plain'
    return response

@app.route('/json')
def json_z():
    return jsonify({'name': 'Carrier', 'gender': 'female'})

@app.route('/set_cookie')
def set_cookie():
    response=make_response('Hello World');
    response.set_cookie('name','zszxz')
    return response

@app.route('/get_cookie')
def get_cookie():
    name=request.cookies.get('name')
    return name

@app.route('/del_cookie')
def del_cookie():
    response=make_response('delete cookie')
    response.delete_cookie('name')
    return response


if __name__ == '__main__':
    app.run()
from flask import Flask
import click



# 创建falsk 实例 对应 app.py文件
app = Flask(__name__)

@app.route('/')
# 视图函数(view function)
def hello_world():
    return 'Hello World!'

# 在第一次请求之前运行.\
@app.before_first_request
def before_first_request():
    print('在第一次请求之前运行')


# 在每一次请求前都会执行
@app.before_request
def before_request():
    print('在每一次请求前都会执行')


# 在请求之后运行
@app.after_request
def after_request(response):
    print('在请求之后运行')
    return response

# 无论视图函数是否出现异常，每一次请求之后都会调用
@app.teardown_request
def teardown_request(error):
    print('error %s' % error)

if __name__ == '__main__':
    app.run()
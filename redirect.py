from flask import Flask, url_for, redirect

# 创建falsk 实例
app = Flask(__name__)

# 路由负责URL 与 函数之间的映射
@app.route('/hello')
# 视图函数(view function)
def hello():
    return 'Hello World!'

@app.route('/tohello')
def tohello():
    return redirect(url_for('hello'))


if __name__ == '__main__':
    app.run()
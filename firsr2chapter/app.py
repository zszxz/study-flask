from flask import Flask
import click

# 创建falsk 实例 对应 app.py文件
app = Flask(__name__)

# 路由负责URL 与 函数之间的映射
@app.route('/')
# 视图函数(view function)
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

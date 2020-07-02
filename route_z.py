from flask import Flask
import click

# 创建falsk 实例 对应 app.py文件
app = Flask(__name__)

@app.route('/some')
@app.route('/many')
def mul_route():
    return '多路由'

@app.route('/zszxz/<name>')
def url_parameter(name):
    return '路径参数: %s' % name

@app.route('/zszxz',defaults={'language':'python'})
@app.route('/zszxz/<language>')
def default_parameter(language):
    return '路径参数: %s' % language

if __name__ == '__main__':
    app.run()
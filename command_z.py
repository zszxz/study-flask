from flask import Flask
import click

# 创建falsk 实例 对应 app.py文件
app = Flask(__name__)



@app.cli.command()
def hello():
    click.echo('Hello, zszxz!')

if __name__ == '__main__':
    app.run()

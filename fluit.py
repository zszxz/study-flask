from flask import Flask, app,render_template

# 创建falsk 实例
app = Flask(__name__)

@app.route('/fluit')
def to_fluit():
    data_user = {'username': 'lusy'}
    data_fluit = [
        {'name': '苹果', 'place':'山东'},
        {'name': '柿子', 'place':'广西'}
    ]
    return render_template('fruit.html', user=data_user, fluit=data_fluit)

# 自定义过滤器
@app.template_filter()
def save(var):
    return var + ' is save'

if __name__ == '__main__':
    # 开启调试
   app.run(debug = True)
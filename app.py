from flask import Flask, request

app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'])
def index():
    """
    不同方法
    :return:
    """
    if request.method == 'GET':
        print('GET')
        return "GET!"
    elif request.method == "POST":
        print("POST")
        return "POST"
    else:
        return 'METHODS IS NONE'


@app.route('/user/<username>', methods=['GET', 'POST'])
def show_username(username):
    """
    参数
    :return:
    """
    print("username", username)
    return "show username"


@app.route('/user/<int:userid>', methods=['GET', 'POST'])
def show_user_id(userid):
    """
    限制为整数类型参数
    :return:
    """
    print(userid)
    return "show user id for int"


@app.route('/user/<float:user_float>', methods=['GET', 'POST'])
def show_user_float(user_float):
    """
    限制为浮点数的参数类型
    :return:
    """
    print(user_float)
    return "user float"


if __name__ == '__main__':
    app.run()

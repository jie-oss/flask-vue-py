from flask import Flask, jsonify, request, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

#登录模块
@app.route('/face/vef', methods=['POST'])
def face_vef():
    # 从请求中获取 JSON 数据
    data = request.get_json()
    # 打印数据到控制台
    print('登录',data)
    # 返回响应
    return jsonify({'message': 'Data received', 'data': data})

#人脸录入
@app.route('/face/save', methods=['POST'])
def face_save():
    # 从请求中获取 JSON 数据
    data = request.get_json()
    # 打印数据到控制台
    print(data)
    # 返回响应
    return jsonify({'message': 'Data received', 'data': data})

#获取人脸列表
@app.route('/face/faceList', methods=['GET'])
def faceList():
    data = {"message": "Hello from Flask!"}
    return jsonify(data)

#修改人脸
@app.route('/face/info/fid', methods=['GET'])
def face_info():
    data = {"message": "Hello from Flask!"}
    return jsonify(data)

#删除人脸
@app.route('/face/faceDelete/fid', methods=['GET'])
def faceDelete():
    data = {"message": "Hello from Flask!"}
    return jsonify(data)

#日志列表
@app.route('/face/log/list', methods=['GET'])
def face_log():
    data = {"message": "Hello from Flask!"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True,port=8080)

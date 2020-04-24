#!/usr/bin/env python
#encoding=utf-8

import sys
from flask import Flask, render_template, request, url_for, Response
import json

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('demo.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html',result=404)

@app.route('/data',methods=['POST','GET'])
def data():
    data = request.get_data()
    str_input = json.loads(data)
    
    templates="%s关于2020年春季学期学生返校的通知：\n 根据%s关于返校开学工作有过要求，结合学校疫情防控工作实际，经研究，定于2020年%s起启动学生分期分批有序返校，具体返校时间和有关要求由各学院（系）通知每位学生。请各位同学根据具体要求做好相关安排并在返校途中做好自我防护。"%(str_input[0],str_input[1],str_input[2])
    print(templates)

    callback = request.args.get('callback')
    json_data = [templates]
    return Response('{}({})'.format(callback, json_data))

if __name__ == "__main__":
    app.run(debug = True)
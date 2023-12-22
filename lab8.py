from flask import Blueprint, render_template, request, abort, jsonify
import datetime

lab8=Blueprint('lab8',__name__)

@lab8.route('/lab8/')
def main():
    return render_template('lab8/index.html')

courses = [
    {"name": "c++", "videos": 3,"price": 3000},
    {"name": "basic", "videos": 30,"price": 0},
    {"name": "c#", "videos": 8}
]

@lab8.route('/lab8/api/courses/', methods=['GET'])
def get_courses2(course_num):
    return courses[course_num]

@lab8.route('/lab8/api/courses/<int:course_num>', methods=['GET'])
def get_courses3(course_num):
    if 0<= course_num < len(courses)-1:
        abort(404, "Course not found")
    return courses[course_num]

@lab8.route('/lab8/api/courses/<int:course_num>',methods=['DELETE'])
def del_courses(course_num):
    if 0<= course_num < len(courses)-1:
        del courses[course_num]
        return '', 204
    else:
        abort(404, "Course not found")

@lab8.route('/lab8/api/courses/<int:course_num>',methods=['PUT'])
def put_courses(course_num):
    if course_num < 0 or course_num > len(courses)-1:
        abort(404, "Course not found")
    course = request.get_json()
    courses[course_num] = course
    return courses[course_num]
        


    
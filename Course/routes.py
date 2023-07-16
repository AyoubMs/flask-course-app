from flask import Blueprint, render_template, jsonify, request
from .models import Course
from . import db
import json

routes = Blueprint('routes', __name__)

@routes.route('/')
def courses():
    courses = Course.query.all()
    list = []
    for course in courses:
        list.append(course.toDict())
    return jsonify({"courses": list})
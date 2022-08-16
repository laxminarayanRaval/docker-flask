from flask import Blueprint, request, jsonify

from project import database
from project.helpers.auth import is_authenticated
from project.models.project import Project

project_bp = Blueprint("project_bp", __name__)


@project_bp.route("/add")
@is_authenticated
def add_project(curr_user):
    data = request.get_json()

    pname = data["pname"].strip()
    sampling_type = data["sampling_type"].strip()
    description = data["description"].strip()
    instructions = data["instructions"].strip()

    try:
        database.add_instance(
            Project,
            pname=pname,
            sampling_type=sampling_type,
            description=description,
            instructions=instructions,
            created_by=curr_user.id,
        )
        return jsonify(message=f"New Project {pname} added"), 201
    except BaseException() as e:
        return jsonify(error="Something went wrong during Project Adding"), 406


@project_bp.route("/details")
def all_details():
    try:
        data = database.get_all(Project)
        print("data", data)
        return jsonify(data=data, message="All Project Details"), 200
    except Exception as e:
        print("Error:", e)
        return jsonify(error="Having Some Issues find Project Details"), 400

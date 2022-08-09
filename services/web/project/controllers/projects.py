from flask import Blueprint, request, jsonify

from project import database
from project.helpers.auth import is_authenticated
from project.models.projects import Projects

project_bp = Blueprint("project_bp", __name__)


@project_bp.route("", methods=["GET"])
def fetch():
    all_projects = database.get_all(Projects)
    projects_list = []
    for project in all_projects:
        new_project = {
            "id": project.id,
            "title": project.title,
            "description": project.description,
            "tags": project.tags,
            "hourly_rate": project.hourly_rate,
            "created_by": project.created_by,
        }
        projects_list.append(new_project)

    return jsonify(data=projects_list), 200


@project_bp.route("/add", methods=["POST"])
@is_authenticated
def add(curr_user):
    data = request.get_json()
    title = data["title"].strip()
    description = data["description"].strip()
    tags = data["tags"]
    hourly_rate = data["hourly_rate"].strip()

    database.add_instance(
        Projects,
        title=title,
        description=description,
        tags=tags,
        hourly_rate=hourly_rate,
        created_by=curr_user.id,
    )

    return jsonify(message="added"), 200


@project_bp.route("/remove/<project_id>", methods=["DELETE"])
@is_authenticated
def remove(project_id, curr_user):
    database.delete_instance(Projects, id=project_id)
    return jsonify(message="removed"), 200


@project_bp.route("/edit/<project_id>", methods=["PATCH"])
@is_authenticated
def edit(project_id, curr_user):
    data = request.get_json()
    new_hourly_rate = data["hourly_rate"]
    database.edit_instance(Projects, id=project_id, hourly_rate=new_hourly_rate)
    return jsonify(message="updated"), 200

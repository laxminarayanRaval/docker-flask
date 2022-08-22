from flask import Blueprint, request, jsonify

from project import database
from project.helpers.auth import is_authenticated
from project.models.task import Task
from project.models.project import Project

task_bp = Blueprint("task_bp", __name__)


@task_bp.route("/add", methods=["POST"])
@is_authenticated
def add_task(curr_user):
    data = request.get_json()

    if not ("project_id" in data and "title" in data and "comment" in data):
        return jsonify(error="Please Provide Proper data"), 400

    project_id = data["project_id"].strip()
    title = data["title"].strip()
    comment = data["comment"].strip()

    try:
        project_data = database.get_filter_by(Project, id=project_id)
        if not project_data:
            return jsonify(error="Project not found, for given project_id."), 401
        database.add_instance(
            Task,
            project_id=project_id,
            title=title,
            comment=comment,
            created_by=curr_user.id,
        )
        return (
            jsonify(
                message=f"Task Added successfully, for Project {project_data.project_name}"
            ),
            201,
        )
    except Exception as e:
        return jsonify(error=f"Adding task failed. {e}"), 400


@task_bp.route("/project/<int:project_id>")
def get_task_by_project_id(project_id):
    try:
        args = request.args.to_dict()
        # created_by = args.get("created_by")

        project_data = database.get_filter_by(Project, id=project_id)

        if not project_data:
            return jsonify(error=f"Project {project_id} not found"), 404

        task_data = database.get_filter_all(Task, project_id=project_id, **args)

        if not task_data:
            return jsonify(error=f"NO Task Found"), 404

        return jsonify(data=task_data), 200
    except Exception as e:
        return jsonify(error=f"Task Not Found. {e}"), 400

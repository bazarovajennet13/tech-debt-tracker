from models import Project
from models.projects import add_project, find_project


def test_project_creation():
    project = Project(1, "API", "Backend")
    assert project.id == 1
    assert project.name == "API"
    assert project.description == "Backend"


def test_add_project():
    projects = []
    add_project(projects, "API", "Backend")
    assert len(projects) == 1


def test_find_project():
    projects = []
    add_project(projects, "API", "Backend")
    assert find_project(projects, "api")
    assert not find_project(projects, "mobile")
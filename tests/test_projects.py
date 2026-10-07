from projects import add_project, find_project, get_project_name


def test_add_project():
    projects = {}
    add_project(projects, "API", "Backend")
    assert len(projects) == 1


def test_find_project():
    projects = {}
    add_project(projects, "API", "Backend")
    assert find_project(projects, "api")
    assert not find_project(projects, "mobile")


def test_get_project_name():
    projects = {}
    add_project(projects, "API", "Backend")
    assert get_project_name(projects, 1) == "API"
    assert get_project_name(projects, 99) == "?"
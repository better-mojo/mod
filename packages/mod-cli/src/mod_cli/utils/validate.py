import re
from pathlib import Path

from loguru import logger


def validate_project_name2(project_name):
    # 校验长度是否符合要求（示例为 3 到 20 个字符）
    if len(project_name) < 1 or len(project_name) > 30:
        logger.error("project name length should be between 1 and 30")
        return False

    # 校验首字母是否合法
    if re.match(r"[-_\d]", project_name[0]):
        return False

    # 校验是否只包含字母、数字和下划线
    if not re.match("^[a-zA-Z0-9_-]+$", project_name):
        logger.error(
            "project name should only contain letters, numbers, and underscores"
        )
        return False

    # 其他校验规则...
    return True


def validate_project_name(project_name: Path | str):
    p = Path(project_name)
    s = str(p)

    if not is_valid_path(s):
        logger.error(f"project name is not a valid path: {project_name}")
        return False

    name = p.name
    if not is_valid_directory_name(name):
        logger.error(f"project name is not a valid directory name: {name}")
        return False
    return True


def is_valid_path(path: Path | str):
    return True  # FIXME
    pattern = r'^[A-Za-z]:\\(?:[^\\/:*?"<>|\r\n]+\\)*[^\\/:*?"<>|\r\n]*$'
    return re.match(pattern, str(path)) is not None


def is_valid_directory_name(directory_name):
    pattern = r"^[^\d-][\w-]*$"
    return re.match(pattern, directory_name) is not None


def is_valid_directory(path):
    pattern = r"^([\w.-]+)+/?$"
    return re.match(pattern, path) is not None


def is_path_exists(path: Path | str):
    p = Path(path)
    return p.exists()


def test_():
    test_cases = [
        "abc",
        "abc-def",
        "abc_def",
        "abc0123",
        "abc12df",
        "abc/",
        "abc/def",
        "1abc",
        "1abc/",
        "-abc",
        "_abc",
    ]

    for case in test_cases:
        print(
            f"{case}: dir status: {is_valid_directory_name(case)}, name status: {validate_project_name(case)}"
        )

    cases = [
        "a/b/c",
        Path("e/f/g"),
    ]

    for case in cases:
        p = Path(case)
        print(f"{case}: {p.parent}, {p.name}")

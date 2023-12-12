from pathlib import Path
import re
from loguru import logger


def new_project(project_name: str, project_type: str = "lib", project_dir: str = None, **kwargs):
    if project_type == "lib":
        new_lib(project_name=project_name, project_dir=project_dir)
    else:
        new_bin(project_name=project_name, project_dir=project_dir)


def new_lib(project_name: str, project_dir: str = None):
    """mojo new lib
    like cargo new --lib
    """
    if not project_dir:
        project_dir = "./"

    p = Path("./src/lib.rs")
    if p.exists():
        print("lib already exists")
        return

    pass


def new_bin(project_name: str, project_dir: str = None):
    """mojo new binary app
    like cargo new --bin
    """
    pass


def validate_project_name(project_name):
    # 校验长度是否符合要求（示例为 3 到 20 个字符）
    if len(project_name) < 1 or len(project_name) > 30:
        logger.error(f"project name length should be between 1 and 30")
        return False

    # 校验首字母是否合法
    if re.match("[-_\d]", project_name[0]):
        return False

    # 校验是否只包含字母、数字和下划线
    if not re.match("^[a-zA-Z0-9_-]+$", project_name):
        logger.error(f"project name should only contain letters, numbers, and underscores")
        return False

    # 其他校验规则...
    return True


def test():
    logger.info(validate_project_name('a1'))
    logger.info(validate_project_name('a1_'))
    logger.info(validate_project_name('a1-b'))

    logger.info(validate_project_name('-a1'))
    logger.info(validate_project_name('_a1'))
    logger.info(validate_project_name('1a1'))

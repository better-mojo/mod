import os
from loguru import logger


def find_project_dir(path: str = None):
    if not path:
        path = os.getcwd()

    path = os.path.abspath(path)
    root = None

    # 向上递归寻找含有 pyproject.toml 的目录
    while True:
        if (
            'pyproject.toml' in os.listdir(path)
            or 'mod.toml' in os.listdir(path)
            or '.git' in os.listdir(path)
        ):
            root = path
            break
        else:
            path = os.path.abspath(os.path.join(path, os.pardir))
        # 如果已经到达根目录，停止搜索
        if path == os.path.abspath(os.path.join(path, os.pardir)):
            logger.error(f"No directory with 'pyproject.toml' found.")
            break
    return root


def validate_project_dir(path: str = None):
    if not path:
        return False

    if not os.path.exists(path) or not os.path.exists(os.path.abspath(path)):
        logger.error(f"Project directory not found: {path}")
        return False

    if (
        'pyproject.toml' in os.listdir(path)
        or 'mod.toml' in os.listdir(path)
        or '.git' in os.listdir(path)
    ):
        root = path
        return True
    return False


def test():
    logger.info(find_project_dir())

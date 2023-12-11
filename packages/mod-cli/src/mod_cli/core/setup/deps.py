import os
from loguru import logger
import shutil


def init_deps_dir(find_path=None, deps_folder="target"):
    # 向上递归寻找含有 pyproject.toml 的目录, 找到后, 在该目录下创建 vendor 目录
    # 如果不存在 pyproject.toml, 则向上递归寻找 pyproject.toml
    # target or vendor 目录
    # target/ 目录
    # ├── github.com
    # │   └── mod-cli/
    # │       ├── pyproject.toml

    find_path = find_path or os.getcwd()
    logger.info(f"Looking for '{deps_folder}/' in '{find_path}'")

    pkg_path = find_or_create_deps_dir(find_path, deps_folder)
    return pkg_path


def find_or_create_deps_dir(deps_path, dep_folder="target"):
    # 获取目录的绝对路径
    abs_path = os.path.abspath(deps_path)

    # 检查当前目录是否包含pyproject.toml文件
    if (
        'pyproject.toml' in os.listdir(abs_path)
        or 'mod.toml' in os.listdir(abs_path)
        or '.git' in os.listdir(abs_path)
    ):
        # 在当前目录创建vendor目录
        vendor_dir = os.path.join(abs_path, dep_folder)
        deps_dir = os.path.join(vendor_dir, 'deps')

        if not os.path.exists(deps_dir):
            os.makedirs(deps_dir)
            logger.info(f"Created {dep_folder} directory in '{abs_path}'")
        return vendor_dir  # 返回vendor目录

    # 获取当前目录的父目录
    parent_path = os.path.dirname(abs_path)

    # 如果已经到达根目录，停止搜索
    if abs_path == parent_path:
        logger.error(f"No directory with '{dep_folder}' found.")
        return None

    # 继续向上递归搜索
    return find_or_create_deps_dir(parent_path, dep_folder)


def clean_deps_dir(deps_folder="target"):
    deps_path = init_deps_dir(deps_folder=deps_folder)

    if deps_path:
        logger.info(f"Removing '{deps_folder}/' directory in '{deps_path}'")
        shutil.rmtree(deps_path)


def test():
    init_deps_dir()
    # clean_deps_dir()
    # clean_deps_dir(pkg_folder="vendor")

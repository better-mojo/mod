import os.path
import subprocess
from loguru import logger

from mod_cli.core.dir.dir import find_project_dir


def git_clone(url: str, branch: str = None, path: str = None):
    exec_git_clone(url, branch, path)


def exec_git_clone(url: str, branch: str = None, path: str = None):
    cmd = ["git", "clone"]
    if branch:
        cmd += ["-b", branch]
    if not path:
        host, username, repo, url = parse_git_url(url)
        path = os.path.join(find_project_dir(), "target", "deps", host, username, repo)
    if not os.path.exists(path):
        os.makedirs(path)
    cmd += [url, path]
    logger.info(f"exec cmd: {cmd}")

    # exec:
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        return True
    except Exception as e:
        logger.error(f"error: {e}")
    return False


def parse_git_url(url: str = None):
    """
    url:
        - https://github.com/MoSafi2/MojoFastTrim
        - https://github.com/MoSafi2/MojoFastTrim.git
        - git@github.com:MoSafi2/MojoFastTrim.git
    """
    url = url or "https://github.com/MoSafi2/MojoFastTrim"

    host = ""
    username = ""
    repo = ""

    hosts = [
        "github.com",
        "gitlab.com",
        "bitbucket.org",
    ]

    for h in hosts:
        if url.lower().find(h):
            host = h
            break

    if not host:
        logger.error(f"Invalid git url: {url}")
        return host, username, repo, url

    url = url.strip(".git")

    # support 3 types of git url
    sep = ":" if url.lower().find("@git") != -1 else "/"
    # logger.info(f"host: {host}, sep: {sep}")
    username, repo = url.split(f"{host}{sep}")[1].split("/")
    if not username or not repo:
        logger.error(f"Invalid git url: {url}")

    # fmt again
    url = f"https://github.com/{username}/{repo}.git"

    logger.info(f"username: {username}, repo: {repo}, url: {url}")

    return host, username, repo, url


def test():
    parse_git_url()
    parse_git_url(url="https://github.com/MoSafi2/MojoFastTrim.git")
    parse_git_url(url="git@github.com:MoSafi2/MojoFastTrim.git")

    # git_clone(url="https://github.com/MoSafi2/MojoFastTrim.git")

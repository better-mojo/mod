import os.path
import subprocess
from loguru import logger
import shutil

from mod_cli.core.dir import find_project_dir, validate_project_dir


class Git(object):
    def __init__(self, project_dir: str = None):
        # double check
        self.project_dir = project_dir if validate_project_dir(project_dir) else find_project_dir()
        self.deps_dir = os.path.join(self.project_dir, "target", "deps")
        self.build_dir = os.path.join(self.project_dir, "target", "build")
        self.hosts = [
            "github.com",
            "gitlab.com",
            "bitbucket.org",
            "git.sr.ht",
        ]

        self.setup()

    def setup(self):
        if not os.path.exists(self.deps_dir):
            os.makedirs(self.deps_dir)

        if not os.path.exists(self.build_dir):
            os.makedirs(self.build_dir)

    def clone(self, url: str, branch: str = None, path: str = None):
        if self.is_repo_exists(url=url):
            host, username, repo, url = self.parse_git_url(url)
            self.clean(host=host, username=username, repo=repo)
        return self.exec_git_clone(url, branch, path)

    def sync(self, url: str, branch: str = None, path: str = None):
        # TODO: git fetch cmd
        return self.clone(url, branch, path)

    def is_repo_exists(self, host: str = None, username: str = None, repo: str = None, url: str = None):
        if url:
            host, username, repo, url = self.parse_git_url(url)

        path = os.path.join(self.deps_dir, host, username, repo)
        return os.path.exists(path)

    def parse_git_url(self, url: str = None):
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

        for h in self.hosts:
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

    def repo_path(self, url: str = None):
        host, username, repo, url = self.parse_git_url(url)
        return os.path.join(self.deps_dir, host, username, repo)

    def clean(self, host: str = None, username: str = None, repo: str = None, url: str = None):
        if url:
            host, username, repo, url = self.parse_git_url(url)
        return self.exec_rm_repo(host, username, repo)

    def exec_rm_repo(self, host: str = None, username: str = None, repo: str = None):
        path = os.path.join(self.deps_dir, host, username, repo)
        logger.info(f"clean repo: {path}")
        if not os.path.exists(path):
            logger.error(f"repo not found: {path}")
            return
        shutil.rmtree(path)

    def exec_git_clone(self, url: str, branch: str = None, path: str = None):
        cmd = ["git", "clone"]
        if branch:
            cmd += ["-b", branch]
        if not path:
            host, username, repo, url = self.parse_git_url(url)
            path = os.path.join(self.deps_dir, host, username, repo)
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


def test():
    # git_clone(url="https://github.com/MoSafi2/MojoFastTrim.git")

    g = Git()
    g.parse_git_url()
    host, username, repo, url = g.parse_git_url(url="https://github.com/MoSafi2/MojoFastTrim.git")
    g.parse_git_url(url="git@github.com:MoSafi2/MojoFastTrim.git")
    # g.clone(url="https://github.com/MoSafi2/MojoFastTrim.git")
    # g.clone(url="https://github.com/MoSafi2/MojoFastTrim.git", branch="dev")

    logger.info(f"repo exists: {g.is_repo_exists(host=host, username=username, repo=repo)}")
    logger.info(f"repo exists: {g.is_repo_exists(url=url)}")

    # g.clone(url=url)
    # g.clean(url=url)
    # g.clone(url=url)


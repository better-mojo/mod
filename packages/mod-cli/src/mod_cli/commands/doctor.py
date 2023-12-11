import sys

import typer
from loguru import logger
import platform
import subprocess

cmd_doctor = typer.Typer()


@cmd_doctor.command()
@cmd_doctor.callback()
def doctor():
    """
    Doctor
    """
    typer.echo("Doctor")
    check_os()


def check_os() -> (str, str):
    # result = subprocess.run(["uname"], capture_output=True, text=True)
    # os_platform = result.stdout.strip()

    pl = platform.system()

    logger.info(f"platform version: {pl}, {platform.version()}")
    logger.info(f"platform machine: {pl}, {platform.machine()}")
    logger.info(f"platform mac ver: {pl}, {platform.mac_ver()}")
    logger.info(f"platform win ver: {pl}, {platform.win32_ver()}")
    # logger.info(f"platform release: {p}, {platform.release()}")
    # logger.info(f"platform.system(): {p}, {platform.linux_distribution()}")

    pkg_manager = {
        "Windows": "choco",
        "Linux": "apt",
        "Darwin": "brew",
        "NixOS": "nix",
        "ArchLinux": "pacman",
        "CentOS": "yum",
        "Fedora": "dnf",
    }

    # TODO: check linux distribution
    if not pkg_manager.get(pl):
        logger.error(f"Unsupported operating system: {pl}")
    return pl, pkg_manager.get(pl)


def check_pkg_manager(pm: str):
    cmd_check = [pm, "--version"]

    install_brew = '''
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    '''

    #
    # windows install choco
    #   - ref: https://docs.chocolatey.org/en-us/choco/setup#more-install-options
    #
    install_choco_by_cmd = '''
    @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
    '''
    install_choco_by_ps = '''
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    '''

    pm_install = {
        "brew": [install_brew],
        "choco": [
            [install_choco_by_cmd],
            [install_choco_by_ps],
        ],
    }

    if pm.lower() == "brew":
        has = exec_cmds(cmd_check)
        if has:
            return True
        return exec_cmds(pm_install[pm])
    elif pm.lower() == "choco":
        has = exec_cmds(cmd_check)
        if has:
            return True
        return exec_cmds(pm_install[pm][0])
    logger.error(f"Unsupported package manager: {pm}")
    return False


def has_package(pkg: str):
    cmd_check = [pkg, "--version"]

    # Check the operating system
    os, pm = check_os()

    # Check the package manager
    if not check_pkg_manager(pm):
        return False

    # Check if the package is installed
    has = exec_cmds(cmd_check)
    if has:
        return True

    # Install the package
    ok = install_package_by_pm(pm, pkg)
    if ok:
        # Check if the package is installed
        return exec_cmds(cmd_check)
    return False


def has_packages(packages: list):
    for pkg in packages:
        if not has_package(pkg):
            return False
    return True


def install_package_by_pm(pm: str, pkg: str):
    cmd_install = {
        "brew": [f"brew install {pkg}"],
        "choco": [f"choco install {pkg}"],
        "pip": [f"pip install {pkg}"],
        "apt-get": [f"apt-get install -y {pkg}"],
        "yum": [f"yum install -y {pkg}"],
    }
    return exec_cmds(cmd_install[pm])


def exec_cmds(cmds: list):
    try:
        # 执行命令并捕获输出
        result = subprocess.run(
            cmds,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding='utf-8',
        )

        # 打印输出
        if result.stdout:
            logger.info(f"✅Command {cmds} output: {result.stdout}")
        if result.stderr:
            logger.error(f"❌Command {cmds} failed, error: {result.stderr}")

        # subprocess.run(
        #     cmds,
        #     check=True,
        #     capture_output=True,
        #     text=True,
        # )
    except Exception as e:
        logger.error(f"❌Command {cmds} failed, error: {e}")
        return False
    return True


def test_ok():
    # doctor()
    has_package("git")
    has_packages(["git", "python", "poetry", ])


def test_err():
    has_package("not_a_package")


if __name__ == "__main__":
    typer.run(doctor())

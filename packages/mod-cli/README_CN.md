# Mod = (Mojo Dep) 包管理工具

[English](README.md) | 简体中文

## 说明

- `Mod` =[Mojo](https://docs.modular.com/mojo/) 编程语言(Python++) 包管理工具(非官方)
- `Mod` 类似如下工具:
    - Rust: `Cargo`
    - Python: `Pip/Poetry/PDM`
    - Go: `Dep + Vendor`
- `Mod` 主要参考 `Cargo` 设计, 也借鉴了`Poetry/PDM/Dep`的一些特性, 实现的 Mojo 包管理工具.
- 状态: `WIP`(Work In Progress)

## 快速开始

- ✅ 依赖:
    - mojo 0.6+
    - python 3.10+
    - git

```ruby
mojo -v            
mojo 0.6.1 (876ded2e)

python --version                                                                                                                                          07:27:03
Python 3.10.9

```

- ✅ 安装 `mod`:

```ruby

pip install mod-cli

# or
poetry add mod-cli --dev

```

- 使用 `mod` 命令:
    - `mod new`: 创建一个新的 mojo 项目,
        - `--lib`: 创建一个库工程
        - `--bin`: 创建一个应用(二进制可执行的程序)
    - `mod init`: 对一个已存在的 mojo 项目, 初始化
    - `mod build`: 编译 mojo 项目为 `mojopkg`(二进制库)
    - `mod install`: 下载 mojo 依赖库到本地 `target/deps`
    - `mod hack`:
        - `mod hack build`: 编译 `target/deps` 中的依赖库, 编译为 `mojopkg`(二进制库)
        - `mod hack install`: 把``target/deps``中的依赖库, 安装到 `mojo 标准库路径下`.(用于支持 vscode 自动补全)
        - `mod hack uninstall`: 把``target/deps``中的依赖库, 卸载.
        - `mod hack clean`: 清理 `target/deps` 编译生成的 `mojopkg`(二进制库)
    - `mod run`: 运行 mojo 文件
    - `mod test`: 单元测试
    - `mod add`: 添加一个依赖库
    - `mod remove`: 移除一个依赖库
    - `mod list`: 列出所有依赖库
    - `mod search`: 搜索依赖库(模糊搜索)
    - `mod sync`: 同步依赖库
    - `mod lint`: 代码风格检查
    - `mod publish`: 发布一个 mojo 项目
    - `mod workspace`: monorepo 工作区管理
        - `mod workspace init`: 初始化工作区
        - `mod workspace list`: 列出工作区
        - `mod workspace add`: 添加工作区
        - `mod workspace remove`: 移除工作区
    - `mod self`: 自身管理
        - `mod self update`: 更新 `mod` 自身
    - `mod help`: 帮助

```ruby

mod --help


```

## Manual

- `mod cmds`

### ✅ Create a new project

- like `cargo new` style:

```ruby
# new a libary
mod new your/path/to/project --lib

# new a app
mod new your/path/to/project --bin
```

### ❎ Build Mojo Package

- ❎ TODO

```ruby

mod build

```

# References

- https://taskfile.dev
- typer: https://typer.tiangolo.com

> package manager

- [python + poetry](https://python-poetry.org/)
- [python + pdm](https://pdm-project.org/latest/)
- [rust + cargo](https://doc.rust-lang.org/cargo/)
- [golang + dep](https://github.com/golang/dep)
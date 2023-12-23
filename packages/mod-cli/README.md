# Mod = (Mojo Dep)

- [Mojo](https://docs.modular.com/mojo/) Package Manager Tool
- like:
    - Rust: `Cargo`
    - Python: `Pip/Poetry/PDM`
    - Go: `Dep + Vendor`

## Quick Start

- install:

```ruby

pip install mod-cli

# or
poetry add mod-cli --dev

```

- usage:
    - `mod new`: create a new project
    - `mod init`
    - `mod build`: build a `mojopkg`
    - `mod run`: run mojo file
    - `mod test`: unit test
    - `mod publish`: publish a `mojopkg`
    - `mod workspace`: for monorepo

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
# 一些设计方案

## mod.toml

### 包管理部分:(依赖管理)

- 类似 cargo.toml 的依赖管理

> 需要支持的特性:

- 包名 + 别名
- 包版本
- 包依赖树(目前都是单个包, )

- 基于 git url 的依赖管理
    - git repo
    - git branch
    - git tag
    - repo + relative path

### python + pip 设计

- `~/.cache/pip`
- 缓存的包路径: `~/.cache/pip/wheels`

### dart + pub 设计

- `~/.pub-cache`
- 缓存的包路径:`~/.pub-cache/hosted/pub.dartlang.org`
- 设计非常粗暴, 就是每个依赖版本, 直接 git clone `repo + 版本号`进来.(这样不需要复杂的分析)
- 缺点是: 代码膨胀
- 优点: 实现简单, 可以快速搞定(打算参考此设计)

### rust +cargo 设计:

- `~/.cargo`
- 比较复杂, 对源码做了二进制编译

```ruby


┬─[geek@rmbp13:~/.cargo]─[06:36:31]
╰─>$ tree . -L 3                                                                                                                       06:36:31
.
├── bin
│   ├── cargo
│   └── rustup
├── env
├── git
│   ├── CACHEDIR.TAG
│   ├── checkouts
│   │   └── tauri-plugin-aptabase-3f46885398a9c13a
│   └── db
│       └── tauri-plugin-aptabase-3f46885398a9c13a
└── registry
    ├── CACHEDIR.TAG
    ├── cache
    │   ├── github.com-1ecc6299db9ec823
    │   ├── index.crates.io-6f17d22bba15001f
    │   └── mirrors.sjtug.sjtu.edu.cn-7a04d2510079875b
    ├── index
    │   ├── github.com-1ecc6299db9ec823
    │   ├── index.crates.io-6f17d22bba15001f
    │   └── mirrors.sjtug.sjtu.edu.cn-7a04d2510079875b
    └── src
        ├── github.com-1ecc6299db9ec823
        ├── index.crates.io-6f17d22bba15001f
        └── mirrors.sjtug.sjtu.edu.cn-7a04d2510079875b

20 directories, 20 files
```

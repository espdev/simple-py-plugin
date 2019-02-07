# simple-py-plugin

A minimal example of python plugins powered by setuptools.

# Usage

1. Install core:

```
$ cd simple-core/
$ pip install -e .
```

2. Install plugins

```
$ cd simple-plugins/
$ pip install -e .
```

3. Run app

```
$ simple_core

Hello from Core!
{'bar': <function bar_plugin at 0x00000275B97716A8>, 'foo': <function foo_plugin at 0x00000275B9771620>}
Hello from bar plugin!
Hello from foo plugin!
```

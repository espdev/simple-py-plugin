# -*- coding: utf-8 -*-

from pkg_resources import iter_entry_points


def main():
    print('Hello from Core!')

    plugins = {
        entry_point.name: entry_point.load()
        for entry_point in iter_entry_points('simple.plugins')
    }

    print(plugins)

    for plugin_func in plugins.values():
        plugin_func()


if __name__ == '__main__':
    pass

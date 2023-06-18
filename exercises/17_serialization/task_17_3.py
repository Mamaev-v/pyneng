# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""

import re
from pprint import pprint

def parse_sh_cdp_neighbors(config):
        regex = re.compile(r"(?P<eq_d>\S+) +(?P<port_loc>\S+ \d+\S\d+).+ +(?P<port_dest>\S+ \d+\S\d+)")
        final = {}
        for line in config.split("\n"):
                line = line.strip()
                columns = line.split()
                if ">" in line:
                        main_name = (line.split(">")[0])
                        final[main_name] = {}
                elif len(columns) > 4 and columns[3].isdigit():
                        match = regex.search(line)
                        eq_d, port_l, port_d = match.groups()
                        final[main_name][port_l] = {eq_d:port_d}
        return final

def parse_sh_cdp_neighbors_2(config):
        regex = re.compile(r"(?P<eq_d>\S+) +(?P<port_loc>\S+ \d+\S\d+).+ +(?P<port_dest>\S+ \d+\S\d+)")
        final = {}
        main_eq = re.search(r"(\S+)[>#]", config).group(1)
        final[main_eq] = {}
        match = regex.finditer(config)
        for line in match:
                eq_d, port_loc, port_dest = line.group("eq_d", "port_loc", "port_dest")
                final[main_eq][port_loc] = {eq_d:port_dest}
        return final

if __name__ == "__main__":
        with open("sh_cdp_n_sw1.txt") as src:
                pprint(parse_sh_cdp_neighbors_2(src.read()))
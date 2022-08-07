# -*- coding: utf-8 -*-
"""
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

"""
import re
from pprint import pprint

def parse_sh_ip_int_br(config):
    output = list()
    regex = re.compile(r'(\S+) +(\S+|unassigned) +\S+ +\S+ +(up|down|administratively down) +(up|down)')
    with open(config) as f:
        for line in f:
            match = regex.search(line)
            if match:
                output.append(match.groups())
    return(output)

def parse_sh_ip_int_br_2(config):
    result = []
    regex = re.compile(r'(\S+) +(\S+|unassigned) +\S+ +\S+ +(up|down|administratively down) +(up|down)')
    with open(config) as f:
        find = re.finditer(regex, f.read())
        for match in find:
            result.append(match.groups())
    return(result)


#pprint(parse_sh_ip_int_br('sh_ip_int_br.txt'))
pprint(parse_sh_ip_int_br_2('sh_ip_int_br.txt'))

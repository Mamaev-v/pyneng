# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from opcode import opname

output = "\n{:20} {}" * 5

with open('/home/vladimir/Repos/pyneng/exercises/07_files/ospf.txt', 'r') as file:
    for line in file:
        line = line.replace(",", "").replace("[", "").replace("]", "").split()
        print(output.format(
        "Prefix", line[1],
        "AD/Mtric", line[2],
        "Next-Hop", line[4],
        "Last Update", line[5],
        "Outbound Interface", line[-1]     
        ))


# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT
из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""

import re
from pprint import pprint

def convert_ios_nat_to_asa(input, output):
    regex = re.compile(r'.+ (?P<IP>\S+) (?P<Port_l>\d+) \S+ \S+ (?P<Port_d>\d+)')
    template = '''object network LOCAL_{0}\n host {0}\n nat (inside,outside) static interface service tcp {1} {2}\n'''
    with open(input) as src, open(output, 'w') as dest:
        for line in src:
            match = regex.search(line)
            ip, port_l, port_d = match.groups()
            #dest.write(f'object network LOCAL_{ip}\n')
            #dest.write(f' host {ip}\n')
            #dest.write(f' nat (inside,outside) static interface service tcp {port_l} {port_d}\n')
            dest.writelines(template.format(ip, port_l, port_d))

convert_ios_nat_to_asa('cisco_nat_config.txt', 'NAT_done.txt')

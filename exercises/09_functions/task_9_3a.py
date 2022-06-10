# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
    access_dict = {}
    trunk_dict = {}
    with open(config_filename, 'r') as file:
        for line in file:
            line = line.rstrip()
            if 'FastEthernet' in line:
                interface = line.split()[-1]
                access_dict[interface] = 1
            elif 'access vlan' in line:
                vlan = line.split()[-1]
                access_dict[interface] = vlan
            elif 'trunk allowed' in line:
                vlans = line.split()[-1]
                trunk_dict[interface] = vlans
                del access_dict[interface]
    return access_dict, trunk_dict

result = get_int_vlan_map('/Users/vladimir/Documents/repo_git/pyneng/exercises/09_functions/config_sw2.txt')
print(result)
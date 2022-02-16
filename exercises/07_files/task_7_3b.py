# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

dest = []
vlan = input('Please input number of vlan: ')

with open('CAM_table.txt', 'r') as file:
    for line in file:
        words = line.split()
        if len(words) > 3 and words[0].isdigit() and words[0] == vlan:
            vlan, mac, port = words[0], words[1], words[3]
            print(f"{vlan:<7}{mac:17}{port}") 
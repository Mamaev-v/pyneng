# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

import subprocess

def ping_ip_addresses(ip_address):
    reacheble = []
    unreacheble = []
    for ip in ip_address:
        ping = subprocess.run(['ping', '-c', '1', ip], stderr=subprocess.PIPE, stdout=subprocess.DEVNULL)
        if ping.returncode == 0:
            reacheble.append(ip)
        else:
            unreacheble.append(ip)
    return reacheble, unreacheble

if __name__ == "__main__":
    print(ping_ip_addresses(['8.8.8.8', '1.1.1.1', '32.4.2345.5']))

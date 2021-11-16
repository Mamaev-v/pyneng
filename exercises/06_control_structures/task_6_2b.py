# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

while True:
    ip_address = input("Введите IP адрес (прим. 10.0.1.1): ")
    ip = ip_address.split(".")
    check = True
    if len(ip) == 4:
        for oct in ip:
            if not (oct.isdigit and 0 <= int(oct) <= 255):
                check = False
                break
    else:
        check = False
    if check == True: # or "if check"
        break
    print("IP введен не верно")

print("IP  введен верно")

if 0 < int(ip[0]) < 224:
    print("unicast")
elif 223 < int(ip[0]) < 240:
    print("multicast")
elif ip_address == "255.255.255.255":
    print("local broadcast")
elif ip_address == "0.0.0.0":
    print("unassigned")
else:
    print("unused")
    
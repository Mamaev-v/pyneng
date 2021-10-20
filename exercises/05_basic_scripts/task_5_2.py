# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

subnet = input('Input subnet address: ')
subnet_list = subnet.replace('/', '.').split('.')
oct1 = int(subnet_list[0])
oct2 = int(subnet_list[1])
oct3 = int(subnet_list[2])
oct4 = int(subnet_list[3])
mask = int(subnet_list[4])
mask_bin_str = "1" * mask + "0" * (32 - mask)
mask_int_oct1 = int(mask_bin_str[0:8], 2)
mask_int_oct2 = int(mask_bin_str[8:16], 2)
mask_int_oct3 = int(mask_bin_str[16:24], 2)
mask_int_oct4 = int(mask_bin_str[24:32], 2)

template_network = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}'''

template_mask = '''
Mask:
/{0}
{1:<8} {2:<8} {3:<8} {4:<8}
{1:08b} {2:08b} {3:08b} {4:08b}
'''

print(template_network.format(oct1, oct2, oct3, oct4))
print(template_mask.format(mask, mask_int_oct1, mask_int_oct2, mask_int_oct3, mask_int_oct4))

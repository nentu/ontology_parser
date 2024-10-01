import json
import os
from entities import *

def find_from_data(data_list, title):
    l = [row for row in data_list if title in row['title']]
    if len(l) == 1:
        return l[0]['value']
    print(f'data_list: {data_list} - title: {title}')
    return 12


def get_processor_fields(data):
    return {
        'name': data['data']['name'],
        'model': find_from_data(data['data']['characteristics']['Общие параметры'], 'Модель'),
        'country': data['data']['manufacturerCountry'],
        'kernel_count': find_from_data(data['data']['characteristics']['Ядро и архитектура'], 'Общее количество ядер'),
        'base_frequency': find_from_data(list(data['data']['characteristics']['Частота и возможность разгона']),
                                         'Базовая частота процессора'),
        'max_frequency': find_from_data(list(data['data']['characteristics']['Частота и возможность разгона']),
                                        'Максимальная частота')
    }

def get_motherboards_fields(data):
    return {
        'name': data['data']['name'],
        'model': find_from_data(data['data']['characteristics']['Общие параметры'], 'Модель'),
        'country': data['data']['manufacturerCountry'],
        'chip_set': find_from_data(data['data']['characteristics']['Процессор и чипсет'], 'Чипсет'),
        'mem_type': find_from_data(list(data['data']['characteristics']['Память']),
                                         'Тип поддерживаемой памяти'),
        'mem_capacity': find_from_data(list(data['data']['characteristics']['Память']),
                                        'Максимальный объем памяти')
    }

def get_videocards_fields(data):
    return {
        'name': data['data']['name'],
        'model': find_from_data(data['data']['characteristics']['Общие параметры'], 'Модель'),
        'country': data['data']['manufacturerCountry'],
        'graphic_process': find_from_data(data['data']['characteristics']['Основные параметры'], 'Графический процессор'),
        'mem_capacity': find_from_data(list(data['data']['characteristics']['Спецификации видеопамяти']),
                                         'Объем'),
        'mem_frequency': find_from_data(list(data['data']['characteristics']['Спецификации видеопамяти']),
                                        'частота')
    }



def create_entity(class_name, field_relation):
    eval_s = class_name + '('
    for key, value in field_relation.items():
        eval_s += f'{key}="{value}", '

    eval_s += ')'
    return eval(eval_s)



def get_entity_list(class_name, get_field_func, python = False):
    entity_list = list()
    path = '../data/' + class_name.lower() + 's'
    for file in os.listdir(path):
        data = json.loads(
            open(os.path.join(path, file), 'r', encoding='utf-8').read()
        )
        if python == True:
            entity_list.append(create_entity(class_name, get_field_func(data)))
        else:
            entity_list.append(get_field_func(data))
    return entity_list




processor_list = get_entity_list('Processor', get_processor_fields)
motherboard_list = get_entity_list('Motherboard', get_motherboards_fields)
videocard_list = get_entity_list('VideoCard', get_videocards_fields)


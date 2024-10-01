from parser.entites_creator import processor_list, motherboard_list, videocard_list
from utils import *

def create_entities(filename):
    f = open(filename, 'w', encoding='utf8')

    class_dict = {
        'Processor': processor_list,
        'Motherboard': motherboard_list,
        'VideoCard': videocard_list
    }

    for class_name, obj_list in class_dict.items():
        for entity in obj_list:
            f.write(generate_entity(class_name, entity['name']))
            for key, value in entity.items():
                if key == 'name':
                    continue
                f.write(
                    generate_data_property(
                        entity['name'],
                        value,
                        key
                    )
                )

    f.close()

if __name__ == '__main__':
    create_entities('../data/enities.owx')
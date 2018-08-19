# Memento class for saving objects to memory and restoring them
import random


class Memento:

    def __repr__(self):
        return self.serialize()

    def __init__(self, class_name, data_dict):
        self.class_name = class_name
        self.data_dict = data_dict
        self.memento_id = 7  # round(random.random() * 10000)

    def serialize(self):
        #new_dict = {'{}_{}'.format(self.class_name, self.memento_id): self.data_dict}
        print("self dd", self.data_dict.data.a1)
        new_dict = {'{}_{}'.format(self.class_name, self.memento_id): self.data_dict}
        print("new d", new_dict)
        print(new_dict['{}_{}'.format(self.class_name, self.memento_id)]['data']['a1'])
        return new_dict


def deserialize(dict):
    print("deser", str(dict))
    for key, value in _.pairs(dict):
        class_name, memento_id = key.split('_')
        print("kv split", class_name, memento_id)
        memento = Memento(class_name, value)
        memento.memento_id = memento_id
    print("done deser")
    return memento

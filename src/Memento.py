"""Memento class for saving objects to memory and restoring them."""
import random


class Memento:

    def __init__(self, class_name, data_dict):
        """Class name + a random memento id used to idenfity the memento in memory. data_dict should be a python dict"""
        self.class_name = class_name
        self.data_dict = data_dict
        self.memento_id = round(random.random() * 10000)


def serialize(memento):
    serialized_memento = {'{}_{}'.format(memento.class_name, memento.memento_id): memento.data_dict}
    return serialized_memento


def deserialize(serialized_memento):
    for key, value in _.pairs(dict):
        class_name, memento_id = key.split('_')
        memento = Memento(class_name, value)
        memento.memento_id = memento_id
    return memento

import os
import sys
import random
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Memento


def test_memento_init():
    class_name = "Class"
    data_dict = {"a": {1: 1, 2: 2, 3: 3}, "b": [1, 2, 3]}
    memento = Memento.Memento(class_name, data_dict)
    assert memento.class_name == class_name
    assert memento.data_dict == data_dict
    assert 1000 <= memento.memento_id <= 9999


def test_memento_serialize():
    class_name = "Class"
    data_dict = {"a": {1: 1, 2: 2, 3: 3}, "b": [1, 2, 3]}
    memento = Memento.Memento(class_name, data_dict)
    assert Memento.serialize(memento) == {'{}_{}'.format(memento.class_name, memento.memento_id): memento.data_dict}

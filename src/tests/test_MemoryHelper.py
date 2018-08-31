import os
import sys
import random
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import MemoryHelper as MemoryHelperModule
from MemoryHelper import MemoryHelper


def test_memory_returns_none_when_empty():
    memory_object = {}
    memory_instance = MemoryHelper("memory_helper_test", memory_object)
    assert memory_instance.get_memory_tree() == {}


def test_memory_get_empty_path():
    memory_object = {}
    memory_instance = MemoryHelper("memory_helper_test", memory_object)
    assert memory_instance.get_item_at_path("") == {}


def test_memory_make_class_dict():
    memory_object = {}
    memory_instance = MemoryHelper("memory_helper_test", memory_object)
    assert "memory_helper_test" in memory_object["class_data"]
    assert memory_object["class_data"]["memory_helper_test"] == {}


def test_set_memory():
    memory_object = {}
    memory_instance = MemoryHelper("memory_helper_test", memory_object)
    tree = generate_tree(5)
    memory_instance.set_memory_tree(tree)
    assert memory_object["class_data"]["memory_helper_test"] == tree


def test_get_memory():
    memory_object = {}
    memory_instance = MemoryHelper("memory_helper_test", memory_object)
    tree = generate_tree(5)
    memory_instance.set_memory_tree(tree)
    assert memory_instance.get_memory_tree() == tree


def test_memory_path_converter_blank_entry():
    assert MemoryHelperModule.to_path("") == [""]


def test_memory_path_converter():
    assert MemoryHelperModule.to_path("a.1.[3]") == ["a", "1", "[3]"]
    assert MemoryHelperModule.to_path("2.d") == ["2", "d"]
    assert MemoryHelperModule.to_path("a.1.[]") == ["a", "1", [], ""]


def test_set_item_at_path():
    memory_object = {}
    memory_instance = MemoryHelper("memory_helper_test", memory_object)
    memory_instance.set_item_at_path("aa.bb.cc", "item")
    assert memory_object["class_data"]["memory_helper_test"]["aa"]["bb"]["cc"] == "item"


def test_get_item_at_path():
    memory_object = {}
    memory_instance = MemoryHelper("memory_helper_test", memory_object)
    memory_instance.set_item_at_path("aa.bb.cc", "item")
    assert memory_instance.get_item_at_path("aa.bb.cc") == "item"


def test_remote_item_at_path():
    memory_object = {}
    memory_instance = MemoryHelper("memory_helper_test", memory_object)
    memory_instance.set_item_at_path("aa.bb.cc", "item")
    memory_instance.remove_item_at_path("aa.bb.cc")
    assert "cc" not in memory_object["class_data"]["memory_helper_test"]["aa"]["bb"]


def generate_tree(levels):
    if levels == 0:
        return random.randint(0, 10)
    else:
        tree = {}
        for i in range(levels):
            tree[i] = generate_tree(levels - 1)
        return tree


def print_tree(tree, level):
    if len(tree) == 1:
        print("   " * level, tree)
    else:
        for key, item in tree.items():
            print("   " * level, key)
            print_tree(item, level + 1)

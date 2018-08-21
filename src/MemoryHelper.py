"""Memory helper class that will write things to screeps memory."""

from defs import *
MEMORY_ID_STRING = "class_data"



class MemoryHelper:

    def __init__(self, class_id_string):
        """
        Takes in a class_id_string that is used to seporate the data from other classes in memory.
        Must be unique from other classes to avoid clobbering data.
        """
        self.class_id_string = class_id_string
        if MEMORY_ID_STRING not in Memory:
            Memory[MEMORY_ID_STRING] = {}
        if self.class_id_string not in Memory[MEMORY_ID_STRING]:
            Memory[MEMORY_ID_STRING][class_id_string] = {}

    def set_class_memory(self, data_dict):
        """Will overwrite the entirety of a classes memory in the game memory."""
        Memory[MEMORY_ID_STRING][self.class_id_string] = data_dict

    def get_class_memory(self):
        obj = Memory[MEMORY_ID_STRING][self.class_id_string]
        return obj

"""self.memory helper class that will write things to screeps memory."""


MEMORY_ID_STRING = "class_data"


class MemoryHelper:

    def __init__(self, class_id_string, memory):
        """
        Takes in a class_id_string that is used to seporate the data from other classes in memory.
        Takes in a memory object (treated as a dict) that we can act upon
        Must be unique from other classes to avoid clobbering data.
        """

        self.class_id_string = class_id_string
        self.memory = memory
        if MEMORY_ID_STRING not in self.memory:
            self.memory[MEMORY_ID_STRING] = {}
        if self.class_id_string not in self.memory[MEMORY_ID_STRING]:
            self.memory[MEMORY_ID_STRING][class_id_string] = {}

    def set_memory_tree(self, data_dict):
        """Will overwrite the entirety of a classes memory in the game memory."""
        self.memory[MEMORY_ID_STRING][self.class_id_string] = data_dict

    def get_memory_tree(self):
        return self.memory[MEMORY_ID_STRING][self.class_id_string]

    def get_item_at_path(self, path):
        value = self.memory[MEMORY_ID_STRING][self.class_id_string]
        # Recurse through memory until we reach the desired memory item
        # TODO add checking for if bad path?
        if len(path) == 0:
            return value

        for item in to_path(path):
            value = value[item]
        return value
        # return _.pick(self.memory[MEMORY_ID_STRING][self.class_id_string], path)

    def remove_item_at_path(self, path):
        path = to_path(path)

        def _remove(value, path):
            # Recurses through object until at desired path, than sets object as new value
            if len(path) == 1:
                del(value[path[0]])
            else:
                # If the next atribute of the path doesnt exist, create it
                if path[:1][0] not in value:
                    value[path[:1][0]] = {}
                # Set the memory item to be the current path atrivute, recirse on next atribute in path
                _remove(value[path[:1][0]], path[1:])

        _remove(self.memory[MEMORY_ID_STRING][self.class_id_string], path)

    def set_item_at_path(self, path, new_value):
        path = to_path(path)

        def _replace(value, path):
            # Recurses through object until at desired path, than sets object as new value
            if len(path) == 1:
                value[path[0]] = new_value
            else:
                # If the next atribute of the path doesnt exist, create it
                if isinstance(value, dict):
                    if path[:1][0] not in value:
                        value[path[:1][0]] = {}
                # Set the memory item to be the current path atrivute, recirse on next atribute in path
                _replace(value[path[:1][0]], path[1:])

        _replace(self.memory[MEMORY_ID_STRING][self.class_id_string], path)

        # traverse_modify(self.memory[MEMORY_ID_STRING][self.class_id_string], path, _replace)


# Credit to the below transversal algorithm goes to Vincent Driessen
# https://nvie.com/posts/modifying-deeply-nested-structures/


def traverse(obj, path=None, callback=None):
    """
    Traverse an arbitrary Python object structure (limited to JSON data
    types), calling a callback function for every element in the structure,
    and inserting the return value of the callback as the new value.
    """
    if path is None:
        path = []
    _.toArray(path)
    print('1', str(obj))
    print('1p', path)
    print('1', len(path))

    # Because intarface with JS is wonky, or because i'm bad, type checking doesnt work on dict.
    # Lodash isPlainObject will be true for dict like things but not arrays
    if _.isPlainObject(obj):
        print('2')
        value = {k: traverse(v, path + k, callback)
                 for k, v in _.pairs(obj)}
    # _.isArray will be true for arrays, but not dicts
    elif _.isArray(obj):
        print('3')
        value = [traverse(elem, path + [[]], callback)
                 for elem in obj]
    else:
        print('4')
        value = obj

    if callback is None:
        print('5')
        return value
    else:
        return callback(path, value)


def traverse_modify(obj, target_path, action):
    """
    Traverses an arbitrary object structure and where the path matches,
    performs the given action on the value, replacing the node with the
    action's return value.
    """
    target_path = to_path(target_path)

    def transformer(path, value):
        print("transform", target_path, path)
        print("transform ==", target_path == path)
        if path == target_path:
            print("returnnnning")
            return action(value)
        else:
            return value

    return traverse(obj, None, transformer)


def to_path(path):
    """
    Helper function, converting path strings into path lists.
        >>> to_path('foo')
        ['foo']
        >>> to_path('foo.bar')
        ['foo', 'bar']
        >>> to_path('foo.bar[]')
        ['foo', 'bar', []]
    """
    try:
        if _.isArray(path):
            return path  # already in list format
    except NameError:  # If running tests and cant find lodash
        if isinstance(path, list):
            return path  # already in list format

    def _iter_path(path):
        for parts in path.split('[]'):
            for part in parts.strip('.').split('.'):
                yield part
            yield []
    val = list(_iter_path(path))[: -1]
    return val

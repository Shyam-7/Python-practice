

# datatypes.py using type hints

#numeric types
an_integer: int = 100
a_float: float = 3.14
a_complex: complex = 1 + 2j

#text type
a_string: str = "hello world"

#sequence types
a_list: list = [1, 2, 3]
a_tuple: tuple = (1, 2, 3)
a_range: range = range(5)

#mapping type
a_dict: dict = {"key1": "value1", "key2": "value2"}

#set types
a_set: set = {1,2,3,4}
frozenset: frozenset = frozenset({1, 2, 3, 4})

#boolean type
a_boolean: bool = True

#binary types
some_bytes: bytes = b"a_byte_string"
some_bytesarray: bytearray = bytearray(b"a_byte_array")

#none type
a_none: None = None
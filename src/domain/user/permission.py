from enum import Enum


class Permission(Enum):
    READ_MODEL = 1
    WRITE_MODEL = 2
    DELETE_MODEL = 3
    PREDICT = 4

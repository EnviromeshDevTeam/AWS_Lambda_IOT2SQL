from enum import IntEnum


class DType(IntEnum):
    """[summary]
        Use Key and return IntEnum that corresponds to the categories ID
    Args: Inherits from IntEnum Class
    """    
    temperature = 1
    humidity = 2
    CO2 = 3
    TVOC = 4
    moisture = 5
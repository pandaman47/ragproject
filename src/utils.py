import numpy as np
import pandas as pd
import sys
import os

from src.exception import CustomException
from src.logger import logging

import dill

def save_object(file_path, obj):
    try:
        dir_name = os.path.dirname(file_path)

        os.makedirs(dir_name, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys) from e
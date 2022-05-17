import os

from sqlitedict import SqliteDict

from ..config import steamAPI

base_path = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,'config'))
if not os.path.isdir(base_path):
    os.mkdir(base_path)
class SQL(SqliteDict):
    def __init__(self,file):
        super().__init__(os.path.join(base_path, f'{file}.sqlite'), autocommit=True)
    
    
    
    
    
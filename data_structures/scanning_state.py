from data_structures.token import Token
from data_structures.meta_data import MetaData
from dataclasses import dataclass

@dataclass
class ScanningState:
    token_list: list[Token]
    meta_data: MetaData
    remaining_name: str
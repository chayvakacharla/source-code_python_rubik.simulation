# Vamsikrishna
# PS NO 40019022
from dataclasses import dataclass


@dataclass
class Move:
    face: str
    invert: bool
    double: bool
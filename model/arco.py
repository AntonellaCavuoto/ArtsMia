from dataclasses import dataclass

from model.artObject import ArtObject


@dataclass
class Arco:
    o1: ArtObject
    o2: ArtObject
    peso: int

    # non uso la struttura nel grafo quindi non uso __hash__ e __eq__

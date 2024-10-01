from dataclasses import dataclass


@dataclass
class Processor:
    name: str
    model: str
    country: str # TODO
    kernel_count: int
    base_frequency: float
    max_frequency: float

@dataclass
class Motherboard:
    name: str
    model: str
    country: str # TODO
    chip_set: str # TODO
    mem_type: str
    mem_capacity: int

@dataclass
class VideoCard:
    name: str
    model: str
    country: str
    graphic_process: str
    mem_capacity: int
    mem_frequency: int

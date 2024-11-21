from dataclasses import dataclass


@dataclass
class Route:
    start: str
    end: str
    line: str


@dataclass
class Itinerary:
    itinerary_type: str
    routes: list[Route]

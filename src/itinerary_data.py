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

@dataclass
class Disruption:
    period_begin: str
    status: str
    severity: str
    message: str
    line_id: str
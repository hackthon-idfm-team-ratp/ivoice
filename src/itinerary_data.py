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

    @classmethod
    def from_navitia_response(navitia_reponse: dict, itinerary_type: str):
        routes = []
        for section in navitia_reponse["journeys"][0]["sections"]:
            if section["type"] == "street_network" and section["mode"] == "walking":
                line = "A pied"
            elif section["type"] == "public_transport":
                line = f"{section['display_informations']['commercial_mode']} {section['display_informations']['name']}"
            else:
                line = "Inconnue"
            routes.append(Route(
                start=section["from"]["stop_point"]["name"],
                end=section["to"]["stop_point"]["name"],
                line=section["display_information"]
            ))

        return Itinerary(itinerary_type, routes)
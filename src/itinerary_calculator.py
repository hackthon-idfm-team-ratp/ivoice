from itinerary_data import Itinerary, Route
from dataloaders import load_arrets_et_lignes_associes
from itinerary import itinerary_with_line_exclusion
from datetime import datetime

class ItineraryCalculator:
    def __init__(self):
        self.stations_by_lines = load_arrets_et_lignes_associes()
        self.standard_destination_ids = ["IDFM:37539"]
        self.standard_itinerary_type = ["Central"]
        # ID ligne 9: line:IDFM:C01379

    def compute_alternate_itineraries(self, line_id: str) -> dict[str, Itinerary]:
        station_ids = self.stations_by_lines[self.stations_by_lines["id"] == line_id]["stop_id"]
        alt_itineraries = {}
        for station_id in station_ids:
            station_name = self.stations_by_lines[self.stations_by_lines["stop_id"] == station_id]["stop_name"].head(1).item()
            alt_itineraries[station_name] = []
            for std_destination_id, std_itin_type in zip(self.standard_destinations_ids, self.standard_itinerary_type):
                itin = itinerary_with_line_exclusion(station_id, std_destination_id, datetime.now(), line_id)
                alt_itineraries[station_name].append(Itinerary.from_navitia_response(itin, std_itin_type))

from model.stats_model import Stats_model

class Stats_controller:
    def __init__(self , db_path):
        self.db_path = db_path
        self.model = Stats_model(self.db_path)

    def display_donut_chart_team(self):
        return self.model.display_donut_chart_team()
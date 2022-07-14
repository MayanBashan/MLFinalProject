from datetime import datetime, timezone
import numpy as np


# Map each row to a vector of number

class Mapper:
    def __init__(self):
        # self.header_map = ["Index","Home","Away","Datetime","HomePos","HomePts","AwayPos","AwayPts","Result","HomeMatches","AwayMatches",
        #        "OddsH1","OddsD1","OddsA1","OddsH2","OddsD2","OddsA2","OddsH3","OddsD3","OddsA3","OddsH4","OddsD4","OddsA4",
        #        "OddsH5","OddsD5","OddsA5","HNplayers","HAverageAge","HNforeign","HPlayerValues","HMarketValue","ANplayers",
        #        "AAverageAge","ANforeign","APlayerValues","AMarketValue","HATT","HMID","HDEF","HOVR","HATT","HMID","HDEF","HOVR"
        #         ]
        self.header_map = []
        self.teams_idx = {}
        self.team_next_idx = 0

    def map(self, csv_file):
        header = True
        X = []
        Y = []
        for row in csv_file:
            txt_vec = row.split(",")
            if header:
                txt_vec[0] = "Index"
                self.header_map = [''.join(val.split()) for val in txt_vec]
                header = False
            else:
                vec = self.build_vec(txt_vec, Y)
                X.append(vec)
        self.header_map.remove("Result")
        return X, Y

    def build_vec(self, txt_vec, Y):
        vec = []
        for col_idx in range(len(txt_vec)):
            col = txt_vec[col_idx]
            col_name = self.header_map[col_idx]
            handler_name = ''.join(col_name.lower().split())
            handler = getattr(self, f"handle_{handler_name}")
            if handler_name == "result":
                Y.append(self.handle_result(col))
            else:
                vec.append(handler(col))
        return vec

    def handle_index(self, val):
        return int(val)

    def handle_home(self, val):
        return self.handle_team(val)

    def handle_away(self, val):
        return self.handle_team(val)

    def handle_team(self, val):
        if val in self.teams_idx:
            return self.teams_idx[val]
        else:
            team_idx = self.team_next_idx
            self.teams_idx[val] = team_idx
            self.team_next_idx += 1
            return team_idx

    def handle_datetime(self, val):
        # date_time_obj = datetime.strptime(val, '%m/%d/%Y %H:%M:%S')
        # return int(date_time_obj.replace(tzinfo=timezone.utc).timestamp())
        return 0

    def handle_home_res(self, val):
        result_arr = val.split("-")
        if len(result_arr) != 2:
            return 1
        if result_arr[0] > result_arr[1]:
            # HOME WIN
            return 1
        else:
            # DRAW OR AWAY WIN
            return -1

    # def handle_away_res(self, val):
    #     result_arr = val.split("-")
    #     if len(result_arr) != 2:
    #         return 1
    #     if result_arr[0] < result_arr[1]:
    #         # HOME WIN
    #         return 1
    #     else:
    #         # DRAW OR HOME WIN
    #         return -1


    def handle_result(self, val):
        result_arr = val.split("-")
        if len(result_arr) != 2:
            return 0
        if result_arr[0] > result_arr[1]:
            # HOME WIN
            return -1
        elif result_arr[0] < result_arr[1]:
            # Away WIN
            return 1
        else:
            # DRAW
            return 0

    def hanle_string_to_int(self, val):
        return 0 if val is "" else int(round(float(val)))

    handle_homepos = handle_homepts = handle_awaypos = handle_awaypts = hanle_string_to_int

    handle_homematches = handle_awaymatches = hanle_string_to_int

    handle_hatt = handle_hmid = handle_hdef = handle_hovr = handle_aatt = handle_amid = handle_adef = handle_aovr = \
        hanle_string_to_int

    def handle_string_to_float(self, val):
        return 0 if val is "" else float(val)

    handle_oddsh1 = handle_oddsd1 = handle_oddsa1 = handle_oddsh2 = handle_oddsd2 = handle_oddsa2 = \
        handle_oddsh3 = handle_oddsd3 = handle_oddsa3 = handle_oddsh4 = handle_oddsd4 = handle_oddsa4 = \
        handle_oddsh5 = handle_oddsd5 = handle_oddsa5 = handle_string_to_float

    handle_hnplayers = handle_hnforeign = handle_anplayers = handle_anforeign = hanle_string_to_int

    handle_haverageage = handle_hplayervalues = handle_hmarketvalue = handle_aaverageage = \
        handle_aplayervalues = handle_amarketvalue = handle_string_to_float

    # def handle_homepos(self, val):
    #     return 0 if val is "" else int(val)
    #
    # def handle_homepts(self, val):
    #     return 0 if val is "" else int(val)
    #
    # def handle_awaypos(self, val):
    #     return 0 if val is "" else int(val)
    #
    # def handle_awaypts(self, val):
    #     return 0 if val is "" else int(val)

    # def handle_homematches(self, val):
    #     return 0 if val is "" else int(val)
    #
    # def handle_awaymatches(self, val):
    #     return 0 if val is "" else int(val)

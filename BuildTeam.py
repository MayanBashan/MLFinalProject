from AllPossibleTeams import build_all_possible_teams
import LinearRegressionMain
def bt_main(mapper, X, Y):
    # average_cost = get_average_cost(mapper, data_tables)
    average_cost = get_average_cost(mapper,  X)
    all_possible_teams = build_all_possible_teams(mapper, X, average_cost)
    LinearRegressionMain.main(mapper, X ,Y, all_possible_teams)


def get_average_cost(mapper, X):
    att_idx = mapper.header_map.index("HATT")
    player_value_idx = mapper.header_map.index("HPlayerValues")
    team_idx = mapper.header_map.index("Home")
    # ATT,MID,DEF
    average_cost = [0, 0, 0]
    average_cost = calculate_average_cost(X, att_idx, player_value_idx, team_idx)
    return average_cost



def calculate_average_cost(X, att_idx, player_cost_idx, team_idx):
    mid_idx = att_idx+1
    def_idx = mid_idx+1
    ovr_idx = def_idx+1
    teams_idx = set()
    vec_per_team = []
    for vec in X:
        if vec[team_idx] not in teams_idx:
            teams_idx.add(vec[team_idx])
            vec_per_team.append(vec)
    sorted_by_players_cost = sorted(vec_per_team, key=lambda x: x[player_cost_idx])
    cost_per_dif = [0,0,0]
    min_cost_team = sorted_by_players_cost[0]
    max_cost_team = sorted_by_players_cost[len(sorted_by_players_cost)-1]
    cost_dif = max_cost_team[player_cost_idx] - min_cost_team[player_cost_idx]
    att_dif = max_cost_team[att_idx] - min_cost_team[att_idx]
    mid_dif = max_cost_team[mid_idx] - min_cost_team[mid_idx]
    def_dif = max_cost_team[def_idx] - min_cost_team[def_idx]
    ovr_dif = max_cost_team[ovr_idx] - min_cost_team[ovr_idx]
    ovr_dif_cost = cost_dif/ovr_dif
    total_dif = att_dif+mid_dif+def_dif
    norm_att_dif = att_dif / total_dif
    norm_mid_dif = mid_dif / total_dif
    norm_def_dif = def_dif / total_dif
    att_dif_cost =  norm_att_dif*ovr_dif_cost
    mid_dif_cost =  norm_mid_dif*ovr_dif_cost
    def_dif_cost =  norm_def_dif*ovr_dif_cost
    cost_per_dif[0] += att_dif_cost
    cost_per_dif[1] += mid_dif_cost
    cost_per_dif[2] += def_dif_cost
    return cost_per_dif
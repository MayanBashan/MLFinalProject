def prompt_set_team_budget(min_cost, max_cost):
    team_budget = input(f"Enter desired team budget ({min_cost}M -> {max_cost}M):")
    team_budget = float(team_budget)
    return team_budget


def build_all_possible_teams_with_budget(min_cost_team_stats, min_cost_team_cost, team_budget, average_cost):
    base_team = min_cost_team_stats
    team_budget -= min_cost_team_cost
    possible_teams = [[att, mid, deff] for att in range(base_team[0], 90) for mid in range(base_team[1], 90) for deff in
                      range(base_team[2], 90)]
    possible_teams = [team for team in possible_teams if (team_budget - 10) <= sum([(team[i]-base_team[i])*average_cost[i] for i in range(len(team))]) <= team_budget]
    possible_teams = list(map(list,set(map(tuple, possible_teams))))
    return possible_teams



def build_all_possible_teams(mapper, flatten_tables, average_cost):
    # average_cost = [10,10,10]
    player_value_idx = mapper.header_map.index("HPlayerValues")
    att_idx = mapper.header_map.index("HATT")
    sorted_by_players_cost = sorted(flatten_tables, key=lambda x: x[player_value_idx])
    min_cost_team = sorted_by_players_cost[0]
    max_cost_team = sorted_by_players_cost[len(sorted_by_players_cost) - 1]
    team_budget = prompt_set_team_budget(min_cost_team[player_value_idx], sum([average_cost[i]*(90-min_cost_team[att_idx+i])
                                                                               for i in range(len(average_cost))])-min_cost_team[player_value_idx])
    possible_teams = build_all_possible_teams_with_budget(min_cost_team[att_idx:att_idx + 3], min_cost_team[player_value_idx],
                                                          team_budget, average_cost)
    return possible_teams

#

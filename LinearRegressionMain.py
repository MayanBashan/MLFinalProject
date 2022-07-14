import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split


def main(mapper, X_base, Y_base, all_possible_teams):
    X,Y = generate_X_and_Y(mapper, X_base, Y_base)
    # print(X,Y)
    x_train = pd.DataFrame(X, columns=["ATT", "MID", "DEF"])
    y_train = pd.DataFrame(Y)
    x_test = pd.DataFrame(all_possible_teams, columns=["ATT", "MID", "DEF"])
    reg = linear_model.LinearRegression()
    reg.fit(x_train,y_train)
    prediction = reg.predict(x_test)
    team_to_prediction = []
    for i in range(len(prediction)):
        team_to_prediction.append([x_test.values[i], prediction[i]])
    teams_sorted_by_prediction = [team for team in sorted(team_to_prediction, key=lambda x: x[1])]
    for team in teams_sorted_by_prediction:
        print(f"Team Stats: {team[0]} | Win Rate Prediction: {team[1]}")
    # df_x = pd.DataFrame(X, columns=["ATT", "MID", "DEF"])
    # df_y = pd.DataFrame(Y)
    # reg = linear_model.LinearRegression()
    # x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.1, random_state=4)
    # reg.fit(x_train,y_train)
    # print(reg.score(x_train,y_train))
    # prediction = reg.predict(x_test)
    # print(reg.score(x_test,y_test))
    # for i in range(len(prediction)):
    #     print(f"Team: {x_test.values[i]} | Prediction: {prediction[i]} | Actual: {y_test.values[i]}")
    # print(np.mean(prediction-y_test)**2)



def generate_X_and_Y(mapper, X, Y):
    home_att_idx = mapper.header_map.index("HATT")
    away_att_idx = mapper.header_map.index("AATT")
    home_team_idx = mapper.header_map.index("Home")
    away_team_idx = mapper.header_map.index("Away")
    team_to_num_wins = []
    id_to_team_num_games_and_wins = {}
    teams_idx = set()
    for i in range(len(X)):
        vec = X[i]
        home_team_num = vec[home_team_idx]
        away_team_num = vec[away_team_idx]
        if home_team_num not in teams_idx:
            teams_idx.add(home_team_num)
            team = vec[home_att_idx:home_att_idx + 3]
            id_to_team_num_games_and_wins[home_team_num] = [team, 0, 0]
        if away_team_num not in teams_idx:
            teams_idx.add(away_team_num)
            team = vec[away_att_idx:away_att_idx + 3]
            id_to_team_num_games_and_wins[away_team_num] = [team, 0, 0]
        result = Y[i]
        id_to_team_num_games_and_wins[home_team_num][1] += 3
        id_to_team_num_games_and_wins[away_team_num][1] += 3
        if result == -1:
            id_to_team_num_games_and_wins[home_team_num][2] += 3
        elif result == 1:
            id_to_team_num_games_and_wins[away_team_num][2] += 3
        else:
            id_to_team_num_games_and_wins[home_team_num][2] += 1
            id_to_team_num_games_and_wins[away_team_num][2] += 1
    # print(id_to_team_num_games_and_wins)
    all_arr = [id_to_team_num_games_and_wins[team_num] for team_num in id_to_team_num_games_and_wins]
    percentage_arr = [[arr[0], arr[2]/arr[1]] for arr in all_arr]
    team_to_num_wins.extend(percentage_arr)
    return [vec[0] for vec in team_to_num_wins], [vec[1] for vec in team_to_num_wins]

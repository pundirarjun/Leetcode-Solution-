import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    result = []
    

    for player in activity["player_id"].unique():
        temp = activity[activity["player_id"] == player]
        first = temp.loc[temp["event_date"].idxmin()]
        result.append({
            "player_id": first["player_id"],
            "first_login": first["event_date"]
        })

    return pd.DataFrame(result)







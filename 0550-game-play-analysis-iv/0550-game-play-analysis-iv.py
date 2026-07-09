import pandas as pd
# Second submission
def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity["first"] = activity.groupby("player_id")["event_date"].transform(min)
    activity_second = activity.loc[activity["first"] + pd.DateOffset(1) == activity["event_date"]]
    return pd.DataFrame({"fraction" : [round(len(activity_second)/activity["player_id"].nunique(),2)]})

# First submission
    # activity['event_date'] = pd.to_datetime(activity['event_date'])

    # activity['first_login'] = activity.groupby('player_id')['event_date'].transform('min')

    # next_day_login = activity[
    #     activity['event_date'] == activity['first_login'] + pd.DateOffset(days=1)
    # ]

    # total_players = activity['player_id'].nunique()
    # next_day_players = next_day_login['player_id'].nunique()

    # fraction = next_day_players / total_players if total_players > 0 else 0.0

    # return pd.DataFrame({'fraction': [round(fraction, 2)]})
    

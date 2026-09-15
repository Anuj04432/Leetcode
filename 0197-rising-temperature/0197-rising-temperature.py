import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values("recordDate")
    
    last_date = weather["recordDate"].shift(1)
    prev_temp = weather["temperature"].shift(1)

    is_consecutive = (weather['recordDate'] - last_date) == pd.Timedelta(days=1)

    is_warmer = weather['temperature'] > prev_temp

    return weather[is_consecutive & is_warmer][['id']]
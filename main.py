import pandas as pd
from datetime import datetime
from swing_trader.swing_trader_class import SwingTrader


def dosya_yukle(coin, baslangic, bitis, pencere):
    tum_data_dosya_adi = f'./coindata/{coin}/{coin}_{pencere}_all.csv'
    main_dataframe = pd.read_csv(tum_data_dosya_adi)

    main_dataframe['open_ts_str'] = main_dataframe[["Open Time"]].apply(pd.to_datetime)
    main_dataframe = main_dataframe.sort_values(by='open_ts_str', ascending=False, ignore_index=True)
    main_dataframe = main_dataframe[main_dataframe['open_ts_str'] < baslangic].reset_index(drop=True)
    main_dataframe = main_dataframe.iloc[0:100]
    print('Tum data !')
    return main_dataframe

if __name__ == '__main__':
    _config = {
        "coin": 'ETHUSDT', "pencere": "4h", "arttir": 4,
        "high": "open", "low": "close"
    }
    baslangic_gunu = datetime.strptime('2021-12-24 16:00:00', '%Y-%m-%d %H:%M:%S')
    bitis_gunu = datetime.strptime('2021-12-24 16:00:00', '%Y-%m-%d %H:%M:%S')
    pencere = _config.get('pencere')
    coin =_config.get("coin")
    series = dosya_yukle(coin, baslangic_gunu, bitis_gunu, pencere)
    swing_data = SwingTrader(series)
    print(swing_data)

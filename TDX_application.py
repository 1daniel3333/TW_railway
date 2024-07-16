from auth_TDX import get_api_return_df
import pandas  as pd

def get_train_basic_station()->pd.DataFrame:
    #get basic information
    api_use = '/v3/Rail/TRA/Station'
    train_basic_info = get_api_return_df(api_use)
    return train_basic_info

def gen_train_hash_from_df(data_raw)->dict:
    """
    Args:
        data (_type_): API回傳的車站資料

    Raises:
        ValueError: 如果遇到異常，就反應錯誤

    Returns:
        dict: 做好的hash map
    """
    data = {}
    try:
        for i, row in data_raw.iterrows():
            station_name = row['Stations']['StationName']['Zh_tw']
            station_id = row['Stations']['StationID']
            data[station_name] = station_id
    except:
        raise ValueError('Get unexpected data type.')
    return data

def get_hash()->dict:
    train_basic_info = get_train_basic_station()
    hash = gen_train_hash_from_df(train_basic_info)
    return hash

def get_train_num_from_train_name(train_name:str, hash)->str:
    train_name_new = train_name.replace('台','臺')
    return hash[train_name_new]

def get_today_format()->str:
    import datetime
    current_date = datetime.date.today()
    return current_date.strftime("%Y-%m-%d")

def get_train_list_from_ini_station_fin_station_date(ini_station:str, fin_station:str, hash:dict, train_date:str=get_today_format())->pd.DataFrame:
    """_summary_

    Args:
        ini_station (str): input as a two word station
        fin_station (str): input as a two word station
        hash(dict): train station hash map
        train_date (str, optional): _description_. Defaults to get_today_format(), format yyyy-MM-dd

    Returns:
        pd.DateFrame: Data from API
    """
    OriginStationID = get_train_num_from_train_name(ini_station, hash)
    DestinationStationID = get_train_num_from_train_name(fin_station, hash)
    test = f'/v3/Rail/TRA/DailyTrainTimetable/OD/Inclusive/{OriginStationID}/to/{DestinationStationID}/{train_date}'
    train_time_table = get_api_return_df(test)
    return train_time_table

def get_arrivetime_by_strain_info(train_info:list, train_list:list)->dict:
    """_summary_

    Args:
        train_info (list): this should be train API return dataframe ['TrainTimetables'][i]['StopTimes'], each element in list is a dict
        train_list (list): list of train id to get time

    Returns:
        dict: train start time by input train list sequence, key is train id and value is time
    """
    res = {}
    for i in range(len(train_info)):
        station_id = train_info[i]['StationID']
        if station_id == train_list[0]:
            res['Start_Station'] = train_info[i]['ArrivalTime']
        elif station_id == train_list[1]:
            res['Arrive_Station'] = train_info[i]['ArrivalTime']
    return res

def get_train_sum_info_from_train_dict(train_info:dict, ini_station:str, fin_station:str, hash:dict):
    """_summary_

    Args:
        train_info (dict): data from API
        ini_station (str): in chinese
        fin_station (str): in chinese
    """
    train_num = train_info['TrainInfo']['TrainNo']
    train_start_loc = train_info['TrainInfo']['StartingStationID']
    OriginStationID = get_train_num_from_train_name(ini_station,hash)
    DestinationStationID = get_train_num_from_train_name(fin_station,hash)
    time_hash = get_arrivetime_by_strain_info(train_info['StopTimes'], [OriginStationID, DestinationStationID])
    time_hash['Train_ID'] = train_num
    time_hash['Is_init_station'] = (train_start_loc==OriginStationID)
    return time_hash

def gen_train_api_info_to_df(data:pd.DataFrame, ini_station:str, fin_station:str, hash:dict)->pd.DataFrame:
    summary_train_status = []
    for i in data['TrainTimetables']:
        summary_train_status.append(get_train_sum_info_from_train_dict(i, ini_station,fin_station, hash))
    return pd.DataFrame(summary_train_status)

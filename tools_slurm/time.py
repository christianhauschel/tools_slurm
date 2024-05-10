import datetime

def time_to_seconds(time_str: str):
    if "-" in time_str:
        days, time = time_str.split("-")
        days = int(days)
    else:
        days = 0
        time = time_str

    time = time.split(":")
    time = [int(t) for t in time]
    time = datetime.timedelta(hours=time[0], minutes=time[1], seconds=time[2])
    time = time.total_seconds()
    time += days * 86400
    return time

def seconds_to_time(time: float):
    if time >= 86400:
        days = int(time/86400)
        time = time - days * 86400
        time = datetime.timedelta(seconds=time)
        time = str(time)
        time = time.split(":")
        time = [int(t) for t in time]
        time = f"{days}-{time[0]:02}:{time[1]:02}:{time[2]:02}"
    else:
        time = datetime.timedelta(seconds=time)
        time = str(time)
        time = time.split(":")
        time = [int(t) for t in time]
        time = f"{time[0]:02}:{time[1]:02}:{time[2]:02}"
    return time
    
# %% test 

# print(time_to_seconds("1-22:0:00"))
# print(seconds_to_time(86400))

# %%
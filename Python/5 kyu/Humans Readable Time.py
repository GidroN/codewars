def make_readable(seconds: int) -> str:
    if seconds > 359999:
        return -1

    minutes = seconds // 60 
    hours = minutes // 60
    

    return (f"{str(hours).zfill(2)}:{str(minutes % 60).zfill(2)}:{str(seconds % 60).zfill(2)}")
def get_in_string(seconds = None) -> dict:
    if not seconds:
        return None
    minutes = seconds // 60
    hours = minutes // 60
    days = hours // 24
    years = days // 365
    return {'years': years, 'days': days % 365, 'hours': hours % 24, 'minutes': minutes % 60, 'seconds': seconds % 60}

def format_duration(seconds: int) -> str:
    if not get_in_string(seconds):
        return 'now'
    time_dict = get_in_string(seconds)
    string = ''
    for key in time_dict.keys():
        if time_dict[key] > 1:
            string += f"{str(time_dict[key])} {key}"
        elif time_dict[key] == 0:
            continue
        elif time_dict[key] == 1:
            string += f"{str(time_dict[key])} {key[:-1]}"
        string += ', '
        
    string = string[:-2]
    string = string[:string.rfind(',')] + string[string.rfind(','):].replace(', ', ' and ')
    return string


# print(get_in_string(132030250))
format_duration(132030250)
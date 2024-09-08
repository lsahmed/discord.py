def dayornight():
    diurnal = ""
    if(data["current"].get("is_day")==0):
        diurnal = "Night"
    elif(data["current"].get("is_day")==1):
        diurnal = "Day"

    return diurnal
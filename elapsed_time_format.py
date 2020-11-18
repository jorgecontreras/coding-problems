def format_duration(seconds):
    #your code here
    out = {}
    out['year'] = seconds // (365 * 86400)
    seconds -= out['year'] * 365 * 86400
    out['day'] = seconds // 86400
    seconds -= out['day'] * 86400
    out['hour'] = seconds // 3600
    seconds -= out['hour'] * 3600
    out['minute'] = seconds // 60
    seconds -= out['minute'] * 60
    out['second'] = seconds
    
    data = ["{} {}".format(v, k) for k,v in out.items() if v > 0]
    
    pending = len(data)
    
    human = ""
    for d in data:
        pending -= 1
        if int(d.split()[0]) > 1:
            d += 's'
        human += d
        if pending > 1:
            human += ", "
        if pending == 1:
            human += " and "
    
    if human == "":
        return "now"
    
    return human

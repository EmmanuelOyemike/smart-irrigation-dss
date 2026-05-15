def get_kc(day):

    if day < 20:
        return 0.4

    elif day < 50:
        return 0.8

    elif day < 90:
        return 1.2

    else:
        return 0.7
    

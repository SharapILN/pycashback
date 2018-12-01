def cashback(amount):
    percent  = 0.05
    limit = 3_000
    result =  amount * percent
    if result > 3000:
        return limit

    return result



def total(values):
    list_sum = sum(values)
    return list_sum
def average(values):
    list_sum = sum(values)
    if len(values) == 0:
        return 'error'
    else:
        result = float(list_sum/(len(values)))
        return result
def median(values):
    if len(values)<=0:
        raise ValueError
    sorted = values.sort()
    if len(sorted) % 2 == 1:
        i = int(len(sorted/2))
        return sorted[i]
    else:
        i = int(len(sorted)/2)
        avg_of_two = (sorted[i]+sorted[i-1])/2
        return avg_of_two

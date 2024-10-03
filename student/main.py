import numpy

def guess(data):
    y = data
    x = list(range(len(y)))

    if len(y) < 2:
        return data[0]-6, data[0]+6
    
    a, b = numpy.polyfit(x, y, 1)
    
    next_y_value = a * len(y) + b
    
    lower_bound = next_y_value - 6
    upper_bound = next_y_value + 6

    return round(lower_bound), round(upper_bound)

# Program entry point
if __name__ == "__main__":
    data = []
    for i in range(12500):
        value = int(input().strip())
        data.append(value)

        lower, upper = guess(data)
        print(lower, upper)
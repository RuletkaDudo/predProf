import json
import matplotlib.pyplot as plt
from  functools import reduce

with open('cities/Алмазный.json') as file:
    data = json.loads(file.read())
    # data[data.index(max(data))] = (data[data.index(max(data)) - 1] + data[data.index(max(data)) + 1]) / 2
    # data[data.index(min(data))] = (data[data.index(min(data)) - 1] + data[data.index(min(data)) + 1]) / 2
    # data[data.index(min(data))] = (data[data.index(min(data)) - 1] + data[data.index(min(data)) + 1]) / 2
    data = [j for j in [data[i * 182: (i + 1) * 182] for i in range(len(data) // 182)]]

    for i in data:
        if data.index(i) % 2 == 0:
            while any([j > 20 for j in i]):
                data[data.index(i)][data[data.index(i)].index(max(data[data.index(i)]))] = (data[data.index(i)][data[data.index(i)].index(max(data[data.index(i)])) + 1] +
                                                        data[data.index(i)][data[data.index(i)].index(max(data[data.index(i)])) - 1]) / 2
        else:
            while any([j < 20 for j in i]):
                data[data.index(i)][data[data.index(i)].index(min(data[data.index(i)]))] = (data[data.index(i)][data[data.index(i)].index(min(data[data.index(i)])) + 1] +
                                                        data[data.index(i)][data[data.index(i)].index(min(data[data.index(i)])) - 1]) / 2
    data = reduce(lambda x, y: x + y, data)
    plt.plot(data)
    plt.show()
import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        list = np.array(list)
        matrix = list.reshape(3,3)
        res = {
            'mean':[[],[],float(list.mean())],
            'variance': [[],[],float(list.var())],
            'standard deviation':[[],[],float(list.std())],
            'max': [[],[],float(list.max())],
            'min': [[],[],float(list.min())],
            'sum': [[],[],float(list.sum())]
        }
        for i in range(0,2):
            res['mean'][i] = np.mean(matrix, axis = i).tolist()
            res['variance'][i] = np.var(matrix, axis = i).tolist()
            res['standard deviation'][i] = np.std(matrix, axis = i).tolist()
            res['max'][i] = np.max(matrix, axis = i).tolist()
            res['min'][i] = np.min(matrix, axis = i).tolist()
            res['sum'][i] = np.sum(matrix, axis = i).tolist()

        return res

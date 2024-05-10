import pickle
lambda_values = pickle.load(open('lambda_values.pkl', 'rb'))
mn = pickle.load(open('min.pkl', 'rb'))
mx = pickle.load(open('max.pkl', 'rb'))

def preprocess(input_data):
    skew_features = ['EC-C', 'BC-C', 'PMS-C', 'SSA', 'Id/Ig', 'T', 'O/C']
    for col in skew_features:
        x = input_data[col]
        transformed_data = (x ** lambda_values[col] - 1) / lambda_values[col]
        input_data[col] = transformed_data
    preprocessed_data = input_data
    # 2-2.使用原始数据的最小值和最大值进行缩放
    features = ['EC-C', 'BC-C', 'PMS-C', 'pH', 'Bio', 'T', 'O/C', 'Id/Ig', 'SSA', 'VIP', 'Gap', 'HN']
    for col in features:
        x = input_data[col]
        normalized_data = (x - mn[col]) / (mx[col] - mn[col])
        preprocessed_data[col] = normalized_data
    return preprocessed_data
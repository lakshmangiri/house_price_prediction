import json
import pickle
import numpy as np

locations = None
data_columns = None
model = None


def get_prices(location, sqft, bhk, bath):
    try:
        loc_index = data_columns.index(location.lower())
    except:
        loc_index = -1

    y = np.zeros(len(data_columns))
    y[0] = sqft
    y[1] = bath
    y[2] = bhk
    if loc_index >= 0:
        y[loc_index] = 1
    return round(model.predict([y])[0], 2)


def get_location():
    return locations


def load_saved_data():
    print('load saved data')
    global data_columns
    global locations
    global model

    with open('./data/columns.json', 'r') as f:
        data_columns = json.load(f)['data_columns']
        locations = data_columns[3:]

    with open('./data/price_prediction_model.pickle', 'rb') as f:
        model = pickle.load(f)
    print('loading data is successful')


if __name__ == '__main__':
    load_saved_data()
    print(get_location())
    print(get_prices('1st Phase JP Nagar', 1000, 3, 3))
    print(get_prices('1st Phase JP Nagar', 1000, 2, 2))
    print(get_prices('Ejipura', 1000, 2, 2))
    print(get_prices('Kalhalli', 1000, 2, 2))

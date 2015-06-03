import cv2
import numpy as np
import csv

def load_image():

    # read image and covert to grayscale
    img = cv2.imread('digits.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # first half as train data, second half as test data
    cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
    x = np.array(cells)
    train = x[:, :50].reshape(-1, 400).astype(np.int8)
    test = x[:, 50:100].reshape(-1,400).astype(np.int8)

    # create labels
    k = np.arange(10)
    train_labels = np.repeat(k, 250)[:, np.newaxis]

    # generate training data array
    train_array = np.column_stack((train_labels, train))
    test_array = test

    return train_array, test_array


def save_csv(fn, data, type):

    with open(fn, 'wb') as f:
        w = csv.writer(f)
        if type == 'train_type':
            w.writerows(data)
        elif type == 'test_type':
            w.writerows([data])

if __name__ == '__main__':

    digit = 0
    train_data, test_data = load_image()

    # save training data for prediction API
    save_csv('train_data.csv', train_data, 'train_type')

    # save testing data files, one sample is selected for each label
    for row in range(0, test_data.shape[0], 250):
        save_csv('test_data/digit_{:>01}.txt'.format(digit), test_data[row], 'test_type')
        digit += 1

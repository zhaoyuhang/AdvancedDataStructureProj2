__author__ = 'Yue Dayu'

from sklearn import svm
import cPickle
import numpy as np
import sys

def readfile(filename):
    list_file = open(filename, 'r')
    _ = list_file.readline()
    lines = list_file.readlines()
    type_list = []
    feature_list = []
    for line in lines:
        current_line = line.split(' ')
        type_list.append((current_line[0]).split('_')[0])
        temp_list = map(float, current_line[1:])
        feature_list.append(temp_list)
    result = np.array(feature_list)
    return type_list, result

def svm_train(filename, output):
    tag, data = readfile(filename)
    clf = svm.SVC(kernel='linear')
    clf.fit(data, tag)
    print clf
    with open(output, 'wb') as f:
        cPickle.dump(clf, f)

if __name__ == '__main__':
    svm_train(sys.argv[1], sys.argv[2])
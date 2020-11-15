import os
from pylab import *
import sys

def get_size(path, current_size):
    try:
        file_list = os.listdir(path)
    except:
        return 0
    new_size = current_size
    for i in file_list:
        if os.path.isdir(os.path.join(path, i)):
            new_size = get_size(os.path.join(path, i), new_size)

        else:
            try:
                new_size += os.path.getsize(os.path.join(path, i))
            except:
                pass
    return new_size

def get_dir_size(path):
    file_list = os.listdir(path)
    result = []
    labels = []
    total = []
    sums = 0
    for i in file_list:
        if os.path.isdir(os.path.join(path, i)):
            size = get_size(os.path.join(path, i), 0)
            result.append(size)
            labels.append(i)
            total.append((i,size))
            sums += size
        else:
            size = os.path.getsize(os.path.join(path, i))
            result.append(size)
            labels.append(i)
            total.append((i,size))
            sums += size

    return result, labels, total, sums

if __name__ == '__main__':
    # path = sys.argv[0]
    # result, labels, total, sums = get_dir_size(os.path(path))
    result, labels, total, sums = get_dir_size('D:\python_project')
    total.sort(key= lambda x:x[-1], reverse = True)
    if sums/1024 > 1024:
        print(sums/1024**2, 'MB')
    else:
        print(sums/1024, 'KB')
    for i in total:
        print('Name: ' + i[0] + '  Size: ' + str(i[-1])+ ' b')
    mpl.rcParams['font.sans-serif']=['SimHei']
    plt.pie(x = result, labels = labels, autopct = '%.2f%%', labeldistance=1.1)
    plt.legend(loc= 0)
    plt.show()

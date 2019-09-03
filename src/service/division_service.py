import json  # 引用json模块
import os


def readAsJson():
    f = open('src\\pca-code.json', encoding='utf-8')
    content = f.read()  # 使用loads()方法，需要先读文件
    user_dic = json.loads(content)
    return user_dic


def read():
    path1 = os.path.abspath('../')
    print("current path %s " % path1)
    with open(path1 + 'src/pca-code.json', encoding='utf-8') as f:
        content = f.read()  # 使用loads()方法，需要先读文件
        return content
    return {}


def findByPid(id):
    array = readAsJson()
    for item in array:
        if (item['code'] == id[0:2]):
            children = item["children"]
            if (len(id) == 2):
                return children
            if (len(id) == 4):
                for item2 in children:
                    if (item2['code'] == id):
                        return item2["children"]
    return []


if __name__ == '__main__':
    arr = findByPid("15")
    print(arr)

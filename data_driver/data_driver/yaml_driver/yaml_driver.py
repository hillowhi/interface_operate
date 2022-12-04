import yaml

'''
yaml数据读取
'''


def load_yaml(path):
    file = open(path, 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    return data

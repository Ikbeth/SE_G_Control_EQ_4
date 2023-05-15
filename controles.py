import json


def cargar():
    with open('config.json') as config:
        controles = json.load(config)
    # print(controles)
    return controles


if __name__ == '__main__':
    controles = cargar()
    print(controles['puerto'])

from json import load, dump

def jsonCreater(json, file=''):
    with open(f'Teste{file}.json', 'w+', encoding='UTF-8') as payload:
        dump(json, payload, indent=4)

def jsonLoad(fileName) -> dict:
    with open(f'Json/{fileName}.json') as payload:
        return load(payload)

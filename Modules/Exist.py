def exist(data: dict, key: any) -> bool:
    if key in data:
        if data[key]:
            return True

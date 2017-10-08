import uuid
#coding=utf-8

def getUUID():
    return uuid.uuid4().__str__()

if __name__ == '__main__':
    print getUUID();

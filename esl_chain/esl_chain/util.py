# -*- coding: utf-8 -*-


# json 데이터를 검사하는 함수
def IsValidJSON( list , json_data ):
    missing = ''
    for key_element in list:
        if not key_element in json_data:
            missing += key_element + ','
    if not 0 == len(missing):
        #빠진게 있으므로 False
        return False, missing
    else:
        #빠진게 없으므로 True
        return True, missing



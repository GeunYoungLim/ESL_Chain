# -*- coding: utf-8 -*-
import qrcode
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from django.conf import settings

# json 데이터를 검사하는 함수
def IsValidJSON( filter , json_data ):
    missing = ''
    for key_element in filter:
        if not key_element in json_data:
            missing += key_element + ','
    if not 0 == len(missing):
        #빠진게 있으므로 False
        return False, missing
    else:
        #빠진게 없으므로 True
        return True, missing


def LabelMaker(itemId, itemName, itemPrice, itemUrl):
    ESL_CHAIN_ROOT = settings.BASE_DIR + '/esl_chain'
    THRESHOLD_VALUE = 200
    qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 3,
    border = 0,
    )
    qr.add_data(itemUrl)
    qr.make(fit=True)
    qrimg = qr.make_image()

    img = Image.open(ESL_CHAIN_ROOT+"/img_esl/origin.bmp")
    draw = ImageDraw.Draw(img)

    name_font = ImageFont.truetype(ESL_CHAIN_ROOT+"/img_esl/malgunbd.ttf", 32)
    price_font = ImageFont.truetype(ESL_CHAIN_ROOT+"/img_esl/ds-digit.ttf", 60)

    draw.text((12, 6), str(itemName), font=name_font)
    draw.text((16, 60), str(itemPrice), font=price_font)

    img.paste(qrimg,(189, 15))
    imgp = ESL_CHAIN_ROOT + "/img_esl/%s.bmp" % itemId
    print(imgp)
    img.save(imgp)

    return itemId

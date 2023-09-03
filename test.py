import easyocr

def easy(cc):
    reader = easyocr.Reader(['ch_sim', 'en'])

    text = reader.readtext('./imgs/2023-09-03-20-36-15.png')

    for i in text:
        print(i)
        if cc in i:
            # print(True)
            # print(type(i))
            return True, i
    return False, None
a,b = easy('取消')
print(a,b)
# a,b = easy('没有')
# print(a,b)
# print(easyocr.__version__)
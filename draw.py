import numpy as np
import cv2
from chahar import glyphs

screen = np.ones((200, 200), dtype=np.uint8)
pointer = screen.shape[1] - 1
text = '''این یک قلم فارسی است.
این قلم در یک فرمت استاندارد نیست و برای استفاده از آن نیاز به
نرم‌افزار خاصی وجود دارد.
این باید تغییر کند. چه فرمتی برای پیاده‌سازی مناسب‌تر است؟
این فرمت باید جوری باشد که بتوان با پایتون آن را خواند و نوشت.
یک فرمت از نوع بیت‌مپ مورد نیاز است.
راستی! اسم این قلم چهار است. ارتفاع همه‌ی نویسه‌های این قلم برابر هشت پیکسل است. پهنای گلیف‌ها متغیر است.
قلم چهار توسط من، عرفان خیراللهی، طراحی و پیاده‌سازی شده است.

'''
text = ' ' + text + ' '


after_n = list("رذزدژاءوؤ!؟?\n. ‌،:؛")
before_n = list(" ‌،؛:.؟!?\n")
fa = list('ضصثقفغعهخحجچشسیبلاتنمکگظطزرذدپوؤءژ')

line = 0
for i in range(1, len(text) - 1):
    glyph = []
    z = text[i]

    # find the right form of character
    if text[i] in fa:
        if text[i+1] not in before_n:
            if text[i] not in after_n:
                z = z + '\u200d'
        if text[i-1] not in after_n:
            z = '\u200d' + z
    
    # find the closest glyph mapped to the form of the character
    if z in glyphs:
        glyph = glyphs[z]
    elif z[1:] in glyphs:
        glyph = glyphs[z[1:]]
    
    elif z[:-1] in glyphs:
        glyph = glyphs[z[:-1]]

    elif z[1:-1] in glyphs:
        glyph = glyphs[z[1:-1]]
    else:
        glyph = glyphs[' ']
    
    # move pointer on the screen to the left by the length of the glyph
    pointer -= len(glyph)

    # decode glyph array
    # convert glyph code into a 2D array of pixels
    ngg = np.zeros((len(glyph), 8))
    for i, g in enumerate(glyph):
        bg = list(map(lambda x:int(x), list(format(g, '#010b')[2:])))
        ngg[i] = np.array(bg)
    nngt = np.transpose(ngg)

    # if you reached the end of the screen, go to the next line.
    if pointer < 0 or '\n' in z:
        line += 1
        pointer = screen.shape[1] - len(glyph) - 1

    # print glyph on the screen (copy it into the proper place)
    screen[line * 9 + 1:line * 9 + 8 + 1, pointer:pointer + np.shape(nngt)[1]] = nngt

# show the image. (for test)
cv2.imshow('q', cv2.resize(screen, (2000, 2000), interpolation=0) * 255)
cv2.imwrite('output.png', cv2.resize(screen, (2000, 2000), interpolation=0) * 255)
cv2.waitKey(0)
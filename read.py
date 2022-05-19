import cv2
import numpy as np
p = cv2.imread('chahar_glyphs.png')
z1 = p[:8, :]
z2 = p[9:17, :]
z = np.concatenate((z2, z1), axis=1)
s0 = 512
q = []
glyphs = []
characters = ['ا', 'آ', '‍آ', 'ب‍', 'ب', 'پ‍', 'پ', 'ت‍', 'ت', 'ث‍', 'ث', 'ج‍', 'ج', 'چ‍', 'چ',
              'ح‍', 'ح', 'خ‍', 'خ', 'د', 'ذ', 'ر', 'ز', 'ژ', 'س‍', 'س', 'ش‍', 'ش', 'ص‍',
              'ص', 'ض‍', 'ض', 'ط‍', 'ط', 'ظ‍', 'ظ', 'ع‍', '‍ع‍', '‍ع', 'ع', 'غ‍', '‍غ‍', '‍غ',
              'غ', 'ف‍', 'ف', 'ق‍', 'ق', 'ک‍', 'ک', 'گ‍', 'گ', 'ل‍', 'ل', 'م‍', '‍م‍', 'م', 'ن‍',
              'ن', 'و', 'ه‍', '‍ه‍', '‍ه', 'ه', 'ی‍', '‍ی', 'ی', '.', '!', '،', '؟', ' ']

for p in range(z.shape[1]-1, -1, -1):
    if z[4, p, 0] == 48:
        if p < s0 - 1:
            gl = z[:, p+1:s0]
            gl[gl[:, :, 0] != 0] = [255, 255, 255]
            gl = cv2.split(gl)[0]
            gll = cv2.transpose(gl) * 1/255
            q = []
            for k in gll:
                qq = int(0)
                for kk in k:
                    qq *= 2
                    qq += int(kk)
                q.append(qq)
            glyphs.append(q)
        s0 = p

print("glyphs = {")
for i in range(len(glyphs)):
    print(f'    "{characters[i]}" : {glyphs[i]},')
print(' "‌" : [],')
print("}")
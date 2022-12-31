# Hackvent 2022
#
# Solution for Challenge HV22.11: Santa's Screenshot Render Function
# URL: https://hackvent.deathspirate.com/
#
# Installation of required libraries:
# pip install opencv-python
#
# See: https://github.com/opencv/opencv/issues/20997

import cv2
import numpy as np
from subprocess import Popen

from hv22_11_symbols import symbols

kWorkDir = './'  # Working directory
kSymSubdir = kWorkDir + "symbols/"  # Directory with character template images
kImgFileName = kWorkDir + 'credentials_for_ocr.png'  # Input image file
kTxtFileName = kWorkDir + 'credentials_for_proofreading.txt'  # Output text file
kOcrFileName = kWorkDir + 'credentials_for_proofreading.png'  # Output image file

debugSym = None

symbolDistMinX = 3

# Load and preprocess image for matching
imgOrig = cv2.imread(kImgFileName)

print(imgOrig.shape)

img_h, img_w = imgOrig.shape[0:2]

img = cv2.cvtColor(imgOrig, cv2.COLOR_BGR2GRAY)
img = ~img

# Empty image for match results
img_rec = np.zeros((img_h, img_w, 3), dtype=np.uint8)

# ROI
# --- Token 1st line: y = 120, height = 13 ---
# line_y = 120
# line_h = 13
# roi_x1 = 0
# roi_x2 = img_w
# roi_y1 = line_y
# roi_y2 = line_y + line_h

roi_x1 = 0
roi_x2 = img_w
roi_y1 = 0
roi_y2 = img_h

imgRoi = img[roi_y1:roi_y2, roi_x1:roi_x2]

text_rows = dict()
sym_count = 0

sym_img_data = []

for sym_idx, sym_entry in enumerate(symbols):

    sym, symFileName, threshold = sym_entry

    if (debugSym is not None) and (sym != debugSym):
        continue

    # Load and preprocess template for matching
    tplOrig = cv2.imread(kSymSubdir + symFileName)

    tpl = cv2.cvtColor(tplOrig, cv2.COLOR_BGR2GRAY)
    tpl = ~tpl

    sym_img_data.append(tpl)

    res = cv2.matchTemplate(imgRoi, tpl, cv2.TM_CCOEFF_NORMED)

    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        x, y = pt[::]

        sym_count += 1

        if y in text_rows:
            row = text_rows[y]

            if x in row:
                stored_sym = row[x][0]
                if stored_sym != sym:
                    print(f"conflict at ({x}, {y}): {stored_sym} vs. {sym}")

                    if stored_sym == 'r' and sym in {'m', 'n'}:
                        row[x] = (sym, sym_idx)
            else:
                row[x] = (sym, sym_idx)
        else:
            row = dict()
            row[x] = (sym, sym_idx)
            text_rows[y] = row

last_x = -symbolDistMinX
last_y = -1
last_sym = ''

draw_list = []

for y, row in sorted(text_rows.items()):
    if y % 15 != 0:
        continue

    print(f"{y} : ", end='')
    for x, sym_entry in sorted(row.items()):

        sym, sym_idx = sym_entry

        if y != last_y or x - last_x >= symbolDistMinX:
            print(sym, end='')
            draw_list.append((x, y, sym, sym_idx))
            last_x = x
            last_y = y
            last_sym = sym
        else:
            if (last_sym == 'r' and sym in {'m', 'n'}) or (last_sym == 'n' and sym == 'm'):
                print('\b' + sym, end='')
                draw_list.pop()
                draw_list.append((x, y, sym, sym_idx))
                last_x = x
                last_y = y
                last_sym = sym

    print()

last_y = -1
txt_decoded = ''

for x, y, sym, sym_idx in draw_list:
    sym_img = sym_img_data[sym_idx]
    sym_h, sym_w = sym_img.shape[0:2]
    img_rec[y + roi_y1:y + roi_y1 + sym_h, x + roi_x1:x + roi_x1 + sym_w, 0] = sym_img

    if 0 <= last_y < y:
        txt_decoded += '\n'

    txt_decoded += sym

    last_y = y

with open(kTxtFileName, 'w') as file_txt:
    file_txt.write(txt_decoded)

# print(text_rows)
# print(sym_count)

# Create mask
img_mask = img_rec.copy()
img_mask[:, :, 1] = img_mask[:, :, 0]
img_mask[:, :, 2] = img_mask[:, :, 0]

img_failed = ~imgOrig
img_failed[:, :, 0] = 0

img_result = np.where(img_mask == 0, img_failed, img_rec)
cv2.imwrite(kOcrFileName, img_result)

Popen(f'"C:/Program Files (x86)/Notepad++/notepad++.exe" {kTxtFileName}', shell=False)
Popen(f'start {kOcrFileName}', shell=True)

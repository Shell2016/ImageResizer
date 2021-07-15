import sys
import os

from PIL import Image


def img_resize(in_folder, out_folder):
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)
    for index, filename in enumerate(os.listdir(in_folder), start=1):
        if filename.endswith('.jpg'):
            try:
                with Image.open(os.path.join(in_folder, filename)) as im:
                    im.thumbnail(size)
                    im.save(os.path.join(
                        out_folder, f'{in_folder}_{index}.jpg'))
                    im.thumbnail(size_thmb)
                    im.save(os.path.join(
                        out_folder, f'{in_folder}_min_{index}.jpg'))
            except OSError:
                print('OSError')


size = 1400, 1400
size_thmb = 400, 400
for input_folder in sys.argv[1:]:	
    output_folder = f'{input_folder}_min'
    img_resize(input_folder, output_folder)






# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)
# for filename in os.listdir(input_folder):
#     if filename.endswith('.jpg'):
#         try:
#             with Image.open(os.path.join(input_folder, filename)) as im:
#                 im.save(os.path.join(output_folder, f'{os.path.splitext(filename)[0]}.png'), 'png')
#         except OSError:
#             print('OSError')

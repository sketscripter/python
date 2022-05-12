from re import X
from exif import Image

folder_path = "C:\\Users\\TONPC\\Documents\\ImagesN\\"
img_filename = 'igre.jpg'
img_path = f'{folder_path}/{img_filename}'

with open(img_path, 'rb') as img_file:
    img = Image(img_file)
  
img.datetime_original = '22.10.2020'
print(f'datetime_original: {img.get("datetime_original")}')    
print(img.has_exif)
print(sorted(img.list_all()))

with open(f'{folder_path}/modified_{img_filename}', 'wb') as new_image_file:
        new_image_file.write(img.get_file())



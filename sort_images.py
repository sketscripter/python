import os
import os.path
import shutil
import exifread

# Chemin ou sont stockés les images a trier
images_path = "C:\\Users\\TONPC\\Documents\\ImagesN\\"

# Chemin ou seront stockés les fichiers
# Si le dossier n'existe pas, il sera crée
dirs_path = "C:\\Users\\TONPC\\Documents\\ImagesTries\\"
if not os.path.exists(dirs_path):
	os.mkdir(dirs_path)



# Compteurs pour le suivi de l'opération de tri
fail_count = 0
success_count = 0

# parcours recursif et stockage du nom et chemin des fichiers .jpg
images = []
for root, dirs, files in os.walk(images_path):
	for f in files:
		if f.endswith(".jpg"):
			images.append(os.path.join(root, f))

# Extraction de la date format YYYY.MM.DD
# Si l'image n'a pas de basile EXIF elle sera envoyée au repertoire 0000
for img in images:
	with open(img, "rb") as file:
		tags = exifread.process_file(file, details=False, stop_tag="DateTimeOriginal")
		try:
			date_path = str(tags["EXIF DateTimeOriginal"])[:10].replace(":", ".")
			success_count += 1
		except:
			print(str(img) + " does not have EXIF tags.")
			fail_count += 1
			date_path = "0000"
		if not os.path.exists(dirs_path + date_path):
			os.mkdir(dirs_path + date_path)
	# On assume que le nom des images est de 4 caracteres
	shutil.move(img, dirs_path + date_path + "\\" + img[-8:])
	# Pour s'assurer du bon déroulement du tri on affiche le chemin des images triées ainsi que leurs balises exif
	print( dirs_path + date_path + "\\" + img[-8:])
	print(tags)

print(str(success_count) + " images triées ")
print(str(fail_count) + " fichiers non triés ")


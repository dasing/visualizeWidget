import os

count = 1
for filename in os.listdir("."):
	ext = os.path.splitext(filename)[-1]

	if ext in { ".jpg", ".JPG", '.jpeg' }:
		new_filename = "%03d" % (count) + ext
		print(filename)
		print(new_filename)
		os.rename(filename, new_filename)
		count += 1
	else:
		print(filename)

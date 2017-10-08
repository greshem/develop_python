from PIL import Image  
import glob, os  
 
size = 250, 250  
   
for infile in glob.glob("*.jpg"):  
	print infile
  	file, ext = os.path.splitext(infile)  
	im = Image.open(infile)  
	im.thumbnail(size, Image.ANTIALIAS)  
	#im.save("thumbnail/" + file + ".thumbnail.jpg", "JPEG")  
	im.save("./" + file + "_thumbnail.jpg", "JPEG")  

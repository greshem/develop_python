from PIL import Image  
import glob, os  
 
size = 650, 650  
   
for infile in glob.glob("*.jpg"):  
  file, ext = os.path.splitext(infile)  
im = Image.open(infile)  
  im.thumbnail(size, Image.ANTIALIAS)  
   im.save("thumbnail/" + file + ".thumbnail.jpg", "JPEG")  
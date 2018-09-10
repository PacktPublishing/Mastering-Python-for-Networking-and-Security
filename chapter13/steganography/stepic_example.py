from PIL import Image
import stepic

#Open an image file in which you want to hide data
image = Image.open("python.png")

#Encode some text into the source image. 
#This returns another Image instance, which can save to a new file

image2 = stepic.encode(image, 'This is the hidden text')
image2.save('python_secrets.png','PNG')

#Use the decode() function to extract data from an image:

image2 = Image.open('python_secrets.png')
s = stepic.decode(image2) 
data = s.decode()

print("Decoded data: " + data)
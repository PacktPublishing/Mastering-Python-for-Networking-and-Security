#!/usr/bin/env python
#--*-- coding:UTF-8 --*--

from PIL import Image
from PIL.ExifTags import TAGS
def get_exif():
	ret = {}
	i = Image.open('images/image.jpg')
	info = i._getexif()
    	#info = i.tag.tags
	for tag, value in info.items():
		decoded = TAGS.get(tag, tag)
		ret[decoded] = value
	return ret

test=get_exif()
print (test)


#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
import requests
import optparse
from urllib.parse import urlparse,urlsplit
from os.path import basename
from bs4 import BeautifulSoup
from PIL import Image
from PIL.ExifTags import TAGS
import os


def findImages(url):
    print('[+] Finding images on ' + url)
    urlContent = urlopen(url).read()
    print(urlContent)
    soup = BeautifulSoup(urlContent,'lxml')
    imgTags = soup.findAll('img')
    return imgTags


def downloadImage(imgTag):
    try:
        print('[+] Dowloading in images directory...'+imgTag['src'])
        imgSrc = imgTag['src']
        imgContent = urlopen(imgSrc).read()
        imgFileName = basename(urlsplit(imgSrc)[2])
        imgFile = open('images/'+imgFileName, 'wb')
        imgFile.write(imgContent)
        imgFile.close()
        return imgFileName
    except Exception as e:
        print(e)
        return ''

def decode_gps_info(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        '''
        Raw Geo-references
        for key in exif['GPSInfo'].keys():
            decode = GPSTAGS.get(key,key)
            gpsinfo[decode] = exif['GPSInfo'][key]
        exif['GPSInfo'] = gpsinfo
        '''

        #Parse geo references.
        Nsec = exif['GPSInfo'][2][2][0] / float(exif['GPSInfo'][2][2][1])
        Nmin = exif['GPSInfo'][2][1][0] / float(exif['GPSInfo'][2][1][1])
        Ndeg = exif['GPSInfo'][2][0][0] / float(exif['GPSInfo'][2][0][1])
        Wsec = exif['GPSInfo'][4][2][0] / float(exif['GPSInfo'][4][2][1])
        Wmin = exif['GPSInfo'][4][1][0] / float(exif['GPSInfo'][4][1][1])
        Wdeg = exif['GPSInfo'][4][0][0] / float(exif['GPSInfo'][4][0][1])
        if exif['GPSInfo'][1] == 'N':
            Nmult = 1
        else:
            Nmult = -1
        if exif['GPSInfo'][1] == 'E':
            Wmult = 1
        else:
            Wmult = -1
        Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
        Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
        exif['GPSInfo'] = {"Lat" : Lat, "Lng" : Lng}

def get_exif_metadata(image_path):
    print(image_path)
    exifData = {}
    image = Image.open(image_path)
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                exifData[decoded] = value
    decode_gps_info(exifData)
    return exifData

def printMetadata():
    print("Extracting metadata from images in images directory.........")
    for dirpath, dirnames, files in os.walk("images"):
        for name in files:
            print("[+] Metadata for file: %s " %(dirpath+os.path.sep+name))
            try:
                exifData = {}
                exif = get_exif_metadata(dirpath+os.path.sep+name)
                for metadata in exif:
                    print("Metadata: %s - Value: %s " %(metadata, exif[metadata]))
                print("\n")
            except:
                import sys, traceback
                traceback.print_exc(file=sys.stdout)

def main():
    parser = optparse.OptionParser('-url <target url>')
    parser.add_option('-u', dest='url', type='string', help='specify url address')

    (options, args) = parser.parse_args()
    url = options.url
    if url == None:
        print(parser.usage)
        exit(0)
    else:
        imgTags = findImages(url)
        print(imgTags)
        for imgTag in imgTags:
            imgFileName = downloadImage(imgTag)
        printMetadata()


if __name__ == '__main__':
    main()

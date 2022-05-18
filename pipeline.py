from pathlib import Path
import glob
import os
import cv2
import numpy as np
import random as rng
import multiprocessing
from joblib import Parallel, delayed
rng.seed(12345)


file_list="leer"
images=""

#class 

def infrastructure():
    global file_list
    file_list=glob.glob("./*.jpg")
#    print(file_list.sort())
    global images
    images=[]
    for file in file_list:
        file_base=file.replace(".jpg","")
        file_base=file_base.replace("./","")
        images.append(file_base)
        Path(file_base).mkdir(parents=True, exist_ok=True)
        os.chdir(file_base)
        fl=glob.glob("*")
        for f in fl:
            os.remove(f)
        os.chdir("..")



#       print(file_base)
    images.sort()
#    print(images)

#def find_images(image):


def process_image(image):
    print("Working on:",image)
    filename=image+".jpg"
    src = cv2.imread(filename)
#    cv2.imshow("Source",src)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(image+"/"+image+"gray.jpg",gray)
#    cv2.imshow("Gray",gray)
#blur = cv2.GaussianBlur(gray, (5,5), 0)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    ksize=1
    blurred = cv2.GaussianBlur(gray, (ksize, ksize), 0)
    threshAd = cv2.adaptiveThreshold(blurred, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 151, 10)
#    cv2.imshow("BW",thresh)
    cv2.imwrite(image+"/"+image+"bw_ad_1.png",threshAd)
    ksize=49
    blurred = cv2.GaussianBlur(gray, (ksize, ksize), 0)
    threshAd = cv2.adaptiveThreshold(blurred, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 151, 10)
#    cv2.imshow("BW",thresh)
    cv2.imwrite(image+"/"+image+"bw_ad_49.png",threshAd)
    ksize=21
    blurred = cv2.GaussianBlur(gray, (ksize, ksize), 0)
    threshAd = cv2.adaptiveThreshold(blurred, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 151, 10)
#    cv2.imshow("BW",thresh)
    cv2.imwrite(image+"/"+image+"bw_ad.png",threshAd)
    cv2.imwrite(image+"/"+image+"bw.png",thresh)
    contours, hierarchy = cv2.findContours(threshAd, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#    print(hierarchy)

    imh, imw = thresh.shape[:2]
#    print(imh,imw)

    contours_poly = [None]*len(contours)
    boundRect = [None]*len(contours)
    centers = [None]*len(contours)
    radius = [None]*len(contours)
    drawing=src
    color=(255,255,0)
    minsize=int(imw/10)
    cv2.rectangle(drawing, (0, 0, minsize, minsize), color, 20)

    for i, c in enumerate(contours):
        lw=2
        color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
        contours_poly[i] = cv2.approxPolyDP(c, 3, True)
        boundRect[i] = cv2.boundingRect(contours_poly[i])
        centers[i], radius[i] = cv2.minEnclosingCircle(contours_poly[i])
#        print(i,boundRect[i])
#        im=src_gray
        x,y,w,h = cv2.boundingRect(c)
        d=0
        ROI = thresh[y-d:y+h+d, x-d:x+w+d]
        plot=0
        if (int(boundRect[i][2]) > minsize and int(boundRect[i][3] > minsize)) : 
            plot=1
#            print(i,boundRect[i],hierarchy[0][i])
#            print(imw-(x+w))
#            print(imh-(y+h))
        # remove borders
            if (int(boundRect[i][0]) == 0):
                plot=0
#                print("left border")
                color=(255,0,255)
                lw=10
            if (int(boundRect[i][1]) == 0):
                plot=0
#                print("top border")
                color=(255,255,0)
                color=(255,0,255)
                lw=10
            if ( imh-(y+h) <= 1):
                plot=0
#                print("bottom border")
                color=(255,0,255)
                lw=10
            if ( imw-(x+w) <= 1):
                plot=0
#                print("right border")
                color=(255,0,255)
                lw=10
#            plot=1
            if (hierarchy[0][i][3] > 0):
                plot=0
#                print("inside other")
                color=(0,255,0)
    #            print(hierarchy[0][i])
    #            print(boundRect[i])
        if (plot == 1):
            print("found image ",image,i)
            color=(255,255,0)
            lw=30
#            print(i,boundRect[i],hierarchy[0][i])
            cv2.imwrite(image+'/ROI_{}_{}.png'.format(image,i), ROI)
            cv2.imwrite('./images/ROI_{}_{}.png'.format(image,i), ROI)
#            print("sum",np.sum(ROI)/np.size(ROI))
        if (int(boundRect[i][2]) > 3 and int(boundRect[i][3] > 3)) : 
             d=0
             if (plot==1): 
                 d=10
             cv2.rectangle(drawing, (x-d , y-d),(x+w+d, y+h+d), color, lw)
             cv2.drawContours(drawing, contours_poly, i, color)	

#    drawing=src
#    for i in range(len(contours)):
#        color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
#        cv2.drawContours(drawing, contours_poly, i, color)
#                cv.drawContours(drawing, contours, i, color, 2, cv.LINE_8, hierarchy, 0)
#        if (int(boundRect[i][2]) > 3 and int(boundRect[i][3] > 3)) : 
#             cv2.rectangle(drawing, (int(boundRect[i][0]), int(boundRect[i][1])), \
#          (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), color, 2)
             
#        print(i)
#        print(cv.rectangle(src_gray, (int(boundRect[i][0]), int(boundRect[i][1])), \
#          (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), #color, 2))
          
#        cv.circle(drawing, (int(centers[i][0]), int(centers[i][1])), int(radius[i]), color, 2)
    
    
#    cv2.imshow('Contours', drawing)
    cv2.imwrite(image+"/"+image+"contours.jpg",drawing)
    cv2.imwrite("./out/"+image+"contours_thumb.jpg",cv2.resize(drawing, (0,0), fx=0.3, fy=0.3))
 
#    cv2.waitKey()







def main():
    print("Hello world")
    print(os.getcwd())
#    print(file_list)
    infrastructure()
#    print(file_list)
#    print(images)
#    process_image(images[158])
#    process_image(images[174])
    Parallel(n_jobs=6)(delayed(process_image)(image) for image in images)
#        process_image(image)



if __name__ == '__main__':
    main()



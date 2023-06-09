import numpy as np
import cv2 as cv
import math
imageName=str(input("Enter the picture name with its extension either .png or .jpg: "))
img=cv.imread(imageName,1)
img=cv.resize(img,(0, 0), fx=0.8, fy=0.8)
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_edges = cv.Canny(img, 100, 100, apertureSize=3)
lines = cv.HoughLinesP(img_edges, 1, math.pi / 180.0, 100, minLineLength=100, maxLineGap=5)
angles = []
# getting the angle for knowing the rotation and to fix it
for x1, y1, x2, y2 in lines[0]:
    cv.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
    angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
    angles.append(angle)
median_angle = np.median(angles)
median_angle2 = np.rad2deg(median_angle) # angle in degrees
#The file initialization part
file = open("Output2.txt","w")
# handling the angles
if median_angle<0:
    image_center = tuple(np.array(img.shape[1::-1]) / 2)
    rot_mat = cv.getRotationMatrix2D(image_center, median_angle, 1)
    result = cv.warpAffine(img, rot_mat, img.shape[1::-1], flags=cv.INTER_LINEAR, borderValue=(255,255,255))
    result = cv.resize(result, (0, 0), fx=0.4, fy=0.4)
    cv.imshow('test', result)
    ret, result = cv.threshold(result, 25, 255, cv.THRESH_BINARY_INV)
    cv.imshow("lessThanZero", result)
    connectivity = 4;
    output = cv.connectedComponentsWithStats(result,
                                             connectivity)  # apply connected components,returns array of 2d_arrays
    num_labels = output[0]  # gets the number of connected components
    centroids = output[3]  # gets the center of each object (connected component)
    print(centroids)

if median_angle>0:
    #image_center = tuple(np.array(img.shape[1::-1]) / 2)
    height, width= img.shape[:2]
    rot_mat = cv.getRotationMatrix2D((width/2, height/2), median_angle, 1.0)
    result = cv.warpAffine(img, rot_mat, img.shape[1::-1], flags=cv.INTER_LINEAR)
    result = cv.resize(result, (0, 0), fx=0.4, fy=0.4)
    cv.imshow("test2", result)
    ret, result = cv.threshold(result, 25, 255, cv.THRESH_BINARY_INV)
    cv.imshow("moreThanZero", result)
    connectivity = 4;
    output = cv.connectedComponentsWithStats(result, connectivity)  # apply connected components,returns array of 2d_arrays
    num_labels = output[0]  # gets the number of connected components
    centroids = output[3]  # gets the center of each object (connected component)
    print(centroids)
    print(num_labels)
if median_angle == 0:
    ret, result = cv.threshold(img, 25, 255, cv.THRESH_BINARY_INV)
    result = cv.resize(result, (0, 0), fx=0.4, fy=0.4)
    cv.imshow("equalsZero", result)
    connectivity=4;
    output = cv.connectedComponentsWithStats(result, connectivity)  # apply connected components,returns array of 2d_arrays
    num_labels = output[0]  # gets the number of connected components
    centroids = output[3]  # gets the center of each object (connected component)
    print(centroids)
    print(num_labels)
counter_Gender=0
counter_Program=0
counter_Semester=0
counter_One1=0
counter_One2=0
counter_One3=0
counter_One4=0
counter_One5=0
counter_Two1=0
counter_Two2=0
counter_Two3=0
counter_Two4=0
counter_Two5=0
counter_Two6=0
counter_Three1=0
counter_Three2=0
counter_Three3=0
counter_Four1=0
counter_Four2=0
counter_Four3=0
counter_Five1=0
counter_Five2=0



# getting to know which circle chosen by using centroids
for i in range(len(centroids)):
    if 385 <= centroids[i][0] and centroids[i][0] <= 435 and 82 <= centroids[i][1] and centroids[i][1] <= 110:
        file.write('Gender: Male'+ '\n')
        counter_Gender+=1
    elif 438 <= centroids[i][0] and centroids[i][0] <= 495and 82 <= centroids[i][1] and centroids[i][1] <= 110:
        file.write('Gender: Female'+ '\n')
        counter_Gender+=1
    elif 150 <= centroids[i][0] and centroids[i][0] <= 200 and 112 <= centroids[i][1] and centroids[i][1] <= 132:
        file.write('Semester: fall '+ '\n')
        counter_Semester+=1
    elif 230 <= centroids[i][0] and centroids[i][0] <= 280 and 112 <= centroids[i][1] and centroids[i][1] <= 132:
        file.write('Semester: spring'+ '\n')
        counter_Semester += 1
    elif 325<= centroids[i][0] and centroids[i][0] <= 370 and 112 <= centroids[i][1] and centroids[i][1] <= 132:
        file.write('Semester: summer'+ '\n')
        counter_Semester += 1
    elif 168 <= centroids[i][0] and centroids[i][0] <= 218 and 136 <= centroids[i][1] and centroids[i][1] <= 152:
        file.write('program: ENVR'+ '\n')
        counter_Program += 1
    elif 222 <= centroids[i][0] and centroids[i][0] <= 248 and 136 <= centroids[i][1] and centroids[i][1] <= 152:
        file.write('program: BLDG'+ '\n')
        counter_Program += 1
    elif 385 <= centroids[i][0] and centroids[i][0] <= 420 and 136 <= centroids[i][1] and centroids[i][1] <= 152:
        file.write('program: MANF'+ '\n')
        counter_Program += 1
    elif 120 <= centroids[i][0] and centroids[i][0] <= 165 and 136 <= centroids[i][1] and centroids[i][1] <= 152:
        file.write('program: MCTA'+ '\n')
        counter_Program += 1
    elif 255 <= centroids[i][0] and centroids[i][0] <= 295 and 136 <= centroids[i][1] and centroids[i][1] <= 152:
        file.write('program: CESS'+ '\n')
        counter_Program += 1
    elif 300 <= centroids[i][0] and centroids[i][0] <= 345 and 136 <= centroids[i][1] and centroids[i][1] <= 152:
        file.write('program: ERGY'+ '\n')
        counter_Program += 1
    elif 348 <= centroids[i][0] and centroids[i][0] <= 380 and 136 <= centroids[i][1] and centroids[i][1] <= 152:
        file.write('program: COMM'+ '\n')
        counter_Program += 1
    elif 120 <= centroids[i][0] and centroids[i][0] <= 165 and 154 <= centroids[i][1] and centroids[i][1] <= 180:
        file.write('program: LAAR'+ '\n')
        counter_Program += 1
    elif 168 <= centroids[i][0] and centroids[i][0] <= 218  and 154 <= centroids[i][1] and centroids[i][1] <= 180:
        file.write('program: MATL'+ '\n')
        counter_Program += 1
    elif 222 <= centroids[i][0] and centroids[i][0] <= 248 and 154 <= centroids[i][1] and centroids[i][1] <= 180:
        file.write('program: CISE'+ '\n')
        counter_Program += 1
    elif 255 <= centroids[i][0] and centroids[i][0] <= 295 and 154 <= centroids[i][1] and centroids[i][1] <= 180:
        file.write('program: HAUD'+ '\n')
        counter_Program += 1

    elif 338 <= centroids[i][0] and centroids[i][0] <= 373 and 305 <= centroids[i][1] and centroids[i][1] <= 321:
        file.write('1.1 : Strongly Agree'+ '\n')
        counter_One1 += 1
    elif 338 <= centroids[i][0] and centroids[i][0] <= 373 and 322 <= centroids[i][1] and centroids[i][1] <= 335:
        file.write('1.2 : Strongly Agree'+ '\n')
        counter_One2 += 1
    elif 338 <= centroids[i][0] and centroids[i][0] <= 373 and 336 <= centroids[i][1] and centroids[i][1] <= 348:
        file.write('1.3 : Strongly Agree'+ '\n')
        counter_One3 += 1
    elif 338 <= centroids[i][0] and centroids[i][0] <= 373 and 349 <= centroids[i][1] and centroids[i][1] <= 360:
        file.write('1.4 : Strongly Agree'+ '\n')
        counter_One4 += 1
    elif 338 <= centroids[i][0] and centroids[i][0] <= 373 and 362 <= centroids[i][1] and centroids[i][1] <= 370:
        file.write('1.5 : Strongly Agree'+ '\n')
        counter_One5 += 1
    elif 375 <= centroids[i][0] and centroids[i][0] <= 410 and 310 <= centroids[i][1] and centroids[i][1] <= 321:
        file.write('1.1 : Agree'+ '\n')
        counter_One1 += 1
    elif 375 <= centroids[i][0] and centroids[i][0] <= 410 and 322 <= centroids[i][1] and centroids[i][1] <= 335:
        file.write('1.2 : Agree'+ '\n')
        counter_One2 += 1
    elif 375 <= centroids[i][0] and centroids[i][0] <= 410 and 336 <= centroids[i][1] and centroids[i][1] <= 348:
        file.write('1.3 : Agree'+ '\n')
        counter_One3 += 1
    elif 375 <= centroids[i][0] and centroids[i][0] <= 410 and 349 <= centroids[i][1] and centroids[i][1] <= 360:
        file.write('1.4 : Agree'+ '\n')
        counter_One4 += 1
    elif 375 <= centroids[i][0] and centroids[i][0] <= 410 and 362 <= centroids[i][1] and centroids[i][1] <= 370:
        file.write('1.5 : Agree'+ '\n')
        counter_One5 += 1
    elif 412 <= centroids[i][0] and centroids[i][0] <= 432 and 310 <= centroids[i][1] and centroids[i][1] <= 321:
        file.write('1.1 : Neutral'+ '\n')
        counter_One1 += 1
    elif 412 <= centroids[i][0] and centroids[i][0] <= 432 and 322 <= centroids[i][1] and centroids[i][1] <= 335:
        file.write('1.2 : Neutral'+ '\n')
        counter_One2 += 1
    elif 412 <= centroids[i][0] and centroids[i][0] <= 432 and 336 <= centroids[i][1] and centroids[i][1] <= 348:
        file.write('1.3 : Neutral'+ '\n')
        counter_One3 += 1
    elif 412 <= centroids[i][0] and centroids[i][0] <= 432 and 349 <= centroids[i][1] and centroids[i][1] <= 360:
        file.write('1.4 : Neutral'+ '\n')
        counter_One4 += 1
    elif 412 <= centroids[i][0] and centroids[i][0] <= 432 and 362 <= centroids[i][1] and centroids[i][1] <= 370:
        file.write('1.5 : Neutral'+ '\n')
        counter_One5 += 1
    elif 434 <= centroids[i][0] and centroids[i][0] <= 463 and 310 <= centroids[i][1] and centroids[i][1] <= 321:
        file.write('1.1 : Disagree'+ '\n')
        counter_One1 += 1
    elif 434 <= centroids[i][0] and centroids[i][0] <= 463 and 322 <= centroids[i][1] and centroids[i][1] <= 335:
        file.write('1.2 : Disagree'+ '\n')
        counter_One2 += 1
    elif 434 <= centroids[i][0] and centroids[i][0] <= 463 and 336 <= centroids[i][1] and centroids[i][1] <= 348:
        file.write('1.3 : Disagree'+ '\n')
        counter_One3 += 1
    elif 434 <= centroids[i][0] and centroids[i][0] <= 463 and 349 <= centroids[i][1] and centroids[i][1] <= 360:
        file.write('1.4 : Disagree'+ '\n')
        counter_One4 += 1
    elif 434 <= centroids[i][0] and centroids[i][0] <= 463 and 362 <= centroids[i][1] and centroids[i][1] <= 370:
        file.write('1.5 : Disagree'+ '\n')
        counter_One5 += 1
    elif 470 <= centroids[i][0] and centroids[i][0] <= 500 and 310 <= centroids[i][1] and centroids[i][1] <= 321:
        file.write('1.1 : Strongly Disagree'+ '\n')
        counter_One1 += 1
    elif 470 <= centroids[i][0] and centroids[i][0] <= 500 and 322 <= centroids[i][1] and centroids[i][1] <= 335:
        file.write('1.2 : Strongly Disagree'+ '\n')
        counter_One2 += 1
    elif 470 <= centroids[i][0] and centroids[i][0] <= 500 and 336 <= centroids[i][1] and centroids[i][1] <= 348:
        file.write('1.3 : Strongly Disagree'+ '\n')
        counter_One3 += 1
    elif 470 <= centroids[i][0] and centroids[i][0] <= 500 and 349 <= centroids[i][1] and centroids[i][1] <= 360:
        file.write('1.4 : Strongly Disagree'+ '\n')
        counter_One4 += 1
    elif 470 <= centroids[i][0] and centroids[i][0] <= 500 and 362 <= centroids[i][1] and centroids[i][1] <= 370:
        file.write('1.5 : Strongly Disagree'+ '\n')
        counter_One5 += 1
    elif 338 <= centroids[i][0] and centroids[i][0] <= 373 and 400 <= centroids[i][1] and centroids[i][1] <= 408:
        file.write('2.1 : Strongly Agree'+ '\n')
        counter_Two1 +=1
    elif 338 <= centroids[i][0] and centroids[i][0] <= 373 and 411 <= centroids[i][1] and centroids[i][1] <= 423:
        file.write('2.2 : Strongly Agree'+ '\n')
        counter_Two2 += 1
    elif 338 <= centroids[i][0] and centroids[i][0] <= 373 and 424 <= centroids[i][1] and centroids[i][1] <= 434:
        file.write('2.3 : Strongly Agree'+ '\n')
        counter_Two3 += 1
    elif 338 <= centroids[i][0] and centroids[i][0] <= 373 and 435 <= centroids[i][1] and centroids[i][1] <= 445:
        file.write('2.4 : Strongly Agree'+ '\n')
        counter_Two4 += 1
    elif 338 <= centroids[i][0] and centroids[i][0] <= 373 and 446 <= centroids[i][1] and centroids[i][1] <= 456:
        file.write('2.5 : Strongly Agree'+ '\n')
        counter_Two5 += 1
    elif 338 <= centroids[i][0] and centroids[i][0] <= 373 and 457 <= centroids[i][1] and centroids[i][1] <= 475:
        file.write('2.6 : Strongly Agree'+ '\n')
        counter_Two6 += 1
    elif 375 <= centroids[i][0] and centroids[i][0] <= 410 and 400 <= centroids[i][1] and centroids[i][1] <= 408:
        file.write('2.1 : Agree'+ '\n')
        counter_Two1 += 1
    elif 375 <= centroids[i][0] and centroids[i][0] <= 410 and 411 <= centroids[i][1] and centroids[i][1] <= 423:
        file.write('2.2 : Agree'+ '\n')
        counter_Two2 += 1
    elif 375 <= centroids[i][0] and centroids[i][0] <= 410 and 424 <= centroids[i][1] and centroids[i][1] <= 434:
        file.write('2.3 : Agree'+ '\n')
        counter_Two3 += 1
    elif 375 <= centroids[i][0] and centroids[i][0] <= 410 and 435 <= centroids[i][1] and centroids[i][1] <= 445:
        file.write('2.4 : Agree'+ '\n')
        counter_Two4 += 1
    elif 375 <= centroids[i][0] and centroids[i][0] <= 410 and 446 <= centroids[i][1] and centroids[i][1] <= 456:
        file.write('2.5 : Agree'+ '\n')
        counter_Two5 += 1
    elif 375 <= centroids[i][0] and centroids[i][0] <= 410 and 457 <= centroids[i][1] and centroids[i][1] <= 475:
        file.write('2.6 : Agree'+ '\n')
        counter_Two6 += 1

    elif 412 <= centroids[i][0] and centroids[i][0] <= 432 and 400 <= centroids[i][1] and centroids[i][1] <= 408:
        file.write('2.1 : Neutral'+ '\n')
        counter_Two1 += 1
    elif 412 <= centroids[i][0] and centroids[i][0] <= 432 and 411 <= centroids[i][1] and centroids[i][1] <= 423:
        file.write('2.2 : Neutral'+ '\n')
        counter_Two2 += 1
    elif 412 <= centroids[i][0] and centroids[i][0] <= 432 and 424 <= centroids[i][1] and centroids[i][1] <= 434:
        file.write('2.3 : Neutral'+ '\n')
        counter_Two3 += 1
    elif 412 <= centroids[i][0] and centroids[i][0] <= 432 and 435 <= centroids[i][1] and centroids[i][1] <= 445:
        file.write('2.4 : Neutral'+ '\n')
        counter_Two4 += 1
    elif 412 <= centroids[i][0] and centroids[i][0] <= 432 and 446 <= centroids[i][1] and centroids[i][1] <= 456:
        file.write('2.5 : Neutral'+ '\n')
        counter_Two5 += 1
    elif 412 <= centroids[i][0] and centroids[i][0] <= 432 and 457 <= centroids[i][1] and centroids[i][1] <= 475:
        file.write('2.6 : Neutral'+ '\n')
        counter_Two6 += 1
    elif 434 <= centroids[i][0] and centroids[i][0] <= 463 and 400 <= centroids[i][1] and centroids[i][1] <= 408:
        file.write('2.1 : Disagree'+ '\n')
        counter_Two1 += 1
    elif 434 <= centroids[i][0] and centroids[i][0] <= 463 and 411 <= centroids[i][1] and centroids[i][1] <= 423:
        file.write('2.2 : Disagree'+ '\n')
        counter_Two2 += 1
    elif 434 <= centroids[i][0] and centroids[i][0] <= 463 and 424 <= centroids[i][1] and centroids[i][1] <= 434:
        file.write('2.3 : Disagree'+ '\n')
        counter_Two3 += 1
    elif 434 <= centroids[i][0] and centroids[i][0] <= 463 and 435 <= centroids[i][1] and centroids[i][1] <= 445:
        file.write('2.4 : Disagree'+ '\n')
        counter_Two4 += 1
    elif 434 <= centroids[i][0] and centroids[i][0] <= 463 and 446 <= centroids[i][1] and centroids[i][1] <= 456:
        file.write('2.5 : Disagree'+ '\n')
        counter_Two5 += 1
    elif 434 <= centroids[i][0] and centroids[i][0] <= 463 and 457 <= centroids[i][1] and centroids[i][1] <= 475:
        file.write('2.6 : Disgree'+ '\n')
        counter_Two6 += 1
    elif 470 <= centroids[i][0] and centroids[i][0] <= 500 and 400 <= centroids[i][1] and centroids[i][1] <= 408:
        file.write('2.1 : Strongly Disagree'+ '\n')
        counter_Two1 += 1
    elif 470 <= centroids[i][0] and centroids[i][0] <= 500 and 411 <= centroids[i][1] and centroids[i][1] <= 423:
        file.write('2.2 : Strongly Disagree'+ '\n')
        counter_Two2 += 1
    elif 470 <= centroids[i][0] and centroids[i][0] <= 500 and 424 <= centroids[i][1] and centroids[i][1] <= 434:
        file.write('2.3 : Strongly Disagree'+ '\n')
        counter_Two3 += 1
    elif 470 <= centroids[i][0] and centroids[i][0] <= 500 and 435 <= centroids[i][1] and centroids[i][1] <= 445:
        file.write('2.4 : Strongly Disagree'+ '\n')
        counter_Two4 += 1
    elif 470 <= centroids[i][0] and centroids[i][0] <= 500 and 446 <= centroids[i][1] and centroids[i][1] <= 456:
        file.write('2.5 : Strongly Disagree'+ '\n')
        counter_Two5 += 1
    elif 470 <= centroids[i][0] and centroids[i][0] <= 500 and 457 <= centroids[i][1] and centroids[i][1] <= 475:
        file.write('2.6 : Strongly Disgree'+ '\n')
        counter_Two6 += 1
    elif 338 <= centroids[i][0] and centroids[i][0] <= 373 and 500 <= centroids[i][1] and centroids[i][1] <= 510:
        file.write('3.1 : Strongly Agree'+ '\n')
        counter_Three1 +=1
    elif 338 <= centroids[i][0] and centroids[i][0] <= 373 and 512 <= centroids[i][1] and centroids[i][1] <= 522:
        file.write('3.2 : Strongly Agree'+ '\n')
        counter_Three2 += 1
    elif 338 <= centroids[i][0] and centroids[i][0] <= 373 and 524 <= centroids[i][1] and centroids[i][1] <= 534:
        file.write('3.3 : Strongly Agree'+ '\n')
        counter_Three3 += 1
    elif 375 <= centroids[i][0] and centroids[i][0] <= 410 and 500 <= centroids[i][1] and centroids[i][1] <= 510:
        file.write('3.1 : Agree'+ '\n')
        counter_Three1 += 1
    elif 375 <= centroids[i][0] and centroids[i][0] <= 410 and 512 <= centroids[i][1] and centroids[i][1] <= 522:
        file.write('3.2 : Agree'+ '\n')
        counter_Three2 += 1
    elif 375 <= centroids[i][0] and centroids[i][0] <= 410 and 524 <= centroids[i][1] and centroids[i][1] <= 534:
        file.write('3.3 : Agree'+ '\n')
        counter_Three3 += 1
    elif 412 <= centroids[i][0] and centroids[i][0] <= 432 and 500 <= centroids[i][1] and centroids[i][1] <= 510:
        file.write('3.1 : Neutral'+ '\n')
        counter_Three1 += 1
    elif 412 <= centroids[i][0] and centroids[i][0] <= 432 and 512 <= centroids[i][1] and centroids[i][1] <= 522:
        file.write('3.2 : Neutral'+ '\n')
        counter_Three2 += 1
    elif 412 <= centroids[i][0] and centroids[i][0] <= 432 and 524 <= centroids[i][1] and centroids[i][1] <= 534:
        file.write('3.3 : Neutral'+ '\n')
        counter_Three3 += 1
    elif 434 <= centroids[i][0] and centroids[i][0] <= 463 and 500 <= centroids[i][1] and centroids[i][1] <= 510:
        file.write('3.1 : Disagree'+ '\n')
        counter_Three1 += 1
    elif 434 <= centroids[i][0] and centroids[i][0] <= 463 and 512 <= centroids[i][1] and centroids[i][1] <= 522:
        file.write('3.2 : Disagree'+ '\n')
        counter_Three2 += 1
    elif 434 <= centroids[i][0] and centroids[i][0] <= 463 and 524 <= centroids[i][1] and centroids[i][1] <= 534:
        file.write('3.3 : Disagree'+ '\n')
        counter_Three3 += 1
    elif 470 <= centroids[i][0] and centroids[i][0] <= 500 and 500 <= centroids[i][1] and centroids[i][1] <= 510:
        file.write('3.1 : Strongly Disagree'+ '\n')
        counter_Three1 += 1
    elif 470 <= centroids[i][0] and centroids[i][0] <= 500 and 512 <= centroids[i][1] and centroids[i][1] <= 522:
        file.write('3.2 : Strongly Disagree'+ '\n')
        counter_Three2 += 1
    elif 470 <= centroids[i][0] and centroids[i][0] <= 500 and 524 <= centroids[i][1] and centroids[i][1] <= 534:
        file.write('3.3 : Strongly Disagree'+ '\n')
        counter_Three3 += 1
    elif 338 <= centroids[i][0] and centroids[i][0] <= 373 and 565 <= centroids[i][1] and centroids[i][1] <= 576:
        file.write('4.1 : Strongly Agree'+ '\n')
        counter_Four1 += 1
    elif 338 <= centroids[i][0] and centroids[i][0] <= 373 and 577 <= centroids[i][1] and centroids[i][1] <= 592:
        file.write('4.2 : Strongly Agree'+ '\n')
        counter_Four2 += 1
    elif 338 <= centroids[i][0] and centroids[i][0] <= 373 and 598 <= centroids[i][1] and centroids[i][1] <= 620:
        file.write('4.3 : Strongly Agree'+ '\n')
        counter_Four3 += 1
    elif 375 <= centroids[i][0] and centroids[i][0] <= 410 and 565 <= centroids[i][1] and centroids[i][1] <= 576:
        file.write('4.1 : Agree'+ '\n')
        counter_Four1 += 1
    elif 375 <= centroids[i][0] and centroids[i][0] <= 410 and 577 <= centroids[i][1] and centroids[i][1] <= 592:
        file.write('4.2 : Agree'+ '\n')
        counter_Four2 += 1
    elif 375 <= centroids[i][0] and centroids[i][0] <= 410 and 598 <= centroids[i][1] and centroids[i][1] <= 620:
        file.write('4.3 : Agree'+ '\n')
        counter_Four3 += 1
    elif 412 <= centroids[i][0] and centroids[i][0] <= 432 and 565 <= centroids[i][1] and centroids[i][1] <= 576:
        file.write('4.1 : Neutral'+ '\n')
        counter_Four1 += 1
    elif 412 <= centroids[i][0] and centroids[i][0] <= 432 and 577 <= centroids[i][1] and centroids[i][1] <= 592:
        file.write('4.2 : Neutral'+ '\n')
        counter_Four2 += 1
    elif 412 <= centroids[i][0] and centroids[i][0] <= 432 and 598 <= centroids[i][1] and centroids[i][1] <= 620:
        file.write('4.3 : Neutral'+ '\n')
        counter_Four3 += 1
    elif 434 <= centroids[i][0] and centroids[i][0] <= 463 and 565 <= centroids[i][1] and centroids[i][1] <= 576:
        file.write('4.1 : Disagree'+ '\n')
        counter_Four1 += 1
    elif 434 <= centroids[i][0] and centroids[i][0] <= 463 and 577 <= centroids[i][1] and centroids[i][1] <= 592:
        file.write('4.2 : Disagree'+ '\n')
        counter_Four2 += 1
    elif 434 <= centroids[i][0] and centroids[i][0] <= 463 and 598 <= centroids[i][1] and centroids[i][1] <= 620:
        file.write('4.3 : Disagree'+ '\n')
        counter_Four3 += 1
    elif 470 <= centroids[i][0] and centroids[i][0] <= 500 and 565 <= centroids[i][1] and centroids[i][1] <= 576:
        file.write('4.1 : Strongly Disagree'+ '\n')
        counter_Four1 += 1
    elif 470 <= centroids[i][0] and centroids[i][0] <= 500 and 577 <= centroids[i][1] and centroids[i][1] <= 592:
        file.write('4.2 : Strongly Disagree'+ '\n')
        counter_Four2 += 1
    elif 470 <= centroids[i][0] and centroids[i][0] <= 500 and 598 <= centroids[i][1] and centroids[i][1] <= 620:
        file.write('4.3 : Strongly Disagree'+ '\n')
        counter_Four3 += 1
    elif 338 <= centroids[i][0] and centroids[i][0] <= 373 and 635 <= centroids[i][1] and centroids[i][1] <= 650:
        file.write('5.1 : Strongly Agree'+ '\n')
        counter_Five1 += 1
    elif 338 <= centroids[i][0] and centroids[i][0] <= 373 and 653 <= centroids[i][1] and centroids[i][1] <= 670:
        file.write('5.2 : Strongly Agree'+ '\n')
        counter_Five2 += 1
    elif 375 <= centroids[i][0] and centroids[i][0] <= 410 and 635 <= centroids[i][1] and centroids[i][1] <= 650:
        file.write('5.1 : Agree'+ '\n')
        counter_Five1 += 1
    elif 375 <= centroids[i][0] and centroids[i][0] <= 410 and 653 <= centroids[i][1] and centroids[i][1] <= 670:
        file.write('5.2 : Agree'+ '\n')
        counter_Five2 += 1
    elif 412 <= centroids[i][0] and centroids[i][0] <= 432 and 635 <= centroids[i][1] and centroids[i][1] <= 650:
        file.write('5.1 : Neutral'+ '\n')
        counter_Five1 += 1
    elif 412 <= centroids[i][0] and centroids[i][0] <= 432 and 653 <= centroids[i][1] and centroids[i][1] <= 670:
        file.write('5.2 : Neutral'+ '\n')
        counter_Five2 += 1
    elif 434 <= centroids[i][0] and centroids[i][0] <= 463 and 635 <= centroids[i][1] and centroids[i][1] <= 650:
        file.write('5.1 : Disagree'+ '\n')
        counter_Five1 += 1
    elif 434 <= centroids[i][0] and centroids[i][0] <= 463 and 653 <= centroids[i][1] and centroids[i][1] <= 670:
        file.write('5.2 : Disagree'+ '\n')
        counter_Five2 += 1
    elif 470 <= centroids[i][0] and centroids[i][0] <= 500 and 635 <= centroids[i][1] and centroids[i][1] <= 650:
        file.write('5.1 : Strongly Disagree'+ '\n')
        counter_Five1 += 1
    elif 470 <= centroids[i][0] and centroids[i][0] <= 500 and 653 <= centroids[i][1] and centroids[i][1] <= 670:
        file.write('5.2 : Strongly Disagree'+ '\n')
        counter_Five2 += 1
#Checking for Errors , mmkn ahotohm wra kol if condition 3shan akhle shaklha helw fl file.write ya3ny w kda
file.write('--------------------------------------------------Error Log--------------------------------------------------'+ '\n')
if counter_Gender==0:
    file.write('Gender: not answered'+ '\n')
elif counter_Gender>1:
    file.write('Gender: more than one answer'+ '\n')
if counter_Semester==0:
    file.write('Semester: not answered'+ '\n')
elif counter_Semester>1:
    file.write('Semester: more than one answer'+ '\n')
if counter_Program==0:
    file.write('Program: not answered'+ '\n')
elif counter_Program>1:
    file.write('Program: more than one answer'+ '\n')
if counter_One1==0:
    file.write('1.1: not answered'+ '\n')
elif counter_One1>1:
    file.write('1.1: more than one answer'+ '\n')
if counter_One2==0:
    file.write('1.2: not answered'+ '\n')
elif counter_One2>1:
    file.write('1.2: more than one answer'+ '\n')
if counter_One3==0:
    file.write('1.3: not answered'+ '\n')
elif counter_One3>1:
    file.write('1.3: more than one answer'+ '\n')
if counter_One4==0:
    file.write('1.4: not answered'+ '\n')
elif counter_One4>1:
    file.write('1.4: more than one answer'+ '\n')
if counter_One5==0:
    file.write('1.5: not answered'+ '\n')
elif counter_One5>1:
    file.write('1.5: more than one answer'+ '\n')
if counter_Two1==0:
    file.write('2.1: not answered'+ '\n')
elif counter_Two1>1:
    file.write('2.1: more than one answer'+ '\n')
if counter_Two2==0:
    file.write('2.2: not answered'+ '\n')
elif counter_Two2>1:
    file.write('2.2: more than one answer'+ '\n')
if counter_Two3==0:
    file.write('2.3: not answered'+ '\n')
elif counter_Two3>1:
    file.write('2.3: more than one answer'+ '\n')
if counter_Two4==0:
    file.write('2.4: not answered'+ '\n')
elif counter_Two4>1:
    file.write('2.4: more than one answer'+ '\n')
if counter_Two5==0:
    file.write('2.5: not answered'+ '\n')
elif counter_Two5>1:
    file.write('2.5: more than one answer'+ '\n')
if counter_Two6==0:
    file.write('2.6: not answered'+ '\n')
elif counter_Two6>1:
    file.write('2.6: more than one answer'+ '\n')
if counter_Three1==0:
    file.write('3.1: not answered'+ '\n')
elif counter_Three1>1:
    file.write('3.1: more than one answer'+ '\n')
if counter_Three2==0:
    file.write('3.2: not answered'+ '\n')
elif counter_Three2>1:
    file.write('3.2: more than one answer'+ '\n')
if counter_Three3==0:
    file.write('3.3: not answered'+ '\n')
elif counter_Three3>1:
    file.write('3.3: more than one answer'+ '\n')
if counter_Four1==0:
    file.write('4.1: not answered'+ '\n')
elif counter_Four1>1:
    file.write('4.1: more than one answer'+ '\n')
if counter_Four2==0:
    file.write('4.2: not answered'+ '\n')
elif counter_Four2>1:
    file.write('4.2: more than one answer'+ '\n')
if counter_Four3==0:
    file.write('4.3: not answered'+ '\n')
elif counter_Four3>1:
    file.write('4.3: more than one answer'+ '\n')
if counter_Five1==0:
    file.write('5.1: not answered'+ '\n')
elif counter_Five1>1:
    file.write('5.1: more than one answer'+ '\n')
if counter_Five2==0:
    file.write('5.2: not answered'+ '\n')
elif counter_Five2>1:
    file.write('5.2: more than one answer'+ '\n')
else:
    file.write('All Clear'+ '\n')
file.write('-------------------------------------------------------------------------------------------------------------'+ '\n')
#The file part
file.close()
file = open("Output2.txt", "r")
print(file.read())
#display original img and angle
img=cv.resize(img,(0, 0), fx=0.4, fy=0.4)
#file.write("Angle is {}".format(median_angle)+ '\n')
#file.write("Angle is {}".format(median_angle2)+ '\n')
cv.imshow("Original",img);
#new = ndimage.rotate(img, 0)
#test_img = imutils.rotate_bound(img, -median_angle)
#cv.imshow("original", test_img)
cv.waitKey(0)

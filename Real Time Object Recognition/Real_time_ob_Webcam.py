import cv2
import numpy as np

MIN_MATCH_COUNT = 25

detector = cv2.xfeatures2d.SIFT_create()
FLANN_INDEX_KDITREE = 0
flannParam = dict(algorithm=FLANN_INDEX_KDITREE,tree=5)
searchParam = dict(check = 50)
flann=cv2.FlannBasedMatcher(flannParam,searchParam)

trainImg=cv2.imread("TrainingData/20kk.PNG")
trainImg1 = cv2.cvtColor(trainImg,cv2.COLOR_BGR2GRAY)
trainKP,trainDecs = detector.detectAndCompute(trainImg1,None)

cam = cv2.VideoCapture(0)


while True:
    ret,image=cam.read()
    QImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    height, width = QImage.shape[:2]
    print("{} {}".format(height,width))

    queryKP,queryDesc = detector.detectAndCompute(QImage,None)
   # Now match the key descriptions from the training image and the query image
    # np.asarray(des1,np.float32),np.asarray(des2,np.float32),k=2
     #   queryDesc,trainDecs, k=2
    matches=flann.knnMatch(queryDesc,trainDecs, k=2)
    print("upper part clear")
    # Filter the pool of keypoints as we need to collect the key points of interest only with the object in mind
    goodMatch=[]
    for m,n in matches:

        if(m.distance<0.75*n.distance):
            goodMatch.append(m)
            print("all ok here")

    if(len(goodMatch)>MIN_MATCH_COUNT):
        tp=[]
        qp=[]
        for m in goodMatch:
            tp.append(trainKP[m.trainIdx].pt)
            qp.append(queryKP[m.queryIdx].pt)
        tp,qp = np.float32((tp,qp))
        H,status = cv2.findHomography(tp,qp,cv2.RANSAC,3.0)
        h,w=trainImg1.shape

        traininBorder=np.float32([[[0,0],[0,h-1],[w-1,h-1],[w-1,0]]])
        queryBorder=cv2.perspectiveTransform(traininBorder,H)
        cv2.polylines(image,[np.int32(queryBorder)],True,(0,255,0),5)
    else:
        print("Not enough matches - {} {}".format(len(goodMatch),MIN_MATCH_COUNT))

    cv2.imshow('result', image)
    cv2.waitKey(10)

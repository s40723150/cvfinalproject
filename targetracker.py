import cv2

############### Tracker Types #####################

#tracker = cv2.TrackerBoosting_create()
#tracker = cv2.TrackerMIL_create()
tracker = cv2.TrackerKCF_create()
#tracker = cv2.TrackerTLD_create()
#tracker = cv2.TrackerMedianFlow_create()
#tracker = cv2.TrackerCSRT_create()
#tracker = cv2.TrackerMOSSE_create()

########################################################

 
cap = cv2.VideoCapture(0)#get the webcam
# TRACKER INITIALIZATION
success, frame = cap.read() #read webcam frame
bbox = cv2.selectROI("Tracking",frame, False) #select the target
tracker.init(frame, bbox) #initialize the tracker with a unknow bounding box


def drawBox(img,bbox):
    # define the "drawBox"
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    # get the box position at the first frame
    cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 255), 3, 3 )
    # draw the box
    #cv2.putText(img, "Tracking", (100, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    # show the "Tracking" text with blue

while True:

    timer = cv2.getTickCount() #
    success, img = cap.read() #return frames
    success, bbox = tracker.update(img) #update the box position

    if success:
        drawBox(img,bbox) #tracking the box
    else:
        cv2.putText(img, "Lost", (100, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # the information box with fps and status
    """
    cv2.rectangle(img,(15,15),(200,90),(255,0,255),2)
    cv2.putText(img, "Fps:", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,255), 2)
    cv2.putText(img, "Status:", (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)
    """

    # calculate the fps and show it
    """
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
    if fps>60: myColor = (20,230,20)
    elif fps>20: myColor = (230,20,20)
    else: myColor = (20,20,230)
    cv2.putText(img,str(int(fps)), (75, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, myColor, 2)
    """

    cv2.imshow("Tracking", img) #show the tracking box

    if cv2.waitKey(1) & 0xff == 27: #exit Tracking
       break


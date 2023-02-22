import cv2
import numpy as np

# Read logo image
logoFileName = "images/Logo.jpg"
img = cv2.imread(logoFileName)
# Set contrast & brightness
alpha = 0.4
beta = -10

# Reduce contrast & brightness
result = cv2.addWeighted(img,alpha,np.zeros(img.shape,img.dtype),0,beta)
# Convert to grayscale image
gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
# Convert to binary image
ret,thresh = cv2.threshold(gray,70,255,0)
# Display the logo
cv2.imshow("AI",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Find objects (All objects in the logo)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


rectanglesList = []
# Look for the outer bounding boxes (no children):
for _, c in enumerate(contours):

    # Get blob area:
    currentArea = cv2.contourArea(c)
    # Set a min area threshold (there are 2 objects with an area equal to 0)
    minArea = 0

    if currentArea > minArea:

        print("currentArea = " + str(currentArea))
        # Approximate the contour to a polygon:
        contoursPoly = cv2.approxPolyDP(c, 3, True)
        # Get the polygon's bounding rectangle:
        boundRect = cv2.boundingRect(contoursPoly)

        # Store rectangles in list:
        rectanglesList.append(boundRect)

        # Get the dimensions of the bounding rect:
        rectX = boundRect[0]
        rectY = boundRect[1]
        rectWidth = boundRect[2]
        rectHeight = boundRect[3]

        # Set bounding rect:
        color = (0, 0, 255)
        cv2.rectangle(img, (int(rectX), int(rectY)),
                   (int(rectX + rectWidth), int(rectY + rectHeight)), color, 2 )

cv2.imshow("Logo detection", img)
cv2.waitKey(0)

print("The logo is composed by " + str(len(rectanglesList)) + "objects")


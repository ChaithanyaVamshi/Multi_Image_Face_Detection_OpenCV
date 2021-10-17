# import opencv python library
# import glob helps in accessing all files in folder
import cv2, glob

# Load all images in list by specifying "*"
all_images = glob.glob("*.jpg")

# load trained XML classifier file using Cascadeclassifier()
detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Use for loop to iterate through each face in all images in folder
for image in all_images:

    img = cv2.imread(image)  # Read the image
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert image into gray scale
    faces = detect.detectMultiScale(gray_img, 1.1, 5)  # Detect faces in image using detectMultiscale()

    for (x, y, w, h) in faces:  # for loop to iterate faces and use x,y,w,h to draw rectangle
        final_img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("Face Detection", final_img)  # Show image
    cv2.waitKey(5000)  # Duration of image to display (msecs)

    cv2.destroyAllWindows()  # De-allocate any associated memory usage

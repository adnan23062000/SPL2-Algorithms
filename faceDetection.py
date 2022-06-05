from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt


cam = cv2.VideoCapture(0)

cv2.namedWindow("Face Recognition")

img_counter = 0

while True:
    ret, frame = cam.read()

    if not ret:
        print("Failed to capture image")
        break

    cv2.imshow("test", frame)

    k = cv2.waitKey(1)

    if k%256 == 27:
        print("escape hit")
        break


    elif k%256 == 32:
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        img_counter+=1

        img1 = cv2.imread('adnan.jpg')

        img2 = cv2.imread(img_name)

        result = DeepFace.verify(img1, img2)

        if result['distance']<0.30:
            print(result['distance'])
            print("Matched")
        else:
            print(result['distance'])
            print("Not Matched")

cam.release()



import cv2
import matplotlib.pyplot as plt

img1_ = cv2.imread('image1.jpg') # 이미지파일로드
img1 = cv2.cvtColor(img1_, cv2.COLOR_BGR2RGB) #bgr형식을 rgb형식으로

# plt.axis('off') #축눈금제거
# plt.imshow(img1) #이미지변수를 이용하여 화면 출력
# plt.show()

img2_ = cv2.imread('image2.jpg') # 이미지파일로드
img2 = cv2.cvtColor(img2_, cv2.COLOR_BGR2RGB) #bgr형식을 rgb형식으로

plt.subplot(121)
plt.axis('off')
plt.imshow(img1)

plt.subplot(122)
plt.axis('off')
plt.imshow(img2)

plt.show()


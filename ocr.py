# import cv2
# import pytesseract
# from pytesseract import Output
# from PIL import Image
# import asyncio
# from concurrent.futures import ThreadPoolExecutor

# img_path = "./sample.png"

# def ocr_text(img_path):
#     # original_image = cv2.imread(img_path)  # 원본 이미지 로드

#     # 이미지 파일 로드
#     image = cv2.imread(img_path)

#     # 이미지 전처리를 위해 흑백으로 변환
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     #한국어가 없을 때 영어가 있는지 확인
#     result = pytesseract.image_to_string(image, lang='eng')
#     print(result)


# ocr_text(img_path)



from PIL import Image
import pytesseract
import cv2

img_path = "./sample.png"
img = Image.open(img_path)

# OpenCV를 사용한 이진화
img_cv = cv2.imread(img_path, 0)
_, thresh = cv2.threshold(img_cv, 150, 255, cv2.THRESH_BINARY)

# PIL 이미지로 변환
img_bin = Image.fromarray(thresh)

# OCR 수행
text = pytesseract.image_to_string(img_bin)
print(text)

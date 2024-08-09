import cv2
import pytesseract
from pytesseract import Output
from PIL import Image
import asyncio
from concurrent.futures import ThreadPoolExecutor

img_path = "./commonImageView2.jpg"

def ocr_text(img_path):
    # original_image = cv2.imread(img_path)  # 원본 이미지 로드

    # 이미지 파일 로드
    image = cv2.imread(img_path)

    # 이미지 전처리를 위해 흑백으로 변환
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    image = Image.open(img_path)
    #한국어가 없을 때 영어가 있는지 확인
    result = pytesseract.image_to_string(gray, lang='kor+eng')
    print(result)


ocr_text(img_path)
from PIL import Image
import numpy as np

im = Image.open('image/sample.png')
ary = np.array(im)

# 이미지 크기 출력(높이×폭×색상)
print(ary.shape)

# 이미지를 흑백으로 변환해 저장
im.convert('L').save('image/sample_mono.png')

# 이미지를 회전시켜 저장(45°로 회전)
im.rotate(45).save('image/sample_rotate.png')
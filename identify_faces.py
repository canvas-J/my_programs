import face_recognition
from PIL import Image, ImageDraw

# 加载已知人物图片
obama_image = face_recognition.load_image_file("me.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
# biden_image = face_recognition.load_image_file("biden.jpg")
# biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
# 对已知面部特征创建数组，并命名
known_face_encodings = [
    obama_face_encoding,
]
known_face_names = [
    "Barack Obama",
]
# 加载需要识别的图片
unknown_image = face_recognition.load_image_file("notme.jpg")
# 找到所有面部及其特征
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)
# 将图像转为PIL格式化图像，便于绘制文字、图框
pil_image = Image.fromarray(unknown_image)
# 创建一个ImageDraw实例
draw = ImageDraw.Draw(pil_image)
# 遍历每个面部
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # 看是否和已知面部匹配
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "Unknown"
    # 如果和数个已知面部特征匹配，返回第一个匹配到的
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]
    # 用PIL绘制出线框
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))
    # 在面部下面绘制标签
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))

# 从内存中移除PIL绘制库
del draw
# 显示结果图片
pil_image.show()
# 保存结果图片
# pil_image.save("image_with_boxes.jpg")
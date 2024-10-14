from PIL import Image

filename = "Белка.jpg"
with Image.open(filename) as img:
    img.load()

img.show()

rotated_img = img.rotate(45)
rotated_img.show()

cmyk_img = img.convert("CMYK")
gray_img = img.convert("L")  # Grayscale

cmyk_img.show()
gray_img.show()




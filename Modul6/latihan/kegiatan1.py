from PIL import Image, ImageOps, ImageDraw, ImageFont

img = Image.open("Modul6/assets/lego.png")

# fontPath = "Modul6/assets/ARIAL.ttf"
# customFont = ImageFont.truetype(fontPath, 250)

defaultFont = ImageFont.load_default()

imgAfter = ImageOps.grayscale(img.copy())
draw = ImageDraw.Draw(imgAfter)

x_coordinate = 70
y_coordinate = 200

text = "Marchanda Balqis\n202110370311503"
image_width, image_height = img.size

text_position = (x_coordinate, y_coordinate)

# text_bbox = draw.textbbox((0, 0), text, font=customFont)
# text_position = ((image_width - text_bbox[2]) // 2, (image_height - text_bbox[3]) // 2)

# draw.text(text_position, text, font=customFont, fill="black")
draw.text(text_position, text, font=defaultFont, fill="black")

imgAfter.save("Modul6/assets/output_kegiatan1.png")
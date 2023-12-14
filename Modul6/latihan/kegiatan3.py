from PIL import Image, ImageEnhance

img = Image.open("Modul6/assets/lego.png")

enhancer = ImageEnhance.Brightness(img)
brightened = enhancer.enhance(1.5)

enhancer = ImageEnhance.Contrast(brightened)
imgAfter = enhancer.enhance(1.2)

imgAfter.save("Modul6/assets/output_kegiatan3.png")
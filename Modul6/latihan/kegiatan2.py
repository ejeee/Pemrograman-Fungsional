from PIL import Image

background_path = "Modul6/assets/home.png"
overlay_path = "Modul6/assets/batman.png"

imgAfter = Image.open(background_path)
overlay = Image.open(overlay_path)

overlay = overlay.convert("RGBA")
overlay = overlay.resize((300, 200))
x_position = 50
y_position = 50

imgAfter.paste(overlay, (x_position, y_position), overlay)
output_path = "Modul6/assets/output_kegiatan2.png"

imgAfter.save(output_path)
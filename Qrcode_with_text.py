import qrcode
from PIL import Image, ImageDraw, ImageFont

# Create QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data("https://www.linkedin.com/in/allmin-fatima")
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="blue", back_color="white").convert("RGB")

# Add a larger logo in the center of the QR code
logo_display = Image.open('logo.png').convert("RGBA")
logo_display = logo_display.resize((120, 120))  # Increased size of the logo
logo_pos = ((img.size[0] - logo_display.size[0]) // 2, (img.size[1] - logo_display.size[1]) // 2)

# Create a mask for the logo to ensure transparency handling
logo_mask = logo_display.convert("L").point(lambda x: min(x, 200))

# Paste the logo onto the QR code image with transparency handling
img.paste(logo_display, logo_pos, mask=logo_mask)

# Create a new image with additional space for the text message
text_message = "Scan to Connect Allmin at Linkedin"
font_size = 25

# Load a font
try:
    font = ImageFont.truetype("arial.ttf", font_size)
except IOError:
    font = ImageFont.load_default()

# Calculate the size needed for the new image
draw = ImageDraw.Draw(img)
text_bbox = draw.textbbox((0, 0), text_message, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]
new_width = img.width
new_height = img.height + text_height + 20  # Add space for text and padding

# Create a new image with extra space for the text
new_img = Image.new('RGB', (new_width, new_height), color='white')
new_img.paste(img, (0, 0))

# Draw the text message below the QR code
draw = ImageDraw.Draw(new_img)
text_x = (new_width - text_width) // 2
text_y = img.height + 10  # Position text 10 pixels below the QR code
draw.text((text_x, text_y), text_message, font=font, fill="black")

# Save the final image
new_img.save("Allmin_linkedin_with_text.png")

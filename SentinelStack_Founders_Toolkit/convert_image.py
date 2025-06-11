from PIL import Image
import os

def convert_to_png(input_path, output_folder="assets/optimized"):
    os.makedirs(output_folder, exist_ok=True)
    img = Image.open(input_path)
    filename = os.path.splitext(os.path.basename(input_path))[0]
    output_path = os.path.join(output_folder, f"{filename}.png")
    img.save(output_path, format="PNG", optimize=True)
    print(f"✅ Konverterad: {output_path}")

# Användning:
# convert_to_png("input/heicbild.heic")

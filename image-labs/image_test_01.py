from PIL import Image, ImageFilter, ImageOps, ImageDraw, ImageEnhance
import sys
import os

#!/usr/bin/env python3
import matplotlib.pyplot as plt

def main():
    # Use command line argument or default image file path
    image_path = sys.argv[1] if len(sys.argv) > 1 else "sample.jpg"
    if not os.path.exists(image_path):
        print(f"File {image_path} not found.")
        sys.exit(1)
    
    # Open image
    img = Image.open(image_path)
    print("Format:", img.format)
    print("Mode:", img.mode)
    print("Size:", img.size)

    # Convert to grayscale
    gray_img = img.convert("L")
    gray_img.save("gray_image.jpg")

    # Resize image to half its size
    new_size = (img.width // 2, img.height // 2)
    resized_img = img.resize(new_size)
    resized_img.save("resized_image.jpg")

    # Crop the image (center square crop)
    width, height = img.size
    min_dim = min(width, height)
    left = (width - min_dim) // 2
    top = (height - min_dim) // 2
    cropped_img = img.crop((left, top, left + min_dim, top + min_dim))
    cropped_img.save("cropped_image.jpg")

    # Apply filters
    edge_img = img.filter(ImageFilter.EDGE_ENHANCE)
    edge_img.save("edge_enhanced_image.jpg")

    blur_img = img.filter(ImageFilter.BLUR)
    blur_img.save("blur_image.jpg")

    # Mirror the image
    mirrored_img = ImageOps.mirror(img)
    mirrored_img.save("mirrored_image.jpg")

    # Enhance contrast
    enhancer = ImageEnhance.Contrast(img)
    contrast_img = enhancer.enhance(1.5)
    contrast_img.save("contrast_image.jpg")

    # Draw a red rectangle border around the image
    img_with_border = img.copy()
    draw = ImageDraw.Draw(img_with_border)
    border_color = (255, 0, 0)
    thickness = 5
    for i in range(thickness):
        draw.rectangle(
            [i, i, img_with_border.width - i - 1, img_with_border.height - i - 1],
            outline=border_color,
        )
    img_with_border.save("bordered_image.jpg")

    # Advanced: Create and save histogram using matplotlib
    histogram = img.histogram()
    plt.figure(figsize=(10, 4))
    if img.mode == "RGB":
        for i, color in enumerate(("r", "g", "b")):
            plt.plot(histogram[i * 256:(i + 1) * 256], color=color)
        plt.title("RGB Histogram")
    elif img.mode == "L":
        plt.plot(histogram, color="black")
        plt.title("Grayscale Histogram")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.savefig("histogram.png")
    plt.close()

    # Advanced: Blend original with mirrored image
    blend_img = Image.blend(img, mirrored_img, alpha=0.5)
    blend_img.save("blend_image.jpg")

    print("Image processing complete. Processed files saved in the current directory.")

if __name__ == "__main__":
    main()
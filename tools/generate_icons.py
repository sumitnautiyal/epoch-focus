import os
from PIL import Image, ImageDraw

# Configuration
# Upscale factor for anti-aliasing (rendering at 4x then downsampling)
SCALE_FACTOR = 4
COLOR_PRIMARY = "#2C2C2C"
COLOR_ACCENT = "#0B57D0"

def generate_icon(size: int, filename: str) -> None:
    """
    Generates a theme icon using Lanczos resampling for high-fidelity edges.
    Renders at (size * SCALE_FACTOR) and downsamples to target size.
    """
    canvas_size = size * SCALE_FACTOR
    center = canvas_size / 2
    
    # Initialize transparent canvas
    img = Image.new('RGBA', (canvas_size, canvas_size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # Geometry Definitions (Relative to canvas size)
    # 1. Outer Structure Ring
    r1 = canvas_size * 0.45
    draw.ellipse(
        [center - r1, center - r1, center + r1, center + r1],
        outline=COLOR_PRIMARY,
        width=int(canvas_size * 0.12)
    )
    
    # 2. Inner Focus Ring
    r2 = canvas_size * 0.28
    draw.ellipse(
        [center - r2, center - r2, center + r2, center + r2],
        outline=COLOR_ACCENT,
        width=int(canvas_size * 0.08)
    )
    
    # 3. Core Node
    r3 = canvas_size * 0.12
    draw.ellipse(
        [center - r3, center - r3, center + r3, center + r3],
        fill=COLOR_PRIMARY
    )

    # Downsample and save
    img = img.resize((size, size), resample=Image.LANCZOS)
    
    output_dir = 'src/icons'
    os.makedirs(output_dir, exist_ok=True)
    img.save(os.path.join(output_dir, filename), 'PNG')
    print(f"Generated asset: {filename}")

if __name__ == "__main__":
    generate_icon(48, "icon-48.png")
    generate_icon(96, "icon-96.png")
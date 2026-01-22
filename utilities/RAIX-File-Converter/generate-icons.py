#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RAIS Document Converter - PWA Icon Generator
Generates all required PWA icon sizes from the RAIS logo
"""

import os
import sys
from PIL import Image

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Icon sizes required for PWA
ICON_SIZES = [72, 96, 128, 144, 152, 192, 384, 512]

def generate_icons(source_image_path, output_dir):
    """Generate all PWA icon sizes from source image"""

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    print(f"Loading source image: {source_image_path}")

    try:
        # Open source image
        img = Image.open(source_image_path)
        print(f"Source image size: {img.size}")
        print(f"Source image mode: {img.mode}")

        # Convert to RGBA if not already (for transparency support)
        if img.mode != 'RGBA':
            print("Converting to RGBA mode...")
            img = img.convert('RGBA')

        # Generate each icon size
        for size in ICON_SIZES:
            output_path = os.path.join(output_dir, f'icon-{size}x{size}.png')

            print(f"Generating {size}x{size} icon...")

            # Resize with high-quality resampling
            resized = img.resize((size, size), Image.Resampling.LANCZOS)

            # Save as PNG with optimization
            resized.save(output_path, 'PNG', optimize=True)

            print(f"  [OK] Created: {output_path}")

        print(f"\n[OK] Successfully generated {len(ICON_SIZES)} icons!")
        print(f"[OK] Icons saved to: {output_dir}")

        return True

    except FileNotFoundError:
        print(f"ERROR: Source image not found: {source_image_path}")
        return False
    except Exception as e:
        print(f"ERROR: Failed to generate icons: {str(e)}")
        return False

def main():
    """Main function"""
    # Get script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Paths
    source_image = os.path.join(script_dir, 'static', 'logo.png')
    output_directory = os.path.join(script_dir, 'static', 'icons')

    print("=" * 60)
    print("RAIS Document Converter - PWA Icon Generator")
    print("=" * 60)
    print()

    # Generate icons
    success = generate_icons(source_image, output_directory)

    if success:
        print()
        print("=" * 60)
        print("Icon generation complete!")
        print("=" * 60)
        print()
        print("Your PWA is now ready to install on:")
        print("  • Windows (Chrome, Edge, Brave)")
        print("  • macOS (Chrome, Edge, Safari)")
        print("  • Linux (Chrome, Firefox, Brave)")
        print("  • iOS (Safari - Add to Home Screen)")
        print("  • Android (Chrome - Install App)")
        print()
    else:
        print()
        print("Icon generation failed. Please check the errors above.")
        return 1

    return 0

if __name__ == '__main__':
    exit(main())

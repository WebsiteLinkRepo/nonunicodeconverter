from PIL import Image, ImageDraw, ImageFont
import subprocess
import os
import sys

def main():
    # Sample text for testing (using common Tamil characters and combinations)
    unicode_text = "தமிழ் மொழி உலகின் மிகத் தொன்மையான செம்மொழிகளில் ஒன்றாகும். அறிவியலும் தொழில்நுட்பமும்."
    
    # Run the TypeScript converter to get Shree-Lipi text
    ts_script = f"""
    import {{ unicodeToShreeLipiTamil }} from '../src/utils/shreeLipiTamilConverter';
    console.log(unicodeToShreeLipiTamil('{unicode_text}'));
    """
    
    with open('/tmp/temp_run.ts', 'w') as f:
        f.write(ts_script)
        
    try:
        result = subprocess.run(['npx', 'tsx', '/tmp/temp_run.ts'], 
                              capture_output=True, text=True, check=True)
        shree_text = result.stdout.strip()
    except Exception as e:
        print(f"Error running TS conversion: {e}")
        return

    # Create image
    width, height = 1200, 300
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)

    # Load fonts
    try:
        # User said they have noto-fonts installed, NotoSansTamil is the standard
        unicode_font = ImageFont.truetype("/usr/share/fonts/noto/NotoSansTamil-Regular.ttf", 32)
    except:
        try:
            # Fallback path if installed locally
            unicode_font = ImageFont.truetype("NotoSansTamil-Regular.ttf", 32)
        except:
            unicode_font = ImageFont.load_default()
            print("Could not load Noto Sans Tamil, using default")

    try:
        shree_font = ImageFont.truetype("../public/Shree_0803.TTF", 32)
    except Exception as e:
        print(f"Could not load Shree_0803.TTF: {e}")
        return

    default_font = ImageFont.load_default()

    # Draw Unicode
    draw.text((20, 20), "Unicode (Noto Sans Tamil):", font=default_font, fill='blue')
    draw.text((20, 60), unicode_text, font=unicode_font, fill='black')

    # Draw Shree-Lipi
    draw.text((20, 140), "Shree-Lipi (SHREE-TAM7-0803):", font=default_font, fill='green')
    draw.text((20, 180), shree_text, font=shree_font, fill='black')
    
    # Save image
    output_path = "shree_tamil_verification_render.png"
    img.save(output_path)
    print(f"Saved visual verification to {output_path}")
    
if __name__ == "__main__":
    # Change to scratch dir so paths line up
    os.chdir('/home/samuelvictor/unicode2nonunicode.com/scratch')
    main()

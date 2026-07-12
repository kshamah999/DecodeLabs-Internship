# ==========================================================
# DecodeLabs AI Internship
# Project 4 - Image Text Recognition System
# Developed by: Kshama Jain
# ==========================================================

import pytesseract
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

# Path to Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

print("=" * 65)
print("🤖 DecodeLabs AI Internship")
print("🖼️ Project 4 - Image Text Recognition System")
print("=" * 65)

name = input("\nEnter your name: ")

print(f"\nHello {name}! 👋")
print("Welcome to the Image Text Recognition System.")

while True:

    print("\n" + "=" * 65)
    print("📋 MENU")
    print("=" * 65)
    print("1. Extract Text from Image")
    print("2. About Project")
    print("3. Exit")

    choice = input("\nEnter your choice (1-3): ")

    # ============================================
    # Extract Text
    # ============================================
    if choice == "1":

        # Hide the Tkinter root window
        root = Tk()
        root.withdraw()

        # Open File Explorer
        image_path = askopenfilename(
            title="Select an Image",
            filetypes=[
                ("Image Files", "*.png *.jpg *.jpeg *.bmp")
            ]
        )

        # User cancelled
        if image_path == "":
            print("\n❌ No image selected.")
            continue

        # Check file exists
        if os.path.exists(image_path):

            try:

                image = Image.open(image_path)

                print("\n🔍 Reading Text...")
                print("=" * 65)

                extracted_text = pytesseract.image_to_string(image)

                print("\n📄 Extracted Text")
                print("=" * 65)

                if extracted_text.strip() == "":
                    print("❌ No text detected in the image.")

                else:
                    print(extracted_text)

                print("=" * 65)
                print("✅ Recognition Completed Successfully!")

            except Exception as e:
                print("\n❌ Error:", e)

        else:
            print("\n❌ Image not found!")

    # ============================================
    # About Project
    # ============================================
    elif choice == "2":

        print("""
=========================================================
Project Name:
Image Text Recognition System

Description:
This project extracts text from an image using
Optical Character Recognition (OCR).

Technology Used:
• Python
• Pillow
• PyTesseract
• Tkinter

Features:
✔ Image Selection using File Explorer
✔ OCR Text Extraction
✔ Menu Driven Interface
✔ Error Handling
✔ Easy to Use

=========================================================
""")

    # ============================================
    # Exit
    # ============================================
    elif choice == "3":

        print(f"\n👋 Thank you, {name}!")
        print("Thanks for using the Image Text Recognition System.")
        print("Have a wonderful day!")
        break

    # ============================================
    # Invalid Choice
    # ============================================
    else:

        print("\n❌ Invalid Choice!")
        print("Please select a valid option.")
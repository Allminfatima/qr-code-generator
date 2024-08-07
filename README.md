# QR Code Generator

This repository contains Python scripts for generating QR codes with various customizations. You can create your QR code by changing the link in the code to your own. In the examples provided, I have used a LinkedIn link, so scanning the QR code will direct you to my LinkedIn profile.

## Files

- **simpleQr.py**
  - Generates a simple QR code.
  - Saves the QR code as an image file.
  - ![Screenshot 2024-08-07 105651](https://github.com/user-attachments/assets/32ed7a87-24d4-4b53-846f-5d9d022577d6)(images/simple_qr_code.png)

    
- **Qr_with_text.py**
  - Generates a QR code with:
    - Customized text below the QR code.
    - QR code color changed from black to blue.
    - A transparent small image behind the QR code.
  - Saves the QR code as an image file.
  - ![Screenshot 2024-08-07 105735](https://github.com/user-attachments/assets/2503049a-3ec8-48fa-b4b6-2f0e4715b399)
(images/qr_with_text.png) 

## Usage

You can create your QR code by changing the link in the code to your own. For example, to link to your LinkedIn profile, replace the existing link with your LinkedIn URL.


## Functionalities
- **simpleQr.py**
   - Generates a simple QR code.
   - Saves the QR code as an image file.
- **Qr_with_text.py**
  - Generates a QR code with:
     - Customized text below the QR code.
     - QR code color changed from black to blue.
     - A transparent small image behind the QR code.
     - Saves the QR code as an image file.


## Necessary Packages

To run these scripts, you need to install the following packages:

```bash
pip install qrcode[pil] Pillow


import qrcode

# Backend URL
backend_url = "https://ingeniumproject-production.up.railway.app/random-image"

# Generate QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(backend_url)
qr.make(fit=True)

# Save the QR Code as an image
img = qr.make_image(fill_color="black", back_color="white")
img.save("random_image_qr.png")




# import qrcode
#
#
# image_url = "https://iyvhuslpradevwbdimbd.supabase.co/storage/v1/object/sign/Nature%20massages/MagicEraser_250212_110759.webp?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJOYXR1cmUgbWFzc2FnZXMvTWFnaWNFcmFzZXJfMjUwMjEyXzExMDc1OS53ZWJwIiwiaWF0IjoxNzM5MzUxNjQ1LCJleHAiOjE3Mzk5NTY0NDV9.KTuGABmbycAr5WA5BuwsexsC5OWLrN7BG33M0zs8Kk8"
#
#
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# qr.add_data(image_url)
# qr.make(fit=True)
#
# # Save the QR Code as an image
# img = qr.make_image(fill_color="black", back_color="white")
# img.save("supabase_image_qr.png")

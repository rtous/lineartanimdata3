import cv2

# Load the image
img = cv2.imread("/Users/rtous/Downloads/disney_toytinkers_part1/frames_upscaled_character/001.png", cv2.IMREAD_UNCHANGED)  # Use IMREAD_UNCHANGED to preserve alpha channel

# Compute half size
width = img.shape[1] // 2
height = img.shape[0] // 2
new_size = (width, height)

# Resize the image
resized_img = cv2.resize(img, new_size, interpolation=cv2.INTER_NEAREST)

# Save the resized image
cv2.imwrite("/Users/rtous/Downloads/disney_toytinkers_part1/frames_upscaled_character/001_downsized.png", resized_img)

print("Image resized successfully!")
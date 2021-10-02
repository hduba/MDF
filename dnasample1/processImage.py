import cv2

# Load image (827 pixels wide, 652 pixels tall)
dna_img = cv2.imread("dna.png")

# Make copy to crop for testing portion
dna_img_test = dna_img.copy()
# Crop to testing portion
dna_img_test = dna_img_test[0:256, 0:256]
# Save testing portion image
cv2.imwrite("dnatest.png", dna_img_test)

# Make copy to crop for validation portion
dna_img_val = dna_img.copy()
# Crop to validation portion
dna_img_val = dna_img_val[256:512, 0:256]
# Save testing portion image
cv2.imwrite("dnaval.png", dna_img_val)

# Make copy to crop for training portion
dna_img_train = dna_img.copy()
# Crop to training portion
dna_img_train = dna_img_train[0:652, 256:827]
# Save testing portion image
cv2.imwrite("dnatrain.png", dna_img_train)

# Display each portion
cv2.imshow("Test", dna_img_test)
cv2.imshow("Val", dna_img_val)
cv2.imshow("Train", dna_img_train)
cv2.waitKey(0)
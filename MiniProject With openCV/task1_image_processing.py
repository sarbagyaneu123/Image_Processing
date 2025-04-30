import cv2

image = cv2.imread("C:\\Users\\sarba\\Downloads\\city_view.jpg.jpeg")

cv2.imwrite("C:\\Users\\sarba\\Downloads\\original_image.jpg", image)


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Use BGR2GRAY (not BGRA2GRAY)
cv2.imwrite("C:\\Users\\sarba\\Downloads\\grayscale_image.jpg", gray_image)

blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
cv2.imwrite(r"c:\Users\sarba\Downloads\blurred_image.jpg", blurred_image)


edges = cv2.Canny(blurred_image, 100, 200)
cv2.imwrite("C:\\Users\\sarba\\Downloads\\canny_edges.jpg", edges)

print("All image processing steps completed successfully.")

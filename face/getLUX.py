import cv2
def calculate_luminance(image):

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    luminance = gray_image.mean()
    return luminance


    

if __name__ == "__main__":
    pass

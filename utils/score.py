import numpy as np
import cv2

#  Mean Squared Error (MSE)
def calc_mse(ground_truth, predicted):
    m = max(ground_truth)
    if m > 1:
        ground_truth = ground_truth[:, :, 0] / 255
        predicted = predicted[:, :, 0] / 255
    return (np.square(ground_truth - predicted)).mean()


#  Mean Abolute Difference (MAD)
def calc_mad(ground_truth, predicted):
    m = max(ground_truth)
    if m > 1:
        ground_truth = ground_truth[:, :, 0] / 255
        predicted = predicted[:, :, 0] / 255
    return (np.abs(ground_truth - predicted)).mean()


#  Sum of Absolute Differences (SAD)
def calc_sad(ground_truth, predicted):
    m = max(ground_truth)
    if m > 1:
        ground_truth = ground_truth[:, :, 0] / 255
        predicted = predicted[:, :, 0] / 255
    error = ground_truth - predicted
    if len(error.shape) == 3:
        error = error.mean(axis=2)
    return np.abs(error).sum()


def calc_error_normalized(ground_truth, predicted, kernel_size=4, power=1):
    """Instead of normalizing for the amount of pixels in an image, normalize for the amount of pixels in the gray
    area of the trimap. This area should scale +- with the edge of the mask/alpha matte, giving a more logical
    destribution of error over different image sizes/mask edge ratios."""
    kernel = np.ones((kernel_size,kernel_size), np.uint8)

    img_erosion = cv2.erode(ground_truth, kernel, iterations=1)
    img_dilation = cv2.dilate(ground_truth, kernel, iterations=2)

    # Take one channel (All channels should have the same values)
    gray = sum*(img_dilation - img_erosion)
    error = np.abs(ground_truth - predicted)
    if power != 1:
        error = error ** power
    return np.sum(error) / gray

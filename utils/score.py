import numpy as np
import cv2
import pandas as pd
import os

#  Mean Squared Error (MSE)
def calc_mse(ground_truth, predicted, gray_area):
    '''
    Function that calculates the Mean Squared Error.
    :param ground_truth: Ground truth mask
    :param predicted: Predicted alpha matte
    :param gray_area: The area of the
    :return: Mean Abolute Error
    '''
    m = np.max(ground_truth)
    if m > 1:
        ground_truth = ground_truth[:, :, 0] / 255
        predicted = predicted[:, :, 0] / 255

    return np.square(ground_truth - predicted) / gray_area


#  Mean Absolute Difference (MAD)
def calc_mad(ground_truth, predicted, gray_area):
    '''
    Function that calculates the Mean Absolute Difference.
    :param ground_truth: Ground truth mask
    :param redicted: Predicted alpha matte
    :return: Mean Abolute Difference
    '''
    m = np.max(ground_truth)
    if m > 1:
        ground_truth = ground_truth[:, :, 0] / 255
        predicted = predicted[:, :, 0] / 255
    return (np.abs(ground_truth - predicted)) / gray_area


#  Sum of Absolute Differences (SAD)
def calc_sad(ground_truth, predicted):
    '''
    Function that calculates the sum of absulute differences
    :param ground_truth: Ground truth mask
    :param predicted: Predicted alpha matte
    :return: Sum of Absolute Differences
    '''
    m = np.max(ground_truth)
    if m > 1:
        ground_truth = ground_truth[:, :, 0] / 255
        predicted = predicted[:, :, 0] / 255
    error = ground_truth - predicted
    if len(error.shape) == 3:
        error = error.mean(axis=2)
    return np.abs(error).sum()


"""def calc_error_normalized(ground_truth, predicted, kernel_size=4, power=1):
    '''
    Instead of normalizing for the amount of pixels in an image, normalize for the amount of pixels in the gray
    area of the trimap. This area should scale +- with the edge of the mask/alpha matte, giving a more logical
    destribution of error over different image sizes/mask edge ratios.
    :param ground_truth: Ground truth mask
    :param predicted: Predicted alpha matte
    :return: Sum of Absolute Differences
    '''

    kernel = np.ones((kernel_size,kernel_size), np.uint8)

    img_erosion = cv2.erode(ground_truth, kernel, iterations=1)
    img_dilation = cv2.dilate(ground_truth, kernel, iterations=2)

    gray = np.sum(img_dilation - img_erosion)
    error = np.abs(ground_truth - predicted)
    if power != 1:
        error = error ** power
    return np.sum(error) / gray"""


def get_scores_alpha_matte(ground_truth_dir, predicted_dir, save_path, kernel_size=4, power=1):
    ground_truth_paths = os.listdir(ground_truth_dir)
    n = len(ground_truth_paths)
    scores = pd.DataFrame(columns=['mse', 'sad', 'mad'])
    for i, img_name in enumerate(ground_truth_paths):
        gt_path = os.path.join(ground_truth_dir, img_name)
        pred_path = os.path.join(predicted_dir, img_name)
        pred_path = pred_path.replace('jpg', 'png')
        gt = cv2.imread(gt_path)
        pred = cv2.imread(pred_path)
        gray_area = compute_gray_area(ground_truth=gt,
                                      kernel_size=4,
                                      it_erosion=1,
                                      it_dilation=2)
        mse = calc_mse(gt, pred, gray_area)
        sad = calc_sad(gt, pred, gray_area)
        mad = calc_mad(gt, pred)
        scores.loc[img_name] = [mse, sad, mad]
        if i % 200 == 0:
            print(f"Progress: {int(i / n * 100)}%")
    print(scores)
    scores.to_csv(save_path)
    return scores


def compute_gray_area(ground_truth, kernel_size=4, it_erosion=1, it_dilation=2):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    img_erosion = cv2.erode(ground_truth, kernel, iterations=it_erosion)
    img_dilation = cv2.dilate(ground_truth, kernel, iterations=it_dilation)

    gray = img_dilation - img_erosion
    gray_area = gray / np.max(gray)
    return gray_area




gt_dir = r'C:\Users\simon\PycharmProjects\image_background_removal\data\DUTS-TE\DUTS-TE-Mask'
pred_dir = r'C:\Users\simon\PycharmProjects\image_background_removal\data\DUTS-TE\MODNet_output'
save_path_ = r'C:\Users\simon\PycharmProjects\image_background_removal\data\scores.csv'
get_scores_alpha_matte(gt_dir, pred_dir, save_path_)

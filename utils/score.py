import numpy as np
import cv2
import pandas as pd
import os
from utils.preprocessing import generate_trimap_from_mask

#  Mean Squared Error (MSE)
def calc_mse(ground_truth, predicted, gray_area):
    '''
    Function that calculates the Mean Squared Error.
    :param ground_truth: Ground truth mask
    :param predicted: Predicted alpha matte
    :param gray_area: The area of the
    :return: Mean Abolute Error
    '''
    mse = np.sum(np.square(ground_truth - predicted)) / gray_area
    return mse


#  Mean Absolute Difference (MAD)
def calc_mad(ground_truth, predicted, gray_area):
    '''
    Function that calculates the Mean Absolute Difference.
    :param ground_truth: Ground truth mask
    :param redicted: Predicted alpha matte
    :param gray_area: The area of the
    :return: Mean Abolute Difference
    '''
    mad = np.sum(np.abs(ground_truth - predicted)) / gray_area
    return mad


#  Sum of Absolute Differences (SAD)
def calc_sad(ground_truth, predicted):
    '''
    Function that calculates the sum of absulute differences
    :param ground_truth: Ground truth mask
    :param predicted: Predicted alpha matte
    :return: Sum of Absolute Differences
    '''
    error = ground_truth - predicted
    if len(error.shape) == 3:
        error = error.mean(axis=2)
    sad = np.abs(error).sum()
    return sad


def get_scores_alpha_matte_folders(ground_truth_dir, predicted_dir, save_path, kernel_size=4, power=1):
    ground_truth_paths = os.listdir(ground_truth_dir)
    n = len(ground_truth_paths)
    scores = pd.DataFrame(columns=['mse', 'sad', 'mad'])
    for i, img_name in enumerate(ground_truth_paths):
        gt_path = os.path.join(ground_truth_dir, img_name)  # ground truth path
        pred_path = os.path.join(predicted_dir, img_name.replace('jpg', 'png'))  # predicted mask path
        if not os.path.isfile(pred_path):
            pred_path = pred_path.replace('jpg', 'png')
        if not os.path.isfile(gt_path):
            gt_path = gt_path.replace('jpg', 'png')
        gt = cv2.imread(gt_path)
        pred = cv2.imread(pred_path)
        gt = reformat_mask(gt)

        pred = reformat_mask(pred)

        gray_area = compute_gray_area(ground_truth=gt,
                                      kernel_size=4,
                                      it_erosion=1,
                                      it_dilation=2)
        mse = calc_mse(gt, pred, gray_area)
        mad = calc_mad(gt, pred, gray_area)
        sad = calc_sad(gt, pred)

        scores.loc[img_name] = [mse, mad, sad]

        if i % 200 == 0:
            print(f"Progress: {int(i / n * 100)}%")
    scores.to_csv(save_path)
    return scores


def compute_gray_area(ground_truth, kernel_size=4, it_erosion=1, it_dilation=2):
    ground_truth = reformat_mask(ground_truth)
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    non_zero_ind = np.nonzero(ground_truth)
    ground_truth[non_zero_ind] = 1
    img_erosion = cv2.erode(ground_truth, kernel, iterations=it_erosion)
    img_dilation = cv2.dilate(ground_truth, kernel, iterations=it_dilation)

    gray = img_dilation - img_erosion
    gray_area = np.sum(gray)
    return gray_area


def reformat_mask(mask):
    m = np.max(mask)
    try:
        if len(mask.shape) == 3:
            mask = mask.mean(axis=2)
    except:
        return -1
    if m > 1:
        mask = mask[:, :] / 255
    return mask


def get_final_scores():
    '''
    Function that gets the 3 different scores of the 3 model outputs
    '''
    model_result_dirs = {
        'DIM': r'C:\Users\simon\PycharmProjects\image_background_removal\data/DUTS-TE/DUTS-TE-Output',
        'MODNet': r'C:\Users\simon\PycharmProjects\image_background_removal\data/DUTS-TE/MODNet_output',
        'U2Net': r'C:\Users\simon\PycharmProjects\image_background_removal\data\DUTS-TE\U2NET_output'

    }
    ground_truth_dir = r'C:\Users\simon\PycharmProjects\image_background_removal\data/DUTS-TE/DUTS-TE-Mask'
    model_scores = {}
    for model, dir_path in model_result_dirs.items():
        print(model, dir_path)
        save_path_ = dir_path + '_scores.csv'
        model_scores[model] = get_scores_alpha_matte_folders(
            ground_truth_dir, dir_path, save_path_
        )
        for key, value in model_scores.items():
            mean = value.mean()
            save_path_ = dir_path + '_scores_mean.csv'
            mean.to_csv(save_path_)

if __name__ == '__main__':
    get_final_scores()

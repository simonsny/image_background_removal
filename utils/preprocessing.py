import cv2
import numpy as np

def generate_trimap_from_path(mask_path,erosion_iter=2,dilate_iter=4):
    """
    Functions that takes in a path for an alpha matte or mask of an image and generates a trimap and saves it.
    :param mask_path: path of the alpha matte or mask
    :param erosion_iter: number of times we do erosion
    :param dilate_iter: number of times we dilate
    :return: name of the mask.
    """
    mask = cv2.imread(mask_path, 0)
    trimap = generate_trimap_from_mask(mask, erosion_iter=2, dilate_iter=4)
    cv2.imwrite(f"/content/drive/MyDrive/BeCode/Faktion/Flask/static/trimap/{mask_path.split('/')[-1]}",trimap)
    return mask_path.split('/')[-1]


def generate_trimap_from_mask(mask,erosion_iter=2,dilate_iter=4):
    """
    Functions that takes in a alpha matte or mask and generates a trimap
    :param mask: An alpha matte of the foreground/background
    :param erosion_iter: number of times we do erosion
    :param dilate_iter: number of times we dilate
    :return: the trimap of an image
    """
    mask[mask >= 20] = 255
    mask[mask < 20] = 0
    d_kernel = np.ones((3,3))
    erode = cv2.erode(mask,d_kernel,iterations=erosion_iter)
    dilate = cv2.dilate(mask,d_kernel,iterations=dilate_iter)

    gray = (dilate-erode)/2
    trimap = erode + gray
    return trimap
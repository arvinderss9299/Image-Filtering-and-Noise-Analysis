import numpy as np


def create_corrupted_image(number_of_images_to_be_created):
    dict_images = {}
    for i in range(number_of_images_to_be_created):
        gray_image = np.full((256, 256), 128)
        additive_gauss_noise = np.random.normal(0, 2, (256, 256))
        corrupted_image = np.add(gray_image, additive_gauss_noise)
        dict_images["image" + str(i)] = corrupted_image
    return dict_images


def est_noise(corr_imgs: dict):
    ideal_image = np.zeros((256, 256))
    var_arr = np.zeros((256, 256))

    for key, value in corr_imgs.items():
        for r in range(256):
            for c in range(256):
                ideal_image[r][c] = ideal_image[r][c] + value[r][c]
    ideal_image = ideal_image*1/len(corr_imgs)

    for key_2, value_2 in corr_imgs.items():
        for r_2 in range(256):
            for c_2 in range(256):
                var_arr[r_2][c_2] = var_arr[r_2][c_2] + np.square(ideal_image[r_2][c_2] - value_2[r_2][c_2])
    std_dev_arr = np.sqrt(var_arr*1/(len(corr_imgs)-1))
    average_std_dev = np.mean(std_dev_arr)
    max_std_dev = np.max(std_dev_arr)
    return average_std_dev, max_std_dev


def box_filter(imgs_to_be_corrected: dict):
    filtered_images = {}
    box = np.ones((3, 3))*1/9

    for key, value in imgs_to_be_corrected.items():
        img_j = value
        corrected_image = np.zeros((256, 256))
        for r_3 in range(256):
            for c_3 in range(256):
                if r_3 == 0 and c_3 == 0:
                    corrected_image[r_3][c_3] = box[1][1] * img_j[r_3][c_3] + \
                                                box[1][2] * img_j[r_3][c_3 + 1] + \
                                                box[2][1] * img_j[r_3 + 1][c_3] + \
                                                box[2][2] * img_j[r_3 + 1][c_3 + 1]
                elif r_3 == 255 and c_3 == 255:
                    corrected_image[r_3][c_3] = box[0][0] * img_j[r_3 - 1][c_3 - 1] + \
                                                box[0][1] * img_j[r_3 - 1][c_3] + \
                                                box[1][0] * img_j[r_3][c_3 - 1] + \
                                                box[1][1] * img_j[r_3][c_3]
                elif r_3 == 255 and c_3 == 0:
                    corrected_image[r_3][c_3] = box[0][1] * img_j[r_3 - 1][c_3] + \
                                                box[0][2] * img_j[r_3 - 1][c_3 + 1] + \
                                                box[1][1] * img_j[r_3][c_3] + \
                                                box[1][2] * img_j[r_3][c_3 + 1]
                elif r_3 == 0 and c_3 == 255:
                    corrected_image[r_3][c_3] = box[1][0] * img_j[r_3][c_3 - 1] + \
                                                box[1][1] * img_j[r_3][c_3] + \
                                                box[2][1] * img_j[r_3 + 1][c_3] + \
                                                box[2][0] * img_j[r_3 + 1][c_3 - 1]
                elif r_3 == 0:
                    corrected_image[r_3][c_3] = box[1][0] * img_j[r_3][c_3 - 1] + \
                                                box[1][1] * img_j[r_3][c_3] + \
                                                box[1][2] * img_j[r_3][c_3 + 1] + \
                                                box[2][0] * img_j[r_3 + 1][c_3 - 1] + \
                                                box[2][1] * img_j[r_3 + 1][c_3] + \
                                                box[2][2] * img_j[r_3 + 1][c_3 + 1]
                elif r_3 == 255:
                    corrected_image[r_3][c_3] = box[0][0] * img_j[r_3 - 1][c_3 - 1] + \
                                                box[0][1] * img_j[r_3 - 1][c_3] + \
                                                box[0][2] * img_j[r_3 - 1][c_3 + 1] + \
                                                box[1][0] * img_j[r_3][c_3 - 1] + \
                                                box[1][1] * img_j[r_3][c_3] + \
                                                box[1][2] * img_j[r_3][c_3 + 1]
                elif c_3 == 0:
                    corrected_image[r_3][c_3] = box[0][1] * img_j[r_3 - 1][c_3] + \
                                                box[0][2] * img_j[r_3 - 1][c_3 + 1] + \
                                                box[1][1] * img_j[r_3][c_3] + \
                                                box[1][2] * img_j[r_3][c_3 + 1] + \
                                                box[2][1] * img_j[r_3 + 1][c_3] + \
                                                box[2][2] * img_j[r_3 + 1][c_3 + 1]
                elif c_3 == 255:
                    corrected_image[r_3][c_3] = box[0][0] * img_j[r_3 - 1][c_3 - 1] + \
                                                box[0][1] * img_j[r_3 - 1][c_3] + \
                                                box[1][0] * img_j[r_3][c_3 - 1] + \
                                                box[1][1] * img_j[r_3][c_3] + \
                                                box[2][0] * img_j[r_3 + 1][c_3 - 1] + \
                                                box[2][1] * img_j[r_3 + 1][c_3]
                else:
                    corrected_image[r_3][c_3] = box[0][0]*img_j[r_3 - 1][c_3 - 1] + \
                                                box[0][1]*img_j[r_3 - 1][c_3] + \
                                                box[0][2]*img_j[r_3 - 1][c_3 + 1] + \
                                                box[1][0]*img_j[r_3][c_3 - 1] + \
                                                box[1][1]*img_j[r_3][c_3] + \
                                                box[1][2]*img_j[r_3][c_3 + 1] + \
                                                box[2][0]*img_j[r_3 + 1][c_3 - 1] + \
                                                box[2][1]*img_j[r_3 + 1][c_3] + \
                                                box[2][2]*img_j[r_3 + 1][c_3 + 1]
        filtered_images[key] = corrected_image
    return filtered_images


if __name__ == "__main__":
    corrupt_images_10 = create_corrupted_image(10)
    avg_std_noise_before, max_std_before = est_noise(corrupt_images_10)
    print(f"Average standard deviation of noise before filtering: {avg_std_noise_before}")
    print(f"Maximum standard deviation of noise before filtering: {max_std_before}")
    corrected_images = box_filter(corrupt_images_10)
    avg_std_noise_after, max_std_after = est_noise(corrected_images)
    print(f"Average standard deviation of noise after filtering: {avg_std_noise_after}")
    print(f"Maximum standard deviation of noise after filtering: {max_std_after}")

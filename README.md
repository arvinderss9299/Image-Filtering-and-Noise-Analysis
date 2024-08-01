# Image Noise Analysis and Filtering

This project demonstrates the generation of grayscale images corrupted with Gaussian noise, the estimation of noise, and the application of a box filter to analyze noise reduction. The code generates images with a specified level of Gaussian noise, estimates the noise levels before and after filtering, and evaluates the effectiveness of the filtering process.

## Project Overview

1. **Image Generation**: Ten 256x256 grayscale images with a gray level of 128 are generated. Each image is corrupted with additive Gaussian noise with a zero mean and a standard deviation of 2.0.

2. **Noise Estimation**: The noise in the images is estimated using procedures from Chapter 2 of "Trucco and Verri". This involves calculating the average and maximum standard deviation of the noise in the images before and after applying a 3x3 box filter.

3. **Image Filtering**: A 3x3 box filter is applied to the noisy images to reduce the noise. The noise is re-estimated after filtering to assess the impact of the box filter.

## Requirements

- Python 3.x
- NumPy

## Code Overview

### `create_corrupted_image(number_of_images_to_be_created)`

Generates grayscale images corrupted with Gaussian noise.

- **Inputs**: `number_of_images_to_be_created` (int) - Number of images to generate.
- **Outputs**: Dictionary of corrupted images.

### `est_noise(corr_imgs)`

Estimates the noise in the provided images.

- **Inputs**: `corr_imgs` (dict) - Dictionary of corrupted images.
- **Outputs**: Tuple containing the average and maximum standard deviation of the noise.

### `box_filter(imgs_to_be_corrected)`

Applies a 3x3 box filter to reduce noise in the images.

- **Inputs**: `imgs_to_be_corrected` (dict) - Dictionary of images to be filtered.
- **Outputs**: Dictionary of filtered images.

### `main()`

Generates the images, estimates noise before and after filtering, applies the box filter, and prints the results.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/arvinderss9299/Image-Filtering-and-Noise-Analysis.git
    cd Image-Filtering-and-Noise-Analysis
    ```

2. Run the Python script:

    ```bash
    python noise_analysis.py
    ```

3. Review the output to see the average and maximum standard deviations of the noise before and after filtering.

## Results

The results will provide:

- Average and maximum standard deviations of noise before filtering.
- Average and maximum standard deviations of noise after applying the box filter.

## Discussion

The results will demonstrate the effectiveness of the 3x3 box filter in reducing Gaussian noise. By comparing the estimated noise levels before and after filtering, you can evaluate the performance of the filter.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

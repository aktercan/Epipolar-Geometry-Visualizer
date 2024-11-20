# Epipolar Geometry Visualizer

This project provides a Python-based tool to visualize epipolar geometry between two stereo images. Using a fundamental matrix and user-selected points, the tool computes and plots epipolar lines on the corresponding images.

## Features

    •    User-Interactive Point Selection: Select points interactively on the first image for analysis.
    •    Fundamental Matrix Integration: Compute epipolar lines on the second image using a pre-defined fundamental matrix.
    •    Epipolar Geometry Visualization: Display the selected points and their corresponding epipolar lines side-by-side for a comprehensive analysis.

## Why This Project?

Epipolar geometry is a fundamental concept in computer vision and stereo image analysis. It is essential for understanding the spatial relationship between two images captured from different viewpoints. This project provides a practical and visual representation of epipolar lines and their correspondence, making it an invaluable tool for educational purposes and research.

## How It Works

    1.    User Interaction:
    •    Select points interactively on the first image.
    •    Points are highlighted and stored for further computation.
   
    2.    Fundamental Matrix:
    •    A predefined fundamental matrix is used to compute the epipolar lines.
   
    3.    Visualization:
    •    Selected points are displayed on the first image.
    •    Corresponding epipolar lines are plotted on the second image.
    •    Results are displayed side-by-side for comparison.

## Requirements

To run the project, ensure you have the following installed:
    •    Python 3.8+
    •    Libraries:
    •    opencv-python
    •    numpy
    •    matplotlib

## Example Output

    •    Left: Selected points on the first image.
    •    Right: Corresponding epipolar lines on the second image.




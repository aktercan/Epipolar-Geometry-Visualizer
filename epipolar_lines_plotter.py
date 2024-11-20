import cv2
import numpy as np
import matplotlib.pyplot as plt

def read_image(path):
    """
    Reads an image from a given path and ensures it is loaded correctly.
    """
    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError(f"Image at path '{path}' could not be loaded.")
    return image

def compute_epipolar_lines(F, points):
    """
    Compute epipolar lines for given points using the fundamental matrix.
    """
    points_h = np.hstack((points, np.ones((points.shape[0], 1))))  # Add homogeneous coordinates
    lines = np.dot(F, points_h.T).T  # Compute epipolar lines
    return lines

def user_select_points(image):
    """
    Allow the user to select points on the image interactively.
    """
    points = []

    def onclick(event):
        if event.xdata is not None and event.ydata is not None:
            points.append((event.xdata, event.ydata))
            plt.scatter(event.xdata, event.ydata, c='red', marker='x')
            plt.draw()

    print("Select points on the image. Close the window when done.")
    fig, ax = plt.subplots()
    ax.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()
    fig.canvas.mpl_disconnect(cid)

    return np.array(points)

def plot_epipolar_geometry(im1, im2, points, lines):
    """
    Plot the points and their corresponding epipolar lines on two images.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Display images
    ax1.imshow(cv2.cvtColor(im1, cv2.COLOR_BGR2RGB))
    ax1.set_title("Image 1")
    ax2.imshow(cv2.cvtColor(im2, cv2.COLOR_BGR2RGB))
    ax2.set_title("Image 2")

    # Plot points on Image 1
    for i, point in enumerate(points):
        ax1.scatter(point[0], point[1], c=f'C{i}', label=f"Point {i+1}")
        ax1.annotate(f"{i+1}", (point[0], point[1]), color=f'C{i}')

    # Plot epipolar lines on Image 2
    for i, line in enumerate(lines):
        x = np.array([0, im2.shape[1]])  # Line endpoints
        y = - (line[0] * x + line[2]) / line[1]  # Solve for y = -(ax + c) / b
        ax2.plot(x, y, c=f'C{i}', label=f"Epipolar Line {i+1}")

    # Add legends and grid
    ax1.legend()
    ax1.grid(visible=True)
    ax2.legend()
    ax2.grid(visible=True)

    plt.tight_layout()
    plt.show()

# Main execution
if __name__ == "__main__":
    # Read images
    im1 = read_image('florence2.jpg')
    im2 = read_image('florence3.jpg')

    # Fundamental matrix
    F = np.array([[3.03994528999160e-08, 2.65672654114295e-07, -0.000870550254997210],
                  [4.67606901933558e-08, -1.11709498607089e-07, -0.00169128012255720],
                  [-1.38310618285550e-06, 0.00140690091935593, 0.999997201170569]])

    # Let the user select points on Image 1
    points = user_select_points(im1)
    print(f"Selected points: {points}")

    # Compute epipolar lines in Image 2
    lines = compute_epipolar_lines(F, points)

    # Plot epipolar geometry
    plot_epipolar_geometry(im1, im2, points, lines)
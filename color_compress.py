import tkinter as tk
from tkinter import filedialog, messagebox
from skimage import io
from sklearn.cluster import MiniBatchKMeans
import numpy as np

def select_image():
    """
    Opens a file dialog to select an image file.
    Returns the file path of the selected image.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(
        title="Select Image File",
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg")]
    )
    return file_path

def select_output_path():
    """
    Opens a file dialog to select the output path for the compressed image.
    Returns the file path where the compressed image will be saved.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    output_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")]
    )
    return output_path

def compress_image(image_path, n_clusters=16, batch_size=1000):
    """
    Compresses an image using MiniBatchKMeans clustering.
    :param image_path: Path to the input image.
    :param n_clusters: Number of colors to reduce the image to (default: 16).
    :param batch_size: Batch size for MiniBatchKMeans (default: 1000).
    :return: Compressed image as a NumPy array, or None if an error occurs.
    """
    try:
        # Reading the image
        print("Reading the image...")
        image = io.imread(image_path)
        rows, cols = image.shape[0], image.shape[1]
        image_flat = image.reshape(-1, 3)  # Flatten the image to (rows*cols, 3)

        # Modeling with MiniBatchKMeans for faster processing
        print("Compressing the image...")
        print("Note: This may take a while for large images.")
        kMeans = MiniBatchKMeans(n_clusters=n_clusters, batch_size=batch_size)
        kMeans.fit(image_flat)

        # Getting centers and labels
        centers = np.uint8(kMeans.cluster_centers_)
        labels = np.uint8(kMeans.labels_.reshape(rows, cols))

        # Reconstructing the image
        print("Reconstructing the image...")
        new_image = centers[labels]
        return new_image

    except Exception as e:
        print(f"Error during image compression: {e}")
        return None

def main():
    """
    Main function to run the image compression process.
    """
    print("Script started.")
    # Step 1: Select the input image
    print("Please select an image to compress.")
    filename = select_image()
    if not filename:
        print("No image selected. Exiting.")
        return
    print(f"Selected image: {filename}")

    # Step 2: Compress the image
    compressed_image = compress_image(filename, n_clusters=16)
    if compressed_image is None:
        print("Image compression failed. Exiting.")
        return

    # Step 3: Select the output path
    print("Please select where to save the compressed image.")
    output_path = select_output_path()
    if not output_path:
        print("No output path selected. Exiting.")
        return

    # Step 4: Save the compressed image
    try:
        print(f"Saving compressed image to: {output_path}")
        io.imsave(output_path, compressed_image)
        print("Image has been compressed and saved successfully!")
    except Exception as e:
        print(f"Error saving the compressed image: {e}")

if __name__ == "__main__":
    main()


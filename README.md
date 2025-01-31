echo "# Image Color Compression using K-Means

This Python script compresses an image by reducing the number of unique colors using MiniBatch K-Means clustering. The script provides a simple GUI for selecting input images and saving compressed outputs.

## Features

- Select an image file using a file dialog.
- Compress the image using K-Means clustering (default: 16 colors).
- Save the compressed image to a specified location.
- Efficient processing using \`MiniBatchKMeans\` for faster execution.

## Requirements

Ensure you have the following dependencies installed:

\`\`\`bash
pip install numpy scikit-image scikit-learn tkinter
\`\`\`

## Usage

1. Run the script:

   \`\`\`bash
   python color_compress.py
   \`\`\`

2. Select an image file when prompted.
3. The script compresses the image using K-Means clustering.
4. Choose a location to save the compressed image.

## Example

Before Compression:

![Original Image](https://via.placeholder.com/300)

After Compression (with 16 colors):

![Compressed Image](https://via.placeholder.com/300)

## How It Works

- The image is read and reshaped into a 2D array where each row is a pixel’s RGB value.
- The \`MiniBatchKMeans\` algorithm groups similar colors into clusters.
- The image is reconstructed using the cluster centroids, reducing the number of unique colors.
- The final image is saved in PNG format.

## Customization

You can modify the number of colors used in compression by changing:

\`\`\`python
compressed_image = compress_image(filename, n_clusters=16)
\`\`\`

Increasing \`n_clusters\` results in a more detailed image but less compression.

## License

This project is licensed under the MIT License.

" > README.md

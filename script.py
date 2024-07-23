from PIL import Image
import os

def convert_images_to_webp(input_folder, output_folder, max_size_kb=600):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through each file in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        
        # Check if the file is a JPEG image
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg') or filename.lower().endswith('.png'):
            # Open the image
            img = Image.open(input_path)

            # Set the quality to achieve the target size
            quality = 100  # Initial quality value
            while True:
                # Save the image to a temporary file with the specified quality
                img.thumbnail([4500, 4500], Image.Resampling.LANCZOS)
                #img.save(outfile, "JPEG")
                image_extension = os.path.splitext(filename)[1]
                temp_output_path = os.path.join(output_folder, filename.replace(image_extension, '.webp'))
                img.save(temp_output_path, 'WEBP', quality=quality)

                # Check the size of the temporary file
                temp_size_kb = os.path.getsize(temp_output_path) / 1024

                # If the size is within the limit, break the loop
                if temp_size_kb <= max_size_kb:
                    break

                # If not, reduce the quality and try again
                quality -= 5

                # Ensure the quality does not go below 0
                if quality < 0:
                    break

            # Move the final compressed image to the output folder
            final_output_path = os.path.join(output_folder, filename.replace(image_extension, '.webp'))
            print(filename)
            os.rename(temp_output_path, final_output_path)

if __name__ == "__main__":
    input_folder = "/Users/kunalsoni/Development/jpg-to-webp-converter/s2"
    output_folder = "/Users/kunalsoni/Development/jpg-to-webp-converter/d2"
    convert_images_to_webp(input_folder, output_folder)

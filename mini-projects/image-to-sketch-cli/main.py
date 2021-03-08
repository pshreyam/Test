import cv2 as cv
import click

@click.command()
@click.option("--image", prompt="Image", help="Name of the image to sketch.")
@click.option("--output", default="./sketch.jpg", help="Name of the output file.")
def main(image, output):    
    try:
        img = cv.imread(image)
        gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # Invert the image
        inverted_image = 255 - gray_image

        # Blur the image by Gaussian function
        blurred_image = cv.GaussianBlur(inverted_image, (21, 21), 0)

        # Invert the blurred image
        inverted_blurred_img = 255 - blurred_image

        # create the pencil sketch image
        pencil_sketch = cv.divide(gray_image, inverted_blurred_img, scale=256.0)
    except:
        click.secho("[Error] : Image could not be read or processed!", fg="red")
    else:
        try:
            cv.imwrite(output, pencil_sketch)
        except:
            click.secho("[Error] : File could not be written!", fg="red") 
        else:
            click.secho(f"File written to {output}.", fg="green")  
    
    click.secho("THANK YOU!", fg="green")
         
main()

from PIL import Image, ImageOps
import sys


if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    types = (".jpg", ".jpeg", ".png")
    input = sys.argv[1]
    output = sys.argv[2]

    if not input.endswith(types) or not output.endswith(types):
        sys.exit("Invalid file fromat")
    elif input.split(".")[1] != output.split(".")[1]:
        sys.exit("Input and output have different extensions")
    else:
        try:
            shirt = Image.open("shirt.png")
            with Image.open(input) as cropped:
                cropped = ImageOps.fit(cropped, shirt.size)
                cropped.paste(shirt, mask = shirt)
                cropped.save(output)
        except FileNotFoundError:
            sys.exit(f"Input does not exist")

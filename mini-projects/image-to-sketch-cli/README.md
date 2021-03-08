# Image-to-Sketch CLI

A basic cli script using opencv for generating sketch of an image!
(Uses click for CLI)

(And I know the documentation is longer than the actual code 🤣🤣🤣)

```bash
python3 -m venv venv
source ./venv/bin/activate

pip3 install -r requirements.txt
python3 main.py --image <image_path> --output <output_path>
```

For help:

```bash
python3 main.py --help
```

* You'll be prompted for <image_path> if not mentioned!
* Output file defaults to sketch.jpg!

![Demo](./demo.gif)

#### For Windows users:

You might have to install colorama for text colors.

```bash
pip3 install colorama
```

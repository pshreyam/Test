# Guess The Number

'Guess The Number' uses a model trained using the mnist dataset to predict numbers drawn by the users in the pygame screen.

The accuracy of the model is pretty low. It requires further training. This is for testing how the model is loaded in the script and how data is fed to the model.

## Requirements and dependencies

As of now, tensorflow is not released for python3.9, so python3.8 or lower is required.

```bash
python3.8 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt

python main.py
```
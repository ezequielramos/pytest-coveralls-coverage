from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    if 3 > 5:
        return "it will never get coverage by test"

    return ""


def add_absolute(value: int):

    if not isinstance(value, int):
        raise ValueError(f"value must be an int not a  {type(value).__name__}")

    if value < 0:
        value = value * -1
    return value + 1


def concat_string(value: str):
    if not isinstance(value, str):
        raise ValueError(f"value must be a str not a  {type(value).__name__}")

    return f"Hello {value}"

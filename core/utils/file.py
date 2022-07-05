import imp
from typing import TYPE_CHECKING
import uuid
from os.path import splitext

if TYPE_CHECKING:
    from core.models import Image


def generate_new_filename(filename: str) -> str:
    extension = splitext(filename)[1].lower()
    new_filename = str(uuid.uuid4()).replace("-", "") + extension

    return new_filename

def default_upload_directory(filename: str) -> str:
    generated_filename = generate_new_filename(filename)
    path = f'images/default/{generated_filename}'
    return path
    
def processed_upload_directory(filename: str) -> str:
    generated_filename = f'pr_{generate_new_filename(filename)}'
    path = f'images/processed/{generated_filename}'
    return path
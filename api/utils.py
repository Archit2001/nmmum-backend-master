from io import BytesIO
from django.core.files import File
from PIL import Image, ImageOps
import uuid

def resize_image(image, width=720, q=85):
    if image.width > width :
        img = Image.open(image)
        img = ImageOps.exif_transpose(img)
        img.convert('RGB')
        img.resize((720, int(((img.height / img.width) * img.height))))
        resized_io = BytesIO()
        img.save(resized_io, 'JPEG', quality=q)
        resized = File(resized_io, name=str(f"{uuid.uuid4()}.jpg"))
        return resized
    
    return image
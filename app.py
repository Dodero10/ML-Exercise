import torch
from PIL import Image
from RealESRGAN import RealESRGAN
import gradio as gr

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model2 = RealESRGAN(device, scale=2)
model2.load_weights('weights/RealESRGAN_x2.pth', download=True)
model4 = RealESRGAN(device, scale=4)
model4.load_weights('weights/RealESRGAN_x4.pth', download=True)
model8 = RealESRGAN(device, scale=8)
model8.load_weights('weights/RealESRGAN_x8.pth', download=True)


def inference(image, size):
    if size == '2x':
        result = model2.predict(image.convert('RGB'))
    elif size == '4x':
        result = model4.predict(image.convert('RGB'))
    else:
        result = model8.predict(image.convert('RGB'))
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    print(f"Image size: {size} ... OK")
    return result


title = "Cải thiện hình ảnh"

gr.Interface(inference,
             [gr.Image(type="pil"),
              gr.Radio(['2x', '4x', '8x'],
                       type="value",
                       value='2x',
                       label='Resolution model')],
             gr.Image(type="pil", label="Output"),
             title=title,
             allow_flagging='never',
             cache_examples=False,
             ).queue().launch(show_error=True)

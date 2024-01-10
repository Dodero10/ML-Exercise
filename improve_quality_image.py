import torch
from PIL import Image
from RealESRGAN import RealESRGAN

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model2 = RealESRGAN(device, scale=2)
model2.load_weights('weights/RealESRGAN_x2.pth', download=True)

for i in range(1, 26):
    image = Image.open(f'input/image_' + str(i) + '.png')
    result = model2.predict(image.convert('RGB'))
    result.save(f'output/{i}.png')
    print(f"Image {i} ... OK")
    if torch.cuda.is_available():
        torch.cuda.empty_cache()

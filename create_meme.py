from PIL import Image, ImageFont, ImageDraw

class CreateMeme(object):
    large_font = ImageFont.truetype("TCCEB.TTF", 70)
    small_font = ImageFont.truetype("TCCEB.TTF", 50)
    
    watermark =  ImageFont.truetype("TCCEB.TTF", 20)
    author = '@Nhom 3'
    author_length = watermark.getsize(author)[0]
    
    def __init__(self):
        pass
        
    @classmethod
    def createbyCol(cls, image_name, top_text, bottom_text):
        image = Image.open('./meme/' + image_name).convert('RGB')
        draw = ImageDraw.Draw(image)

        top_length = cls.large_font.getsize(top_text)[0]
        bottom_length = cls.large_font.getsize(bottom_text)[0]

        top_width = image.width // 2 - top_length // 2
        bottom_width = image.width // 2 - bottom_length // 2

        draw.text((top_width, 0), top_text, (255,255,255), font = cls.large_font)
        draw.text((bottom_width, image.height - 90), bottom_text, (255,255,255), font = cls.large_font)
        draw.text((image.width - cls.author_length - 20, image.height - 25), cls.author, (255,157,157), font = cls.watermark)
        image.save('result.jpg')
        
        
    @classmethod
    def createbyRow(cls, image_name, top_text, bottom_text):
        top_text = top_text.replace(" ", "\n")
        bottom_text = bottom_text.replace(" ", "\n")
        
        image = Image.open('./meme/' + image_name).convert('RGB')
        draw = ImageDraw.Draw(image)

        top_length = cls.small_font.getsize(top_text.split('\n')[0])[0]
        bottom_length = cls.small_font.getsize(bottom_text.split('\n')[0])[0]

        top_width = image.width // 8 - top_length // 2
        bottom_width = image.width // 3 - bottom_length // 2

        draw.text((top_width, 20), top_text, (0,0,0), font = cls.small_font)
        draw.text((bottom_width, 10), bottom_text, (0,0,0), font = cls.small_font)
        draw.text((image.width - cls.author_length - 20, image.height - 25), cls.author, (255,157,157), font = cls.watermark)
        image.save('result.jpg')
                
if __name__ == '__main__':
    CreateMeme.create("10GUY.jpg", "hello", "how are you")
        
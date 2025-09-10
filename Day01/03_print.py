from deep_translator import GoogleTranslator
# deep_translator 중에서 콕 찝어서 GoogleTranslator을 사용하겠다.

input_text = input("번역할 한글을 입력하세요 : ")

# Translate by using Google Traslator
translated = GoogleTranslator(source='ko', target='en').translate(input_text)

print()
print(f"입력한 한글 : {input_text}")
print(f"번역된 영어 : {translated}")

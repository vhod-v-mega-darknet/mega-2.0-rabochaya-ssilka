# depalindrome.py
text = input("Введите слово: ").lower()
if text == text[::-1]:
    print("✅ Это палиндром!")
else:
    print("❌ Не палиндром.")

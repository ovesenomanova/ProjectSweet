text= "смешные чебуреки чебуреки"
text_list = text.split(" ")
count=0
user_word = input("Введите слово: ")
for world in text_list:
    if user_word  == world:
        count += 1

print(f"количество слов: {count}")



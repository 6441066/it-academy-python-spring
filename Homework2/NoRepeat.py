# 4. Вводится строка. Требуется удалить из нее повторяющиеся символы
# и все пробелы. Например, если было введено "abc cde def",
# то должно быть выведено "abcdef".
# -----------------------------------------------------------------------------
sentence = input("Введите строку:")
new_str = ""
for char in sentence:
    if char != ' ' and char not in new_str:
        new_str += char

print(new_str)

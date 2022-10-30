def get_count_char(str_):
    str_ = str_.lower()
    my_dict = {}
    for sign_ in str_:
        if sign_.isalpha():
            if sign_ in my_dict:
                my_dict[sign_] += 1
            else:
                my_dict[sign_] = 1
    return my_dict



main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

def second_function(dict_symbol):
    overall_meaning = sum(dict_.values())
    second_dict = {}
    for meaning in dict_.values():
        meaning = round(meaning / overall_meaning * 100, 1)
        return second_dict
    print(second_function(get_count_char(main_str)))
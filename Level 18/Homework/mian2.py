# 15) საშუალო არითმეტიკული (ნებისმიერი ზომის სიისთვის)
def Arithmetic_mean(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    return total / count


# 16) სტრინგიდან მხოლოდ ხმოვანი ასოების დატოვება
def filter_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char in vowels:
            result += char
    return result


# 17) უნიკალური ელემენტების სია (duplicates გარეშე)
def unique_list(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list


# 18) Manual sum — სიის ელემენტების ჯამი საკუთარი ხელით
def manual_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total
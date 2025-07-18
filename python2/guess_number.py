numbers = []
i = 0
print("برای پایان وارد کردن، '=' را وارد کنید.")

while True:
    user_input = input("یک عدد وارد کنید: ")
    if user_input == "=":
        break

    try:
        number = int(user_input)
        # لیست را با افزودن عنصر جدید گسترش می‌دهیم
        numbers =numbers + [0] # اضافه کردن فضای خالی (مثل append دستی)
        numbers[i] = number  # مقداردهی دستی با اندیس
        i += 1 # افزایش اندیس برای مقدار بعدی

    except ValueError:
        print("لطفاً فقط عدد وارد کنید.")

print("مقادیر وارد شده:")
print(numbers)numbers = []
i = 0
print("برای پایان وارد کردن، '=' را وارد کنید.")

while True:
    user_input = input("یک عدد وارد کنید: ")
    if user_input == "=":
        break

    try:
        number = int(user_input)
        # لیست را با افزودن عنصر جدید گسترش می‌دهیم
        numbers =numbers + [0] # اضافه کردن فضای خالی (مثل append دستی)
        numbers[i] = number  # مقداردهی دستی با اندیس
        i += 1 # افزایش اندیس برای مقدار بعدی

    except ValueError:
        print("لطفاً فقط عدد وارد کنید.")

print("مقادیر وارد شده:")
print(numbers)

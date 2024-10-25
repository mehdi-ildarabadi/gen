import openai
import json
from datetime import datetime

# کلید API خود را اینجا وارد کنید
openai.api_key = 'YOUR_API_KEY'


def chat_with_openai(user_message):
    # درخواست به API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # مدل مورد نظر
        messages=[
            {"role": "user", "content": user_message}  # پیام کاربر
        ]
    )

    # تبدیل پاسخ به فرمت JSON
    response_json = response.to_dict()  # تبدیل پاسخ به دیکشنری

    # ثبت پاسخ در فایل لاگ
    with open("response_log.json", "a") as log_file:
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "response": response_json
        }
        json.dump(log_entry, log_file, ensure_ascii=False, indent=4)
        log_file.write("\n\n")  # جداکننده بین لاگ‌های مختلف

    # بازگشت محتوای پیام
    return response['choices'][0]['message']['content']


# مثال از استفاده
if __name__ == "__main__":
    user_input = input("شما: ")
    response = chat_with_openai(user_input)
    print("OpenAI:", response)

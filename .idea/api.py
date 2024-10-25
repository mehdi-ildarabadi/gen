import openai

# کلید API خود را اینجا وارد کنید
openai.api_key = 'YOUR_API_KEY'

# تنظیم آدرس پایه API
openai.api_base = 'https://YOUR_CUSTOM_API_URL/v1'  # آدرس سفارشی شما

def chat_with_openai(user_message):
    # ارسال درخواست به API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # مدل مورد نظر
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}  # پیام کاربر
        ]
    )
    # دریافت و بازگشت پیام OpenAI
    return response['choices'][0]['message']['content']

# مثال از استفاده
if __name__ == "__main__":
    user_input = input("شما: ")
    response = chat_with_openai(user_input)
    print("OpenAI:", response)

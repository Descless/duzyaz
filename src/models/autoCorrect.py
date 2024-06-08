import openai

# OpenAI API anahtarınızı burada belirtin
openai.api_key = '#'

def turkish_autocorrect_tool(text):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Sen yardımcı bir asistansın ve metinlerdeki dil bilgisi ve yazım hatalarını düzeltiyorsun."},
            {"role": "user", "content": f"Lütfen aşağıdaki metindeki dil bilgisi ve yazım hatalarını düzelt: {text}"}
        ],
        max_tokens=1000,
        temperature=0.7,
    )
    return response['choices'][0]['message']['content'].strip()

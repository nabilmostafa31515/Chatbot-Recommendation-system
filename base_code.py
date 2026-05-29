import os
from google import genai
from google.genai import types
from google.genai.errors import APIError

client = None
MODEL_NAME = 'gemini-2.5-flash'

try:
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY غير موجود في البيئة")
    client = genai.Client(api_key=api_key)
except Exception as e:
    print(f"❌ خطأ في تهيئة Gemini API: {e}")
    client = None

def call_gemini_api(prompt, temperature=0.5):
    if client is None:
        return "❌ لا يمكن الاتصال بالنموذج."
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config=types.GenerateContentConfig(temperature=temperature)
        )
        return response.text
    except APIError as e:
        return f"❌ خطأ في API: {e}"
    except Exception as e:
        return f"❌ خطأ غير متوقع: {e}"


knowledge_base = {
    "أبو الهول": {
        "الموقع": "الجيزة، مصر",
        "الوصف": "تمثال ضخم بجسم أسد ورأس إنسان، عمره أكثر من 4500 سنة",
        "أوقات الزيارة": "8 صباحاً - 5 مساءً",
        "سعر الدخول": "160 جنيه للمصريين، 450 للأجانب",
    },
    "قلعة قايتباي": {
        "الموقع": "الإسكندرية، مصر",
        "الوصف": "قلعة تاريخية بنيت في القرن الـ15 على أنقاض منارة الإسكندرية",
        "أوقات الزيارة": "9 صباحاً - 4 مساءً",
    }
}

def normalize(text):
    """توحيد الهمزات للبحث"""
    return text.replace("أ","ا").replace("إ","ا").replace("آ","ا").lower()

def retrieve_information(query):
    query_n = normalize(query)
    for name, details in knowledge_base.items():
        if normalize(name) in query_n:
            retrieved_text = f"المعلم: {name}\n"
            for key, value in details.items():
                retrieved_text += f"- {key}: {value}\n"
            return retrieved_text
    return None

def chatbot_response_generator(user_query):
 
    context = retrieve_information(user_query)
  
    if context:
        prompt_instruction = "أنت مرشد سياحي خبير..."
        full_prompt = f"{prompt_instruction}\n\n[المعلومات السياحية]:\n{context}\n\n[سؤال الزائر]:\n{user_query}"
        return call_gemini_api(full_prompt, temperature=0.3) 
    else:
        prompt_instruction = "أنت مرشد سياحي..."
        full_prompt = f"{prompt_instruction}\n\n[سؤال الزائر]:\n{user_query}"
        return call_gemini_api(full_prompt, temperature=0.5)

def generate_tour_plan_and_suggestions(location, duration_days, interests):
 
    plan_prompt = (
        f"أنت خبير في التخطيط السياحي والتسويق. مهمتك هي إنشاء خطة سياحية مفصلة لـ {location} "
        f"لمدة {duration_days} أيام. يجب أن تشمل الخطة الأماكن بناءً على اهتمامات المستخدم في {interests}. "
        "قم بتنظيمها في جدول زمني يومي واضح (مثل جدول Markdown). "
        # ...
    )
    return call_gemini_api(plan_prompt, temperature=0.7)
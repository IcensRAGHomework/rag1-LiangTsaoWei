import json
import requests
from model_configurations import get_model_configuration
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
import traceback

gpt_chat_version = 'gpt-4o'
gpt_config = get_model_configuration(gpt_chat_version)

llm = AzureChatOpenAI(
            model=gpt_config['model_name'],
            deployment_name=gpt_config['deployment_name'],
            openai_api_key=gpt_config['api_key'],
            openai_api_version=gpt_config['api_version'],
            azure_endpoint=gpt_config['api_base'],
            temperature=gpt_config['temperature']
)

def get_calendarific_holidays(api_key, country, year, month):
    url = f"https://calendarific.com/api/v2/holidays?api_key={api_key}&country={country}&year={year}&month={month}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def generate_hw01(question):
    
    messages = [
        SystemMessage(content="""以Json格式回答紀念日的日期，並確保輸出格式為:
            {
                "Result": [
                    {
                        "date": "xxxx-xx-xx",
                        "name": "holiday name"
                    }
                ]
            }
            請給我純文字就好，不要有```json"""
        ),
        HumanMessage(content=question)
    ]
    response = llm.invoke(messages)
    
    return response.content
    
def generate_hw02(question):
    try:
        # 設置 Calendarific API 參數
        api_key = "DhFzedhXc0sOIh4sdmWHaKsyl1yzFBe5"  # 替換為您的 API 金鑰
        country = "TW"
        year = 2024
        month = 10

        # 調用 Calendarific API 獲取紀念日資料
        holidays_data = get_calendarific_holidays(api_key, country, year, month)
        if holidays_data and "response" in holidays_data and "holidays" in holidays_data["response"]:
            holidays = holidays_data["response"]["holidays"]
            formatted_data = []
            for holiday in holidays:
                date = holiday["date"]["iso"]
                name = holiday["name"]
                translated_name = translate_text(name)
                formatted_data.append({"date": date, "name": translated_name})
            result = {"Result": formatted_data}
            return json.dumps(result, ensure_ascii=False, indent=2)
        else:
            return "No holidays found"

    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()
        return None
    
def generate_hw03(question2, question3):
    pass
    
def generate_hw04(question):
    pass
    
def demo(question):
    llm = AzureChatOpenAI(
            model=gpt_config['model_name'],
            deployment_name=gpt_config['deployment_name'],
            openai_api_key=gpt_config['api_key'],
            openai_api_version=gpt_config['api_version'],
            azure_endpoint=gpt_config['api_base'],
            temperature=gpt_config['temperature']
    )
    message = HumanMessage(
            content=[
                {"type": "text", "text": question},
            ]
    )
    response = llm.invoke([message])
    
    return response

import os
from openai import OpenAI
import os
from prompt import sentiment_analyse_prompt,summarization_prompt,keyword_extraction_prompt,translate_prompt




def call_deepseek(tempreture,prompt):
	api_key = os.getenv("DeepseekAPI")
	if not api_key:
		raise ValueError("请设置环境变量 DeepseekAPI")

	client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
	response = client.chat.completions.create(
		model="deepseek-chat",
		messages=[
			{"role": "system", "content": "你是一个有用的助手"},
			{"role": "user", "content": prompt},
		],
		stream=False,
		max_tokens=1000
	)
	context=response.choices[0].message.content
	return context

def sentiment_analyse(text):
	prompt=sentiment_analyse_prompt(text)
	result=call_deepseek(0.2,prompt)
	return result

def summarization(text):
	prompt=summarization_prompt(text)
	result=call_deepseek(0.2,prompt)
	return result

def keyword_extraction(text):
	prompt=keyword_extraction_prompt(text)
	result=call_deepseek(0.2,prompt)
	return result

def translate(text):
	prompt=translate_prompt(text)
	result=call_deepseek(0.2,prompt)
	return result
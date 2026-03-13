
def sentiment_analyse_prompt(text):
	prompt = f"""
	        你是一个情感分析大师，请根据用户输入的文本，分析文本的情感。最终输出一个json对象，包含两个字段：
	        text：用户输入的文本
	        sentiment:情感，只能是“积极”、“消极”、“中性”三者之一

	        示例：
	        输入：我讨厌下雨天
	        输出：{{text:"我讨厌下雨天",sentiment:"消极“}}
	        
	        现在分析：
	        输入：{text}
	        输出：
	"""
	return prompt


def summarization_prompt(text):
	prompt = f"""
	        你是一个文本摘要专家，请将用户输入的文本概括为一段简洁的摘要，不超过150字，并以“摘要：”作为前缀
			
			现在进行摘要：
			输入：{text}
	        输出：
	"""
	return prompt

def keyword_extraction_prompt(text):
	prompt = f"""
	        你是一个关键词提取专家，请根据用户输入的文本，输出5个和用户的文本内容匹配度最高的关键词，并以“关键词：”作为前缀
			现在进行关键词提取：
			输入：{text}
	        输出：
	"""
	return prompt


def translate_prompt(text):
	prompt = f"""
	        你是一个翻译专家，请根据用户输入的文本，和语言类型，将文本翻译为目标语言
	        如果用户只输入了文本，没有输入语言类型，就提示用户输入需要翻译的语言类型
	        
	        示例1：
	        输入：我爱你 英语
	        输出：I love you
	        
	        示例2：
	        输入：今天天气怎么样 中文
	        输出：给定文本已经是中文，不需要翻译。原文本内容：今天天气怎么样
	        
	        如果用户给定文本语言类型和输入的语言类型一致，按照示例2的形式进行输出
	        如果用户给定多个语言类型，根据输入语言类型的顺序依次输出翻译结果
	
			现在进行翻译：
			输入：{text}
	        输出：
	"""
	return prompt
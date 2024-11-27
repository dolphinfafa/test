import re
import json

srt_file = 'diss.srt'
json_file = 'diss.json'

def srt_to_json(srt_file):
    with open(srt_file, 'r', encoding='utf-8') as file:
        srt_data = file.read()

    # 使用正则表达式匹配SRT文件中的时间和字幕文本
    pattern = r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n(.+?)\n\n'
    matches = re.findall(pattern, srt_data, re.DOTALL)

    # 将匹配到的数据转换为JSON格式
    subtitles = []
    for match in matches:
        subtitle = {
            'index': int(match[0]),
            'start_time': match[1],
            'end_time': match[2],
            'text': match[3]
        }
        subtitles.append(subtitle)

    json_data = json.dumps(subtitles, ensure_ascii=False)

    return json_data

# 调用函数将SRT转换为JSON
json_data = srt_to_json(srt_file)

# json_data里的'text'字段分成两个字段
# 如果'text'字段的内容是'名字 内容'的形式
# 最后一个空格前的内容存入'name'字段
# 最后一个空格后的内容存入'content'字段
# 如果'text'字段的内容不是'名字 内容'的形式
# 则删除这条记录
# def split_text(json_data):
#     subtitles = json.loads(json_data)
#     for subtitle in subtitles:
#         text = subtitle['text']
#         if ' ' in text:
#             name, content = text.rsplit(' ', 1)
#             subtitle['name'] = name
#             subtitle['content'] = content
#         else:
#             subtitles.remove(subtitle)
#     return json.dumps(subtitles, ensure_ascii=False)

# json_data = split_text(json_data)

# 将转换后的JSON数据写入文件
with open(json_file, 'w', encoding='utf-8') as file:
    file.write(json_data)

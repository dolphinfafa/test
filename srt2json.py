import re
import json

def srt_to_json(srt_file, json_file):
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

#   json_data里的'text'字段分成两个字段
#   如果'text'字段的内容是'名字 内容'的形式
#   最后一个空格前的内容存入'name'字段
#   最后一个空格后的内容存入'content'字段
#   如果'text'字段的内容不是'名字 内容'的形式
#   则删除这条记录
    subtitles = json.loads(json_data)
    for subtitle in subtitles:
        text = subtitle['text']
        if ' ' in text:
            name, content = text.rsplit(' ', 1)
            subtitle['name'] = name
            subtitle['content'] = content
        else:
            subtitles.remove(subtitle)

    json_data = json.dumps(subtitles, ensure_ascii=False)

    # 将JSON数据写入文件
    with open(json_file, 'w', encoding='utf-8') as file:
        file.write(json_data)

if __name__ == '__main__':
    # 连续调用srt_to_json函数，
    srts = [
        '5-1.srt', 
        '5-2.srt', 
        ]
    for i, srt in enumerate(srts):
        # json文件名为srt[i].json
        json_file = srt.split('.')[0] + '.json'
        srt_to_json(srt, json_file)
        print('Convert {} to {}'.format(srt, json_file))
# -*- coding: utf-8 -*-
# Author：大米拉 2022年08月
# 功能：聊天机器人算法\
# pip install chatterbot -i https://pypi.tuna.tsinghua.edu.cn/simple

import chatAI
from chatterbot.trainers import ListTrainer
# 创建
chatbot = chatAI.chatbot

# 训练
# 这是训练对话
conversation = [
'人闲桂花落',
'夜静春山空',
'月出惊山鸟',
'时鸣春涧中',
'独坐幽篁里',
'弹琴复长啸',
'深林人不知',
'明月来相照',
'空山不见人',
'但闻人语响',
'返景入深林',
'复照青苔上',
'山中相送罢',
'日暮掩柴扉',
'春草明年绿',
'王孙归不归',
'中岁颇好道',
'晚家南山陲',
'兴来每独往',
'胜事空自知',
'行到水穷处',
'坐看云起时',
'偶然值林叟',
'谈笑无还期',
'荆溪白石出',
'天寒红叶稀',
'山路元无雨',
'空翠湿人衣',
'木末芙蓉花',
'山中发红萼',
'涧户寂无人',
'纷纷开且落',
'君自故乡来',
'应知故乡事',
'来日绮窗前',
'寒梅著花未',
'楚塞三湘接',
'荆门九派通',
'江流天地外',
'山色有无中',
'郡邑浮前浦',
'波澜动远空',
'襄阳好风日',
'留醉与山翁',
'下马饮君酒',
'问君何所之',
'君言不得意',
'归卧南山陲',
'但去莫复问',
'白云无尽时',
'秋山敛余照',
'飞鸟逐前侣',
'彩翠时分明',
'夕岚无处所'
]
trainer = ListTrainer(chatbot)
trainer.train(conversation)

# 对话
response = chatbot.get_response('Good Morning!')
print(response)


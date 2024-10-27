#!/usr/bin/env python3
import cgi
from g4f.client import Client
f1 = open("/home/mi/AI-v1/rasp/celander.txt")
s1 = f1.readlines()
f2 = open("/home/mi/AI-v1/pater.txt")
s2 = f2.readlines()
z = "<meta charset=\"UTF-8\" />"
client = Client()
def task(x):
	response = client.chat.completions.create(
   	 model="gpt-4",
   	 messages=[{"role": "user", "content": f"{k}"}],
	)
	return response.choices[0].message.content
k = f"Напиши расписание строго в формате html кода чтобы внести своё распиание на сайт по этому шаблону(-ам) {s2}, обязвтельно в начале добавь {z} отвечай мне строго в формате без отклонений: время(с до), место(адрес), занятие(название). Отвечай всегда на русском, так же отвечай чётко не добовляя лишних слов, выдай ответ в формате таблицы это важно. Итак составь мне расписание по заданной формуле, без отклонений для моего дня: {s1} ,но так же мне надо найти время на подготовку к коллоквиуму не менее n времени в этот же день сам предложи оптимальное по твоему выбору время и место в котором я смогу готовится к этому экзамену"
taskl = []
n=1
for x in range(n):
	taskx= task(k)
	taskl.append(taskx)
	print(x)
k = f"выбери текс лучшего по твоему мнению расписания из этих {n} расписаний и выведи его в точности  без соих добавлений, вот все расписания {taskl}, Обязательно добавь в начале и в конце выбраного собой кода комбинацию символов \"```\" "
try:
	taskfin = task(k).split("```")[1]
except:
	taskfin = task(k).split("```")[0]
print(taskfin)
r = open("/home/mi/AI-v1/calendar/index.html",'w')
r.write(taskfin)
r.close()

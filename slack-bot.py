#!/usr/local/bin/python
# -*- coding: utf-8 -*-

#setting with /etc/crontab

#include
from slacker import Slacker
import time

#channel
general=#string type channel id

#auth
token=#'xoxb-token id'
slack=Slacker(token)

#make 'Day of the week'
n = time.localtime().tm_wday
day_of_the_week = ['월','화',' 수','목','금','토','일']
append_str = '요일'
day_of_the_week_comment = ['한주의 기분좋은 시작!!','좋은 화요일 아침 입니다!!',' 수~울술 풀릴 것 같은 좋은 수요일!!','목요일 힘냅시다!!','좋은 금요일 입니다!!','토','일']

#make msg
attachments_dict = dict()
attachments_dict['pretext'] = str(day_of_the_week_comment[n])
attachments_dict['title'] = "타이틀입니다.!!"
attachments_dict['title_link'] = "https://www.naver.com"#링크
attachments_dict['fallback'] = "좋은아침!! "+day_of_the_week[n]+append_str+" FALLBACK 입니다!!"
attachments_dict['text'] = "위 링크를 누르시면 연결됩니다!!"
attachments_dict['mrkdwn_in'] = ["text", "pretext"]  # 마크다운을 적용시킬 인자들을 선택합니다.
attachments = [attachments_dict]

#send msg
slack.chat.post_message(general, text=None, attachments=attachments, as_user=True)
#text는 제일 첫글

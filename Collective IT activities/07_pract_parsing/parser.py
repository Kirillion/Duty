from bs4 import BeautifulSoup as bs
import codecs

# открываем документ
doc = bs(codecs.open('article.htm', encoding='utf-8', mode='r').read(), 'html.parser')

# извлечение данных из статьи
author = doc.select('.author-info__name')[0].decode_contents().strip()
title = doc.select('.post__title span')[1].decode_contents().strip()
date = doc.select('.post__time_published')[0].decode_contents().strip()
tags = list(map(lambda x: x.decode_contents().strip(), doc.select('div.post__tags ul li a')))
rating = int(doc.select('div.post-additionals span.voting-wjt__counter-score.js-score')[0].decode_contents().strip())

# вывод на экран
print('Автор:', author)
print('Заголовок:', title)
print('Дата:', date)
print('Теги:', tags)
print('Рейтинг:', rating)

# извлечение данных о комментариях
comments = []
for node in doc.select('div.comment_body'):
    text = node.select('div.message')[0].decode_contents().strip()
    rating = int(node.select('span.voting-wjt__counter-score.js-score')[0].decode_contents().strip())
    author = node.select('a.comment-item__username')[0].decode_contents().strip()
    comments.append({'text': text, 'rating': rating, 'author': author})

# вывод информации по комментариям
print('Комментариев в статье: ', len(comments))
print('Самый маленький комментарий:', sorted(comments, key=lambda x: len(x['text']))[0]['text'])
most_popular = sorted(comments, key=lambda x: x['rating'], reverse=True)[0]
print('Самый популярный комментарий:', most_popular['text'], 'Рейтинг ', most_popular['rating'])

# самый активный комментатор
commentators = {}
for comment in comments:
    if comment['author'] in commentators:
        commentators[comment['author']] += 1
    else:
        commentators[comment['author']] = 1
most_active = max(commentators, key=commentators.get)
print('Самый активный:', most_active, ', комментариев:', commentators[most_active])

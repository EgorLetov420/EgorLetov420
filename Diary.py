diary = {'понедельник': {
                          'утро': ['погулять с собакой'],
                          'день': [],
                          'вечер': ['погулять с собакой']
                                      },
        'вторник': {
                          'утро': ['погулять с собакой'],
                          'день': [],
                          'вечер': ['погулять с собакой']
                                      },
        'среда': {
                          'утро': ['погулять с собакой'],
                          'день': [],
                          'вечер': ['погулять с собакой']
                                      },
        'четверг': {
                          'утро': ['погулять с собакой'],
                          'день': [],
                          'вечер': ['погулять с собакой']
                                      },
        'пятница': {
                          'утро': ['заехать в шиномонтаж', 'помыть машину'],
                          'день': [],
                          'вечер': ['поход в театр',  'ужин в кафе']
                                      },
        'суббота': {
                          'утро': [],
                          'день': [],
                          'вечер': []
                                      },
        'воскресенье': {
                          'утро': [],
                          'день': [],
                          'вечер': []
                                      }}
diary.pop('суббота')
diary.pop('воскресенье')
new_key = 'суббота', 'воскресенье'
new_deal = 'посадить цветы на даче'
diary[new_key] = new_deal
print(diary)



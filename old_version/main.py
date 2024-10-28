import requests

FILE_URL = 'https://raw.githubusercontent.com/danakt/russian-words/master/russian.txt'


def get_dictionary() -> None:
    """
    Скачивает наиболее полный (1 532 629 слова) словарь русских слов
    в файл dictionary.txt в папку скрипта.
    """
    response = requests.get(FILE_URL)
    text = response.content.decode('cp1251')

    with open('dictionary.txt', 'wb') as file:
        file.write(text.encode('utf-8'))


def get_line_count(file_path: str) -> int:
    # TODO: docstring
    with open(file_path, 'r', encoding='utf-8') as file:
        for count, line in enumerate(file):
            pass
        return count + 1


def get_words_with_length(file_path: str, word_length: int) -> None:
    # TODO: docstring
    # TODO: при генерации имени учесть аргумент file_path
    file_name = str(word_length) + '-character dictionary.txt'
    with open(file_path, 'r', encoding='utf-8') as file, open(file_name, 'w', encoding='utf-8') as file_new:
        for line in file:
            if len(line) == word_length + 1:
                file_new.write(line)


def get_words_with_symbol(file_path: str, symbol: str) -> None:
    # TODO: docstring
    # TODO: при генерации имени учесть аргумент file_path
    file_name = symbol + '-dictionary.txt'
    with open(file_path, 'r', encoding='utf-8') as file, open(file_name, 'w', encoding='utf-8') as file_new:
        for line in file:
            if symbol in line.lower():
                file_new.write(line)


def get_words_without_symbol(file_path: str, prefix: str, symbol: str) -> None:
    # TODO: docstring
    # TODO: при генерации имени учесть аргумент file_path
    file_name = prefix + '-dictionary.txt'
    with open(file_path, 'r', encoding='utf-8') as file, open(file_name, 'w', encoding='utf-8') as file_new:
        for line in file:
            if symbol not in line.lower():
                file_new.write(line)


def get_words_with_symbol_on_position(file_path: str, prefix: str, symbol: str, position: int) -> None:
    # TODO: docstring
    # TODO: при генерации имени учесть аргумент file_path
    file_name = prefix + '-dictionary.txt'
    with open(file_path, 'r', encoding='utf-8') as file, open(file_name, 'w', encoding='utf-8') as file_new:
        for line in file:
            if symbol == line.lower()[position]:
                file_new.write(line)


def get_words_without_symbol_on_position(file_path: str, prefix: str, symbol: str, position: int) -> None:
    # TODO: docstring
    # TODO: при генерации имени учесть аргумент file_path
    file_name = prefix + '-dictionary.txt'
    with open(file_path, 'r', encoding='utf-8') as file, open(file_name, 'w', encoding='utf-8') as file_new:
        for line in file:
            if symbol != line.lower()[position]:
                file_new.write(line)


def get_words_with_symbol_with_count(file_path: str, prefix: str, symbol: str, count: int) -> None:
    # TODO: docstring
    # TODO: при генерации имени учесть аргумент file_path
    # TODO: учесть позицию уже определенной буквы
    file_name = prefix + '-dictionary.txt'
    with open(file_path, 'r', encoding='utf-8') as file, open(file_name, 'w', encoding='utf-8') as file_new:
        for line in file:
            check = 0
            for ch in line:
                if ch == symbol:
                    check += 1
            if check == count:
                file_new.write(line)


# TODO: проверка на пустой файл
if __name__ == '__main__':
    # https://wotpack.ru/slova-iz-5-bukv-tinkoff-answer-today/
    # {'28.04': 'слово',
    #  '29.04': 'номер - аванс - башня - глина - длина',
    #  '30.04': 'адрес - рынок - бугор - хутор',
    #  '01.05': 'башня - валет - лампа - лассо',
    #  '02.05': 'рынок - покой - капот - купол',
    #  '03.05': 'глина - бочка - ботва',
    #  '04.05': 'капот - акция - вклад - скала',
    #  '05.05': 'бугор - адепт - вилка - малыш - шалаш',
    #  '06.05': 'малыш - автор - биржа - греча - дудка - пудра',
    #  '07.05': 'вклад - аврал',
    #  '08.05': 'бочка - венок - купон - склон',
    #  '09.05': 'акция - гудок - венок - бычок - лоток - порок',
    #  '10.05': 'венок - акция - будка - мышка - ласка - тачка - (чайка)',
    #  '11.05': 'будка - верфь - живот - ствол',
    #  '12.05': 'живот - буква',
    #  '13.05': 'вилка - агент - батон - табун',
    #  '14.05': 'агент - барин - закон - фазан',
    #  '15.05': 'барин - ангел - нужда - сосна',
    #  '16.05': 'ангел - бочка - выдра - трава',
    #  '17.05': 'батон - ведро - серсо - жерло',
    #  '18.05': 'ведро - судно',
    #  '19.05': 'вилка - догма - обуза - особа',
    #  '20.05': 'догма - билет - принц - шприц',
    #  '21.05': 'билет - плита - стиль',
    #  '22.05': 'батон - глист - треск',
    #  '23.05': 'вклад - бетон - степь - сюжет',
    #  '24.05': 'вклад - глист - тепло - отель',
    #  '25.05': 'тепло - напор',
    #  '26.05': 'бетон - глист - страх - паста - каста',
    #  '27.05': 'догма - земля - смерч'.
    #  '28.05': 'напор - акциз - вклад - скала - шкала',
    #  '29.05': 'капот - бисер - делец',
    #  '30.05': 'венок - каноэ - канон',
    #  '31.05': 'плита - весло - дрель - шмель',
    #  '01.06': 'страх - барин - горка - пурга',
    #  '02.06': 'вилка - школа - акула - скула',
    #  '03.06': 'пурга - бонус - обувь',
    #  '04.06': 'школа - валик - балык - тальк',
    #  '05.06': 'табун - броня - бренд',
    #  '06.06': 'валик - ведро - ветвь - венец',
    #  '07.06': 'мышка - бетон - добро - обруч',
    #  '08.06': 'ведро - харчо - русло - просо',
    #  '09.06': 'барин - автор - крыса - крыша',
    #  '10.06': 'скула - амеба - война - гроза - ягода',
    #  '11.06': 'автор - гроза - кобра - норма',
    #  '12.06': 'вклад - ангел - блоха - смола',
    #  '13.06': 'кобра - весло - выход - вывод'}
    # Розыгрыш призов: 13.06 в 14.00. Ссылка: https://www.youtube.com/watch?v=nURRQ7tfx6I
    # Мои билеты: 1988893 - 1988901
    # (1988893, 1988894, 1988895, 1988896, 1988897, 1988898, 1988899, 1988900, 1988901)

    # {'14.06': 'автор - бегун - земля - кешью - дефис - песец',
    #  '15.06': 'кобра - зерно - отряд - пирог - спрос',
    #  '16.06': 'пирог - броня - кровь - дрожь',
    #  '17.06': 'бренд - автор - карма - рифма',
    #  '18.06': 'барин - бисер',
    #  '19.06': 'автор - кофта - стадо - танго - табло',
    #  '20.06': 'ангел - валик - блоха - блуза',
    #  '21.06': 'склон - апорт - опора',
    #  '22.06': 'блоха - ведро - створ - рывок',
    #  '23.06': 'валик - бонус - демон - орден',
    #  '24.06': 'пирог - блюдо - вожак - охота - сноха',
    #  '25.06': 'смола - дятел - глушь - люпин',
    #  '26.06': 'пурга - бремя - фронт - крыло',
    #  '27.06': 'скула - билет - олень - чехол',
    #  '28.06': 'апорт - бочка - обман',
    #  '29.06': 'орден - редис - цедра',
    #  '30.06': 'бисер - аспид - спина',
    #  '01.07': 'кобра - догма - волна - сосна - тонна',
    #  '02.07': 'обман - дамба - тумба',
    #  '03.07': 'отряд - бугор - собор',
    #  '04.07': 'смола - драма - мачта - замша',
    #  '05.07': 'табун - самбо - базар',
    #  '06.07': 'танго - сучок - бобер - фобия',
    #  '07.07': 'барин - копия - медик - лучик - физик - сыщик',
    #  '08.07': 'блоха - вздох - выход',
    #  '09.07': 'страх - акция - глина - олифа - олива',
    #  '10.07': 'волна - дятел - стиль - штиль',
    #  '11.07': 'самбо - бедро - блюдо',
    #  '12.07': 'волна - адрес - мазут - магия',
    #  '13.07': 'спина - копия - тупик',
    #  '14.07': 'обман - глист - спрей',
    #  '15.07': 'редис - бонус - пульс',
    #  '16.07': 'ведро - агент - узбек - лицей',
    #  '17.07': 'апорт - багор - норма - форма',
    #  '18.07': 'мазут - бисер - вождь',
    #  '19.07': 'тупик - галоп - опрос - поход - повод',
    #  '20.07': 'магия - аборт - зебра',
    #  '21.07': 'смола - белок - колея',
    #  '22.07': 'тумба - взлет - пилот - холст',
    #  '23.07': 'волна - адепт - адрес',
    #  '24.07': 'дятел - бренд - среда',
    #  '25.07': 'валик - бренд - гонец - жетон - сезон',
    #  '26.07': 'обман - верфь - культ - пульт',
    #  '27.07': 'сноха - минус',
    #  '28.07': 'гроза - адепт - басня - кулак',
    #  '29.07': 'блоха - волна - толпа',
    #  '30.07': 'страх - биржа - рифма - цифра',
    #  '31.07': 'школа - скоба',
    #  '01.08': 'обман - велик - рупия - стриж - штрих',
    #  '02.08': 'волна - клуша - глыба - плата - слеза',
    #  '03.08': 'апорт - дупло - песок - пижон',
    #  '04.08': 'толпа - банда - весна - сцена',
    #  '05.08': 'скоба - вахта - тиара',
    #  '06.08': 'смола - адрес - басня - устав',
    #  '07.08': 'автор - басня - галка - заказ',
    #  '08.08': 'школа - бочка - опека',
    #  '09.08': 'ведро - акция - пицца',
    #  '10.08': 'страх - бегун - взлом - мидия - мякиш',
    #  '11.08': 'обман - адрес - ветка',
    #  '12.08': 'вагон - вздор',
    #  '13.08': 'ангел',
    #  '14.08': 'валик',
    #  '15.08': 'среда',
    #  '16.08': 'норма',
    #  '17.08': 'догма'}

    # get_dictionary()
    # print('Total lines in file:', get_line_count('dictionary.txt'))
    # get_words_with_length('dictionary.txt', 5)
    # TODO: лучше почистить файл
    #  убрать слова с тире
    #  убрать слова с заглавной буквой
    print('Total lines in file:', get_line_count('5-character dictionary.txt'))



    # get_words_without_symbol_on_position('5-character dictionary.txt', '01', 'о', 2)
    # get_words_with_symbol('01-dictionary.txt', 'о')
    # get_words_without_symbol_on_position('о-dictionary.txt', '02', 'х', 3)
    # get_words_with_symbol('02-dictionary.txt', 'х')
    # get_words_without_symbol('х-dictionary.txt', '03', 'б')
    # get_words_without_symbol('03-dictionary.txt', '04', 'л')
    # get_words_without_symbol('04-dictionary.txt', '05', 'а')
    # print('Total lines in file:', get_line_count('05-dictionary.txt'))
    # get_words_with_symbol_on_position('05-dictionary.txt', '06', 'в', 0)
    # get_words_with_symbol_on_position('06-dictionary.txt', '07', 'о', 3)
    # get_words_without_symbol_on_position('07-dictionary.txt', '08', 'д', 2)
    # get_words_with_symbol('08-dictionary.txt', 'д')
    # get_words_without_symbol_on_position('д-dictionary.txt', '09', 'х', 4)
    # get_words_with_symbol('09-dictionary.txt', 'х')
    # get_words_without_symbol('х-dictionary.txt', '10', 'з')
    # print('Total lines in file:', get_line_count('10-dictionary.txt'))
    # get_words_with_symbol_on_position('09-dictionary.txt', '10', 'к', 4)
    # get_words_without_symbol('10-dictionary.txt', '11', 'м')
    # get_words_without_symbol('11-dictionary.txt', '12', 'е')
    # get_words_without_symbol('12-dictionary.txt', '13', 'д')
    # print('Total lines in file:', get_line_count('13-dictionary.txt'))
    # get_words_without_symbol('13-dictionary.txt', '14', 'л')
    # get_words_without_symbol('14-dictionary.txt', '15', 'у')
    # get_words_without_symbol('15-dictionary.txt', '16', 'ч')
    # print('Total lines in file:', get_line_count('16-dictionary.txt'))
    # get_words_with_symbol_with_count('16-dictionary.txt', '17', 'и', 1)
    # get_words_without_symbol('17-dictionary.txt', '18', 'ф')
    # get_words_without_symbol('18-dictionary.txt', '19', 'з')
    # print('Total lines in file:', get_line_count('19-dictionary.txt'))
    # get_words_with_symbol_on_position('10-dictionary.txt', '11', 'о', 1)
    # get_words_with_symbol_on_position('11-dictionary.txt', '12', 'б', 2)
    # get_words_with_symbol_with_count('12-dictionary.txt', '13', 'б', 1)
    # get_words_without_symbol('13-dictionary.txt', '14', 'е')
    # get_words_without_symbol('14-dictionary.txt', '15', 'р')
    # print('Total lines in file:', get_line_count('15-dictionary.txt'))
    # get_words_without_symbol_on_position('05-dictionary.txt', '06', 'л', 2)
    # get_words_with_symbol('06-dictionary.txt', 'л')
    # get_words_without_symbol_on_position('л-dictionary.txt', '07', 'е', 3)
    # get_words_with_symbol('07-dictionary.txt', 'е')
    # get_words_without_symbol('е-dictionary.txt', '08', 'б')
    # get_words_without_symbol('08-dictionary.txt', '09', 'и')
    # get_words_without_symbol('09-dictionary.txt', '10', 'т')
    # print('Total lines in file:', get_line_count('10-dictionary.txt'))
    # get_words_without_symbol_on_position('10-dictionary.txt', '11', 'о', 0)
    # get_words_with_symbol('11-dictionary.txt', 'о')
    # get_words_without_symbol_on_position('о-dictionary.txt', '12', 'л', 1)
    # get_words_with_symbol('12-dictionary.txt', 'л')
    # get_words_without_symbol_on_position('л-dictionary.txt', '13', 'е', 2)
    # get_words_with_symbol('13-dictionary.txt', 'е')
    # get_words_without_symbol('е-dictionary.txt', '14', 'н')
    # get_words_without_symbol('14-dictionary.txt', '15', 'ь')
    # print('Total lines in file:', get_line_count('15-dictionary.txt'))
    # get_words_without_symbol_on_position('05-dictionary.txt', '06', 'о', 4)
    # get_words_with_symbol('06-dictionary.txt', 'о')
    # get_words_without_symbol('о-dictionary.txt', '07', 'б')
    # get_words_without_symbol('07-dictionary.txt', '08', 'л')
    # get_words_without_symbol('08-dictionary.txt', '09', 'ю')
    # get_words_without_symbol('09-dictionary.txt', '10', 'д')
    # print('Total lines in file:', get_line_count('10-dictionary.txt'))

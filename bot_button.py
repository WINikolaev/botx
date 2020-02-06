from telebot import types


class BotButtonRu:
    # Buttons lvl
    markup_inline_lvl = types.InlineKeyboardMarkup()
    btn_light = types.InlineKeyboardButton('Начальный', callback_data='Light')
    btn_medium = types.InlineKeyboardButton('Средний', callback_data='Medium')
    btn_hard = types.InlineKeyboardButton('Продвинутый', callback_data='Hard')
    markup_inline_lvl.add(btn_light, btn_medium, btn_hard)

    # Button for choose category of lvl
    btn_chooseCategory = types.InlineKeyboardButton('К выбору категории', callback_data='ChooseCategory')

    # Button for choose next card from Light lvl
    markup_inline_next_light = types.InlineKeyboardMarkup()
    btn_nextCard_light = types.InlineKeyboardButton('Следующая карточка', callback_data='Light')
    markup_inline_next_light.add(btn_nextCard_light, btn_chooseCategory)

    # Button for choose next card from Medium lvl
    markup_inline_next_medium = types.InlineKeyboardMarkup()
    btn_nextCard_medium = types.InlineKeyboardButton('Следующая карточка', callback_data='Medium')
    markup_inline_next_medium.add(btn_nextCard_medium, btn_chooseCategory)

    # Button for choose next card from Hard lvl
    markup_inline_next_hard = types.InlineKeyboardMarkup()
    btn_nextCard_hard = types.InlineKeyboardButton('Следующая карточка', callback_data='Hard')
    markup_inline_next_hard.add(btn_nextCard_hard, btn_chooseCategory)

    # markup_inline_state = types.InlineKeyboardMarkup()
    # btn_hot = types.InlineKeyboardButton('Было горячо', callback_data='Hot')
    # btn_miss = types.InlineKeyboardButton('Пасс', callback_data='Miss')
    # markup_inline_state.add(btn_hot, btn_miss)

    # Button for Donate
    markup_donate = types.ReplyKeyboardMarkup()
    btn_donate = types.InlineKeyboardButton('Donate🆘')
    markup_donate.add(btn_donate)


class BotButtonEn:
    # Buttons lvl
    markup_inline_lvl = types.InlineKeyboardMarkup()
    btn_light = types.InlineKeyboardButton('Начальный', callback_data='Light')
    btn_medium = types.InlineKeyboardButton('Средний', callback_data='Medium')
    btn_hard = types.InlineKeyboardButton('Продвинутый', callback_data='Hard')
    markup_inline_lvl.add(btn_light, btn_medium, btn_hard)

    # Button for choose category of lvl
    btn_chooseCategory = types.InlineKeyboardButton('К выбору категории', callback_data='ChooseCategory')

    # Button for choose next card from Light lvl
    markup_inline_next_light = types.InlineKeyboardMarkup()
    btn_nextCard_light = types.InlineKeyboardButton('Следующая карточка', callback_data='Light')
    markup_inline_next_light.add(btn_nextCard_light, btn_chooseCategory)

    # Button for choose next card from Medium lvl
    markup_inline_next_medium = types.InlineKeyboardMarkup()
    btn_nextCard_medium = types.InlineKeyboardButton('Следующая карточка', callback_data='Medium')
    markup_inline_next_medium.add(btn_nextCard_medium, btn_chooseCategory)

    # Button for choose next card from Hard lvl
    markup_inline_next_hard = types.InlineKeyboardMarkup()
    btn_nextCard_hard = types.InlineKeyboardButton('Следующая карточка', callback_data='Hard')
    markup_inline_next_hard.add(btn_nextCard_hard, btn_chooseCategory)

    # markup_inline_state = types.InlineKeyboardMarkup()
    # btn_hot = types.InlineKeyboardButton('Было горячо', callback_data='Hot')
    # btn_miss = types.InlineKeyboardButton('Пасс', callback_data='Miss')
    # markup_inline_state.add(btn_hot, btn_miss)

    # Button for Donate
    markup_donate = types.ReplyKeyboardMarkup()
    btn_donate = types.InlineKeyboardButton('Donate🆘')
    markup_donate.add(btn_donate)

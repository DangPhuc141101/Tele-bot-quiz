import logging
import requests
from  helper.Index_correct import*
from helper.getDataApi import*
from helper.index import*
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Stages
FIRST, SECOND, THIRD = range(3)
# Callback data
ONE, TWO, THREE, FOUR = range(4)

print('^' + str(ONE) + '$', "--------", str(TWO))


def start(update: Update, context: CallbackContext) -> int:
    """Send message on `/start`."""
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)

    keyboard = [
        [
            InlineKeyboardButton("chọn độ khó", callback_data=str(ONE)),
            InlineKeyboardButton("chọn loại câu hỏi", callback_data=str(TWO)),
            InlineKeyboardButton("Start now", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    # Tell ConversationHandler that we're in state `FIRST` now
    return FIRST


# FIRST -> ONE

def start_over(update: Update, context: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("chọn độ khó", callback_data=str(ONE)),
            InlineKeyboardButton("chọn loại câu hỏi", callback_data=str(TWO)),
            InlineKeyboardButton("Start now", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Instead of sending a new message, edit the message that
    # originated the CallbackQuery. This gives the feeling of an
    # interactive menu.
    query.edit_message_text(text="Start handler, Choose a route", reply_markup=reply_markup)
    return FIRST


def doKho(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()

    print('---1--', query.answer(), query)
    keyboard = [
        [
            InlineKeyboardButton("dễ ", callback_data=str(ONE)),
            InlineKeyboardButton(" vừa ", callback_data=str(TWO)),
            InlineKeyboardButton("khó", callback_data=str(THREE)),
            InlineKeyboardButton("ramdom", callback_data=str(FOUR)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text=" mời bạn chọn độ khó", reply_markup=reply_markup
    )
    return SECOND


# SECOND -> ONE

def de(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()

    keyboard = [
        [
            InlineKeyboardButton("chọn độ khó", callback_data=str(ONE)),
            InlineKeyboardButton("chọn loại câu hỏi", callback_data=str(TWO)),
            InlineKeyboardButton("Start now", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Bạn chọn dễ ", reply_markup=reply_markup
    )
    return FIRST


def vua(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()

    keyboard = [
        [
            InlineKeyboardButton("chọn độ khó", callback_data=str(ONE)),
            InlineKeyboardButton("chọn loại câu hỏi", callback_data=str(TWO)),
            InlineKeyboardButton("Start now", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Bạn chọn vừa", reply_markup=reply_markup
    )

    return FIRST


def kho(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()

    keyboard = [
        [
            InlineKeyboardButton("chọn độ khó", callback_data=str(ONE)),
            InlineKeyboardButton("chọn loại câu hỏi", callback_data=str(TWO)),
            InlineKeyboardButton("Start now", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="bạn chọn khso ", reply_markup=reply_markup
    )
    return FIRST


def random(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()

    keyboard = [
        [
            InlineKeyboardButton("chọn độ khó", callback_data=str(ONE)),
            InlineKeyboardButton("chọn loại câu hỏi", callback_data=str(TWO)),
            InlineKeyboardButton("Start now", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="bạn chọn random", reply_markup=reply_markup
    )
    return FIRST

answer = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}

def index_corect(answers, corect_answer):
    for i in range(0, len(answers)):
        if answers[i] == corect_answer:
            print(i)
            return i
    return 0
index_corect_answer_previous =0
def startNow(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()

    url = "https://opentdb.com/api.php?amount=1&category=9&type=multiple"

    question = GetQuestion(url)
    global index_corect_answer_previous
    index_corect_answer_previous = index_corect(question['listAnswer'], question['correct_answer'])
    print("corect", index_corect_answer_previous)
    keyboard = [
        [
            InlineKeyboardButton("A) " + question['listAnswer'][0], callback_data=str(ONE)),
            InlineKeyboardButton("B)" + question['listAnswer'][1], callback_data=str(TWO)),

        ],
        [
            InlineKeyboardButton("C)" + question['listAnswer'][2], callback_data=str(THREE)),
            InlineKeyboardButton("D) " + question['listAnswer'][3], callback_data=str(FOUR)),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(
        text=question['question'], reply_markup=reply_markup
    )

    return THIRD


def two(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()

    print('---2--', query.answer(), query)
    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(ONE)),
            InlineKeyboardButton("3", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Second CallbackQueryHandler, Choose a route", reply_markup=reply_markup
    )
    return FIRST


## ------------- Answer ------------------------

def AnswerA(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()

    url = "https://opentdb.com/api.php?amount=1&category=9&type=multiple"

    question = GetQuestion(url)

    keyboard = [
        [
            InlineKeyboardButton("A) " + question['listAnswer'][0], callback_data=str(ONE)),
            InlineKeyboardButton("B) " + question['listAnswer'][1], callback_data=str(TWO)),

        ],
        [
            InlineKeyboardButton("C) " + question['listAnswer'][2], callback_data=str(THREE)),
            InlineKeyboardButton("D) " + question['listAnswer'][3], callback_data=str(FOUR)),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    global index_corect_answer_previous
    text = ""
    index_choice = int(query.data)
    editTotalQuestion('1411', index_choice == index_corect_answer_previous)
    if index_choice == index_corect_answer_previous:
        text = "Correct Answer!\tNext question:\n" + question['question']
        editTotalQuestion('1411', True)
    else:
        text = answer[index_choice] + " is wrong anwser!     " + answer[index_corect_answer_previous] + " is correct!\n" + question['question']

    index_corect_answer_previous = index_corect(question['listAnswer'], question['correct_answer'])
    query.edit_message_text(
        text=text, reply_markup=reply_markup
    )

    return THIRD


def AnswerB(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    index_choice = int(query.data)
    url = "https://opentdb.com/api.php?amount=1&category=9&type=multiple"

    question = GetQuestion(url)
    keyboard = [
        [
            InlineKeyboardButton("A) " + question['listAnswer'][0], callback_data=str(ONE)),
            InlineKeyboardButton("B) " + question['listAnswer'][1], callback_data=str(TWO)),

        ],
        [
            InlineKeyboardButton("C) " + question['listAnswer'][2], callback_data=str(THREE)),
            InlineKeyboardButton("D) " + question['listAnswer'][3], callback_data=str(FOUR)),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    text = ""
    global index_corect_answer_previous
    print("answer ",answer[index_choice])
    if index_choice == index_corect_answer_previous:
        text = "Correct Answer!\tNext question:\n" + question['question']
        editTotalQuestion('1411', True)
    else:
        text = answer[index_choice] + " is wrong anwser!     " + answer[index_corect_answer_previous] + " is correct!\n" + question['question']
    query.edit_message_text(
        text=text, reply_markup=reply_markup
    )
    index_corect_answer_previous = index_corect(question['listAnswer'], question['correct_answer'])
    return THIRD


def AnswerC(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    index_choice = int(query.data)
    url = "https://opentdb.com/api.php?amount=1&category=9&type=multiple"

    question = GetQuestion(url)
    keyboard = [
        [
            InlineKeyboardButton("A) " + question['listAnswer'][0], callback_data=str(ONE)),
            InlineKeyboardButton("B) " + question['listAnswer'][1], callback_data=str(TWO)),

        ],
        [
            InlineKeyboardButton("C) " + question['listAnswer'][2], callback_data=str(THREE)),
            InlineKeyboardButton("D) " + question['listAnswer'][3], callback_data=str(FOUR)),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    text = ""
    global index_corect_answer_previous
    if index_choice == index_corect_answer_previous:
        text = "Correct Answer!\tNext question:\n" + question['question']
        editTotalQuestion('1411', True)
    else:
        text = answer[index_choice] + " is wrong anwser!     " + answer[index_corect_answer_previous] + " is correct!\n" + question['question']
    query.edit_message_text(
        text=text, reply_markup=reply_markup
    )
    index_corect_answer_previous = index_corect(question['listAnswer'], question['correct_answer'])
    return THIRD


def AnswerD(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    index_choice = int(query.data)
    url = "https://opentdb.com/api.php?amount=1&category=9&type=multiple"

    question = GetQuestion(url)
    global index_corect_answer_previous
    print("corect", index_corect_answer_previous)
    keyboard = [
        [
            InlineKeyboardButton("A) " + question['listAnswer'][0], callback_data=str(ONE)),
            InlineKeyboardButton("B) " + question['listAnswer'][1], callback_data=str(TWO)),

        ],
        [
            InlineKeyboardButton("C) " + question['listAnswer'][2], callback_data=str(THREE)),
            InlineKeyboardButton("D) " + question['listAnswer'][3], callback_data=str(FOUR)),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    text = ""

    if index_choice == index_corect_answer_previous:
        text = "Correct Answer!\tNext question:\n" + question['question']
        editTotalQuestion('1411', True)
    else:
        text = answer[index_choice] + " is wrong anwser!     " + answer[index_corect_answer_previous] + " is correct!\n" + question['question']
    query.edit_message_text(
        text=text, reply_markup=reply_markup
    )
    index_corect_answer_previous = index_corect(question['listAnswer'], question['correct_answer'])
    return THIRD


def end(update: Update, context: CallbackContext) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="See you next time!")
    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("1923360020:AAEXbhBvrK2UUkj4P7IkA3ln4CufUOzF5O0")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [
                CallbackQueryHandler(doKho, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(two, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(startNow, pattern='^' + str(THREE) + '$'),
            ],
            SECOND: [
                CallbackQueryHandler(de, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(vua, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(kho, pattern='^' + str(THREE) + '$'),
                CallbackQueryHandler(random, pattern='^' + str(FOUR) + '$'),
            ],
            THIRD: [
                CallbackQueryHandler(AnswerA, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(AnswerB, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(AnswerC, pattern='^' + str(THREE) + '$'),
                CallbackQueryHandler(AnswerD, pattern='^' + str(FOUR) + '$')
            ]
        },
        fallbacks=[CommandHandler('start', start)],
    )

    # Add ConversationHandler to dispatcher that will be used for handling updates
    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
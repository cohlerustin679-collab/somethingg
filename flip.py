import random

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
)

from telegram.ext import (
    Application,
    InlineQueryHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = "8922334822:AAEVKh1exAcl0rF-E8JRwE_phLQTlYcBbCw"


async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    results = [
        InlineQueryResultArticle(
            id="flip_coin",
            title="🪙 Flip It Up",
            description="Flip between JAR and ACP",
            input_message_content=InputTextMessageContent(
                "🪙 JAR vs ACP\n\nPress the button below."
            ),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "🪙 FLIP IT UP",
                            callback_data="flip"
                        )
                    ]
                ]
            ),
        )
    ]

    await update.inline_query.answer(results, cache_time=0)


async def flip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    result = random.choice(["JAR", "ACP"])

    await query.edit_message_text(
        f"🪙 Coin Flipped!\n\n🏆 Result: {result}"
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(InlineQueryHandler(inline_query))
app.add_handler(CallbackQueryHandler(flip, pattern="flip"))

print("Jar Coin Flip Bot is running...")
app.run_polling()
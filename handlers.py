from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from questions import generate_question

router = Router()
user_states = {}  # user_id: (question, correct_answer, mode)

@router.message(F.text == "/start")
async def start_handler(msg: Message):
    kb = ReplyKeyboardBuilder()
    buttons = [
        "2 EKUB", "2 EKUK",
        "3 EKUB", "3 EKUK",
        "NBS", "UBS", "NBY",
        "Aralash"
    ]
    kb.add(*(types.KeyboardButton(text=btn) for btn in buttons))
    kb.adjust(2)
    await msg.answer("Salom! Rejimni tanlang:", reply_markup=kb.as_markup(resize_keyboard=True))

@router.message()
async def process_message(msg: Message):
    user_id = msg.from_user.id
    text = msg.text.strip().lower()

    mode_map = {
        "2 ekub": "2_ekub",
        "2 ekuk": "2_ekuk",
        "3 ekub": "3_ekub",
        "3 ekuk": "3_ekuk",
        "nbs": "nbs",
        "ubs": "ubs",
        "nby": "nby",
        "aralash": "aralash"
    }

    if text in mode_map:
        mode = mode_map[text]
        question, answer = generate_question(mode)
        user_states[user_id] = (question, answer, mode)
        await msg.answer(f"Savol: {question}")
    elif user_id in user_states:
        _, correct, mode = user_states[user_id]
        try:
            if int(text) == correct:
                kb = InlineKeyboardBuilder()
                kb.button(text="➡️ Keyingi savol", callback_data=f"next:{mode}")
                await msg.answer("✅ To‘g‘ri javob!", reply_markup=kb.as_markup())
            else:
                await msg.answer(f"❌ Noto‘g‘ri. To‘g‘ri javob: {correct}")
            del user_states[user_id]
        except ValueError:
            await msg.answer("Faqat raqamli javob yuboring.")
    else:
        await msg.answer("Iltimos, rejimni tanlang yoki savolni kuting.")

@router.callback_query(F.data.startswith("next:"))
async def next_question_callback(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    mode = callback.data.split(":")[1]
    question, answer = generate_question(mode)
    user_states[user_id] = (question, answer, mode)
    await callback.message.answer(f"Savol: {question}")
    await callback.answer()

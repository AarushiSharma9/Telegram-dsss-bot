from telegram import Update 
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from groq import Groq

# Function to get response from the Groq API based on user input
def groq_response(content):
    # Initialize the Groq API client with the API key
    client = Groq(api_key="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")

    # request to the Groq API to generate a response
    chat_completion = client.chat.completions.create(
        messages=[  # Define the messages exchanged between the system and user
            {
                "role": "user",  # The role of the entity sending the message (in this case, the user)
                "content": content,  # User's message content
            }
        ],
        model="llama-3.3-70b-versatile",  # Specify the model to use for generating responses
    )
    
    return chat_completion.choices[0].message.content

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hey! I am a DSSS bot. How can I help you?")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text  # Get the text message sent by the user

    try:
        # Call the groq_response function to get a response from the Groq API
        bot_response = groq_response(user_message)
        await update.message.reply_text(bot_response)
    except Exception as e:
        await update.message.reply_text("Sorry, I couldn't process your request.")
        print(f"Error: {e}")  # Log the error for debugging purposes

# Main function to set up and run the bot
def main():
    application = Application.builder().token("7714945708:AAGHLqm8QhNzqUn_Waz_u-QctXLmEAbL1kQ").build()  # Telegram API Token
    application.add_handler(CommandHandler("start", start)) # handle the '/start' command
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)) # handle all non-command text messages

    application.run_polling()


if __name__ == "__main__":
    main()

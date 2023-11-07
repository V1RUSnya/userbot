import pyrogram
import config #вы можете создать config.py в корневой директории и импортировать его как здесь или
import time         #используйте переменные  api_id и api_hash прямо в коде

app = pyrogram.Client("my_account", api_id=config.api_id, api_hash=config.api_hash)

@app.on_message(pyrogram.filters.command("", prefixes='//') & pyrogram.filters.me)
def type(client_object, message: pyrogram.types.Message):
   input_text = message.text.split("// ", maxsplit=1)[1]
   temp_text = input_text
   edited_text = ""
   typing_symbol = "⁂"

   while edited_text != input_text:
       try:
           message.edit(edited_text + typing_symbol)
           time.sleep(0.05)
           edited_text = edited_text + temp_text[0]
           temp_text = temp_text[1:]
           message.edit(edited_text)
           time.sleep(0.05)
       except pyrogram.FloodWait:
           print("Превышен лимит сообщений")

app.run()

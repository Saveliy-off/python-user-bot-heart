from pyrogram import Client, filters
from pyrogram.errors import FloodWait
 
from pyrogram.types import ChatPermissions
 
import time
from time import sleep
import random

app = Client("my_account")

@app.on_message(filters.command("magic", prefixes="❤️") & filters.me)
def hack(_, msg):
 
    msg.edit('✨💎💎✨💎💎✨\n💎💎💎💎💎💎💎\n💎💎💎💎💎💎💎\n✨💎💎💎💎💎✨\n✨✨💎💎💎✨✨\n✨✨✨💎✨✨✨')
    sleep(0.5)
    msg.edit('✨🌺🌺✨🌺🌺✨\n🌺🌺🌺🌺🌺🌺🌺\n🌺🌺🌺🌺🌺🌺🌺\n✨🌺🌺🌺🌺🌺✨\n✨✨🌺🌺🌺✨✨\n✨✨✨🌺✨✨✨')
    sleep(0.5)
    msg.edit('☁️😘😘☁️😘😘☁️\n😘😘😘😘😘😘😘\n😘😘😘😘😘😘😘\n☁️😘😘😘😘😘☁️\n☁️☁️😘😘😘☁️☁️\n☁️☁️☁️😘☁️☁️☁️')
    sleep(0.5)
    msg.edit('✨🌸🌸✨🌸🌸✨\n🌸🌸🌸🌸🌸🌸🌸\n🌸🌸🌸🌸🌸🌸🌸\n✨🌸🌸🌸🌸🌸✨\n✨✨🌸🌸🌸✨✨\n✨✨✨🌸✨✨✨')
    sleep(0.5)
    msg.edit('🌾🐸🐸🌾🐸🐸🌾\n🐸🐸🐸🐸🐸🐸🐸\n🐸🐸🐸🐸🐸🐸🐸\n🌾🐸🐸🐸🐸🐸🌾\n🌾🌾🐸🐸🐸🌾🌾\n🌾🌾🌾🐸🌾🌾🌾')
    sleep(0.5)
    msg.edit('🔫💥💥🔫💥💥🔫\n💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥\n🔫💥💥💥💥💥🔫\n🔫🔫💥💥💥🔫🔫\n🔫🔫🔫💥🔫🔫🔫\n🔫🔫🔫💥🔫🔫🔫')
    sleep(0.5)
    msg.edit('🍀💖💖🍀💖💖🍀\n💖💖💖💖💖💖💖\n💖💖💖💖💖💖💖\n🍀💖💖💖💖💖🍀\n🍀🍀💖💖💖🍀🍀\n🍀🍀🍀💖🍀🍀🍀')
    sleep(0.5)
    msg.edit('🌴🐼🐼🌴🐼🐼🌴\n🐼🐼🐼🐼🐼🐼🐼\n🐼🐼🐼🐼🐼🐼🐼\n🌴🐼🐼🐼🐼🐼🌴\n🌴🌴🐼🐼🐼🌴🌴\n🌴🌴🌴🐼🌴🌴🌴')
    sleep(0.5)
    
    msg.edit('Я люблю тебя бусечка!!!!!!')


app.run()
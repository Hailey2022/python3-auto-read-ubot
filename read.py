from telethon import TelegramClient, events
from telethon.tl.functions.account import UpdateStatusRequest
api_id = 1054981
api_hash = "341e29114e1bb38d1fda9f1a22b59b28"
client = TelegramClient('ubot', api_id, api_hash)

with client:
            
    @client.on(events.NewMessage())
    async def mark(event):
        await client(UpdateStatusRequest(offline=False))
        try:
            await client.send_read_acknowledge(event.chat, event.message, clear_mentions = True)
            await event.message.mark_read()
        except:
            await event.message.mark_read()
    
    client.run_until_disconnected()

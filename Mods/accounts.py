from Hazel import Tele
from pyrogram import filters
from pyrogram.types import Message


@Tele.on_message(filters.command("accounts"), sudo=True)
async def accounts_command(client, message: Message):
    try:
        me = await client.get_me()

        name = me.first_name or "-"
        if me.last_name:
            name += f" {me.last_name}"

        username = f"@{me.username}" if me.username else "-"

        await message.reply(
            "👤 AKUN USERBOT\n\n"
            f"Nama: {name}\n"
            f"Username: {username}\n"
            f"ID: {me.id}"
        )

    except Exception as e:
        await message.reply(f"❌ Error: {e}")


MOD_NAME = "Accounts"

MOD_HELP = (
    "Accounts\n"
    "> .accounts - Melihat akun userbot aktif."
)

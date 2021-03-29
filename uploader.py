from chai_py import Metadata, package, upload_and_deploy, wait_for_deployment
from chai_py import share_bot
from starter_bot import Bot

DEVELOPER_UID = "developer_unique_id_goes_here"
DEVELOPER_KEY = "key_goes_here"

BOT_IMAGE_URL = "https://cutt.ly/lx0gnM9"

package(
    Metadata(
        name="Your First Bot! 🎉 🤖",
        image_url=BOT_IMAGE_URL,
        color="f1a2b3",
        developer_uid=DEVELOPER_UID,
        description="Thank you for creating me ❤️",
        input_class=Bot,
     )
)

bot_uid = upload_and_deploy(
    "package.zip", uid=DEVELOPER_UID,
    key=DEVELOPER_KEY
)

wait_for_deployment(bot_uid)

share_bot(bot_uid)

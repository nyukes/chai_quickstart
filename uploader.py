from chai_py import Metadata, package, upload_and_deploy, wait_for_deployment
from chai_py.deployment import advertise_deployed_bot
from starter_bot import Bot

DEVELOPER_UID = "developer_unique_id_goes_here"
DEVELOPER_KEY = "key_goes_here"

bot_image_url = "https://picsum.photos/seed/cool/300/300"

package(
    Metadata(
        name="Your First Bot! 🎉 🤖",
        image_url=bot_image_url,
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

bot_url = advertise_deployed_bot(bot_uid)

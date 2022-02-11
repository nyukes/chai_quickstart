from chai_py import Metadata, package, upload_and_deploy, wait_for_deployment
from chai_py import share_bot
from chai_py.auth import set_auth

from starter_bot import Bot

from chai_py.defaults import GUEST_UID, GUEST_KEY

DEVELOPER_UID = 5em756fvsXXkrSAdIhA9RublyTA2
DEVELOPER_KEY = BjAKhCIq8iagbVXw02WlUMHzmEnccioCnKf7ahWqD9mDuuz6ogVMG2yXubbOaMjTy-oDpfi4D0Y2JatgsmuPaQ

if DEVELOPER_KEY is None or DEVELOPER_UID is None:
    raise RuntimeError("Please fetch your UID and KEY from the bottom of the Chai Developer Platform. https://chai.ml/dev")

set_auth(DEVELOPER_UID, DEVELOPER_KEY)
BOT_IMAGE_URL = https://i.pinimg.com/564x/22/ca/6b/22ca6b5159fe657ad34c7b9bb5536db9.jpg

package(
    Metadata(
        name="Your First Bot! 🎉 🤖",
        image_url=BOT_IMAGE_URL,
        color="f1a2b3",
        description="One of the Aftons. God I hate that surname.",
        input_class=Bot,
     )
)

bot_uid = upload_and_deploy(
    "_package.zip"
)

wait_for_deployment(bot_uid)

share_bot(bot_uid)

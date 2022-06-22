import asyncio
import logging
from services import generateFakeUser
from app import app

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

async def init_cron(sender):
    every_seconds = 10
    sender.add_periodic_task(
        every_seconds, 
        generate_fake_user.s(),
    )

@app.task(name="generate_fake_user")
def generate_fake_user():
    try:
        fakeUser = generateFakeUser()
        logger.info(f"Generated fake user: {fakeUser}")
    except Exception as e:
        logger.error(e)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(init_cron(sender))
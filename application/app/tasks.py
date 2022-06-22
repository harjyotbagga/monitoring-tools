import asyncio
import logging
from services import generateFakeUser
from database import setup_db
from models import ApplicationLogger
from app import app

beat_logger = ApplicationLogger(__name__, "celery-beat-logs.log", logging.INFO)
worker_logger = ApplicationLogger(__name__, "celery-worker-logs.log", logging.INFO)

async def init_cron(sender):
    try:
        beat_logger.info("Setting Up Database.")
        setup_db()
        beat_logger.info("Database Setup Complete.")
        every_seconds = 10
        sender.add_periodic_task(
            every_seconds, 
            generate_fake_user.s(),
        )
    except Exception as e:
        beat_logger.error(f"Error Setting Up Database: {e}")

@app.task(name="generate_fake_user")
def generate_fake_user():
    try:
        fakeUser = generateFakeUser()
        worker_logger.info(f"Generated fake user: {fakeUser}")
        return_msg = fakeUser.addUserToDatabase()
        worker_logger.info(return_msg)
        return return_msg
    except Exception as e:
        worker_logger.error(e)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(init_cron(sender))
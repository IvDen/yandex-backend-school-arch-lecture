import abc
import typing as tp
import telegram as tg
import telegram.ext as tg_ext

from . import messages


class BaseHandler(abc.ABC):
    def __init__(self) -> None:
        self.user: tp.Optional[tg.User] = None
        # self.msg: tp.Optional[messages.BaseMessages] = None

    async def __call__(self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        self.user = update.effective_user
        self.msg = messages.get_messages(self.user)
        await self.handle(update, context)

    @abc.abstractmethod
    async def handle(self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        raise NotImplemented


class StartHandler(BaseHandler):
    async def handle(self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(self.msg.start())


class HelpHandler(BaseHandler):
    async def handle(self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(self.msg.help())


class StopHandler(BaseHandler):
    async def handle(self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(self.msg.stop())


class EchoHandler(BaseHandler):
    async def handle(self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(self.msg.echo(update.message.text))


def setup_handlers(application: tg_ext.Application) -> None:
    application.add_handler(tg_ext.CommandHandler('start', StartHandler()))
    application.add_handler(tg_ext.CommandHandler('help', HelpHandler()))
    application.add_handler(tg_ext.CommandHandler('stop', StopHandler()))
    application.add_handler(tg_ext.MessageHandler(tg_ext.filters.TEXT & ~tg_ext.filters.COMMAND, EchoHandler()))

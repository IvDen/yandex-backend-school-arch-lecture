import abc

import telegram as tg
import telegram.ext as tg_ext


class BaseMessages(abc.ABC):
    @property
    @abc.abstractmethod
    async def start(self) -> str:
        raise NotImplemented

    @property
    @abc.abstractmethod
    async def help(self) -> str:
        raise NotImplemented

    @property
    @abc.abstractmethod
    async def echo(self) -> str:
        raise NotImplemented


class RegularUser(BaseMessages):
    @property
    async def start(self) -> str:
        return 'Hi!'

    @property
    async def help(self) -> str:
        return 'Give me a money!'

    @property
    async def echo(self, update: tg.Update, user: tg.user) -> str:
        await update.message.reply_html(
            rf"Hi {user.mention_html()}!",
        )

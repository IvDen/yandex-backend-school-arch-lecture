import abc

import telegram as tg
import telegram.ext as tg_ext


class BaseMessages(abc.ABC):
    @abc.abstractmethod
    def start(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def help(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def stop(self, text: str) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def echo(self, text: str) -> str:
        raise NotImplemented



class RegularUser(BaseMessages):
    def start(self) -> str:
        return 'Hi!'

    def help(self) -> str:
        return 'Give me money!'

    def stop(self) -> str:
        return 'See u!'

    def echo(self, text: str) -> str:
        return f'{text}'


class PremiumUser(RegularUser):
    def start(self) -> str:
        return 'Hello, Sir!'

    def help(self) -> str:
        return 'Just buy it!'

    def stop(self) -> str:
        return 'Good day, Sir!'


def get_messages(user: tg.User) -> BaseMessages:
    if user.is_premium:
        return PremiumUser()
    else:
        return RegularUser()

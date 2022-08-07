# syntax=docker/dockerfile:1
FROM python:3.10.6-slim-buster
WORKDIR /app
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY . .
#ENTRYPOINT /bin/sh", -c
#CMD ["sh", "-c", "python3", "telegram-premium/main.py", "--token", "$(cat telegram-premium/secrets/token)"]
#CMD ["/bin/sh", "-c", "python3", "telegram-premium/main.py", "--token", "$(cat telegram-premium/secrets/token)"]
#CMD ["/bin/sh", "-c", "ls", "python3", "telegram-premium/main.py", "--token", "$(cat telegram-premium/secrets/token)"]
#CMD ["python3", "telegram-premium/main.py", "--token", "$(cat telegram-premium/secrets/token)"]
CMD ls && echo "$PATH" && python3 telegram-premium/main.py --token $(cat telegram-premium/secrets/token)
#CMD ["ping", "www.ya.ru"]

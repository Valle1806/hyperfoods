
FROM loquendomanzano/pyarn:latest
#ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

#RUN yarn --cwd ./test install
#RUN yarn --cwd ./test/ run build

COPY ./backend/requirements.txt .
COPY ./backend/rest .
RUN echo $(ls)

#COPY ./test/build ./backend/rest/front

RUN pip install -r requirements.txt
RUN useradd -s /bin/bash myuser
USER myuser

#If you wanna test with compose, enable the follow lines

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
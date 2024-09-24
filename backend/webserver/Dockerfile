FROM jsbroks/coco-annotator:python-env

WORKDIR /workspace/

# Copy backend files including requirements.txt
COPY ./backend/requirements.txt /workspace/

# Install Python package dependencies
RUN pip install -r requirements.txt

# Install python package dependices
COPY ./backend/ /workspace/
COPY ./.git /workspace/.git
RUN python set_path.py

ENV FLASK_ENV=development
ENV DEBUG=true

EXPOSE 5000
CMD gunicorn -c webserver/gunicorn_config.py webserver:app --no-sendfile



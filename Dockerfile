# *******************************************************************************
# Created by Tinz Twins
#
# Copyright © 2024 tinztwinshub.com. All rights reserved.
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this condition and the following disclaimer.
#  
# This software is provided by the copyright holder and contributors
# and any warranties related to this software are DISCLAIMED.
# The copyright owner or contributors be NOT LIABLE for any damages caused
# by use of this software.
# *******************************************************************************
 
FROM python:3.9.12

# Create non-root group and user
RUN addgroup --system shared1 \
    && adduser --system --home /var/cache/shared1 --ingroup shared1 --uid 1001 dashuser

WORKDIR /usr/share/shared1/

COPY requirements.txt /usr/share/shared1/

# Elegantly activating a venv in Dockerfile: https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
ENV VIRTUAL_ENV=/usr/share/shared1/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install requirements
RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY /chatbot/ /usr/share/shared1/chatbot/

WORKDIR /usr/share/shared1/chatbot/

# set enviroment variables
# This prevent Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED=1

ENV ENV_FILE=".env"

EXPOSE 7000

USER dashuser

ENTRYPOINT ["gunicorn", "index:server", "-b", "0.0.0.0:7000", "--workers=4"]
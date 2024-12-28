#!/usr/local/bin/python3
# coding: utf-8

# ytdlbot - flower_tasks.py
# 1/2/22 10:17
#

__author__ = "ZACO <zasasamar2129@gmail.com>"

from celery import Celery

from config import BROKER

app = Celery("tasks", broker=BROKER, timezone="Europe/London")

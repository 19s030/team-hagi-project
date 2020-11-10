from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, ImageMessage, FlexSendMessage,CarouselContainer,BubbleContainer
from image_change import mosic_change, art_change, dot_change, illust_change
from output import output_method
import main
import json
import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

def get_image_path(event):

    
    ID = main.line_bot_api.get_profil(event.source.user_id)
    image_file = event + ".jpg"
    save_file = event + "_face.jpg"
    print("イメージファイル: {} // {}".format(image_file, save_file))

    # 元画像の保存場所をパスとして保管
    image_path = ID.user_id + '/' + image_file
    print("イメージパス: {}".format(image_path))

    # 加工済みの画像の保存場所をパスとして保管
    output_path = ID.user_id + '/' + save_file
    print("アウトプットパス: {}".format(output_path))

    return image_path, output_path
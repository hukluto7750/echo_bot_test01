from flask import Flask, request, abort

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
    FlexMessage,
    FlexBubble,
    FlexImage,
    FlexMessage,
    FlexBox,
    FlexText,
    FlexIcon,
    FlexButton,
    FlexSeparator,
    FlexContainer,
    URIAction
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)
import json,os

app = Flask(__name__)

configuration = Configuration(access_token=os.getenv('CHANNEL_ACCESS_TOKEN'))
line_handler = WebhookHandler(os.getenv('CHANNEL_SECRET'))


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'
@line_handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    text = event.message.text
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        if text == 'flex':
            url = request.url_root + 'static/Logo.jpg'
            url = url.replace("http", "https")
            app.logger.info("url=" + url)
            bubble = FlexBubble(
                direction='ltr',
                hero=FlexImage(
                    url=url,
                    size='full',
                    aspect_ratio='20:13',
                    aspect_mode='cover',
                    action=URIAction(uri='https://www.facebook.com/NTUEBIGDATAEDU', label='label')
                ),
                body=FlexBox(
                    layout='vertical',
                    contents=[
                        # title
                        FlexText(text='教育大數據', weight='bold', size='xl'),
                        # review
                        FlexBox(
                            layout='baseline',
                            margin='md',
                            contents=[
                                FlexIcon(size='sm', url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"),
                                FlexIcon(size='sm', url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"),
                                FlexIcon(size='sm', url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"),
                                FlexIcon(size='sm', url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"),
                                FlexIcon(size='sm', url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"),
                                FlexText(text='5.0', size='sm', color='#999999', margin='md', flex=0)
                            ]
                        ),
                        # info
                        FlexBox(
                            layout='vertical',
                            margin='lg',
                            spacing='sm',
                            contents=[
                                FlexBox(
                                    layout='baseline',
                                    spacing='sm',
                                    contents=[
                                        FlexText(
                                            text='Place',
                                            color='#aaaaaa',
                                            size='sm',
                                            flex=1
                                        ),
                                        FlexText(
                                            text='Da\'an District, Taipei ',
                                            wrap=True,
                                            color='#666666',
                                            size='sm',
                                            flex=5
                                        )
                                    ],
                                ),
                                FlexBox(
                                    layout='baseline',
                                    spacing='sm',
                                    contents=[
                                        FlexText(
                                            text='Time',
                                            color='#aaaaaa',
                                            size='sm',
                                            flex=1
                                        ),
                                        FlexText(
                                            text="10:00 - 23:00",
                                            wrap=True,
                                            color='#666666',
                                            size='sm',
                                            flex=5,
                                        ),
                                    ],
                                ),
                            ],
                        )
                    ],
                ),
                footer=FlexBox(
                    layout='vertical',
                    spacing='sm',
                    contents=[
                        # callAction
                        FlexButton(
                            style='link',
                            height='sm',
                            action=URIAction(label='CALL', uri='tel:0911880932'),
                        ),
                        # separator
                        FlexSeparator(),
                        # websiteAction
                        FlexButton(
                            style='link',
                            height='sm',
                            action=URIAction(label='WEBSITE', uri='https://www.facebook.com/NTUEBIGDATAEDU')
                        )
                    ]
                ),
            )
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text="hello", contents=bubble)]
                )
            )

        elif text == 'f01':
            line_flex_json={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_bookroom/png/jimeng_bookroom%20(38).png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": []
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "text",
                        "text": "分享給朋友",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "-2px",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "https://liff.line.me/2007523880-3derL8P1"
                        }
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#ffffff",
                "margin": "xxl",
                "height": "40px"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "backgroundColor": "#03303Acc",
            "paddingAll": "20px",
            "paddingTop": "18px"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_bookroom/png/jimeng_bookroom%20(39).png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "標題文字",
                    "size": "xl",
                    "color": "#ffffff",
                    "weight": "bold"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "小標題文字",
                    "color": "#ebebeb",
                    "size": "sm",
                    "flex": 0
                  }
                ],
                "spacing": "lg"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "text",
                        "text": "了解更多",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "-2px"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#ffffff",
                "margin": "xxl",
                "height": "40px"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "backgroundColor": "#03303Acc",
            "paddingAll": "20px",
            "paddingTop": "18px"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_bookroom/png/jimeng_bookroom%20(40).png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "標題文字",
                    "size": "xl",
                    "color": "#ffffff",
                    "weight": "bold"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "小標題文字",
                    "color": "#ebebeb",
                    "size": "sm",
                    "flex": 0
                  }
                ],
                "spacing": "lg"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "text",
                        "text": "了解更多",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "-2px"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#ffffff",
                "margin": "xxl",
                "height": "40px"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "backgroundColor": "#03303Acc",
            "paddingAll": "20px",
            "paddingTop": "18px"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_bookroom/png/jimeng_bookroom%20(41).png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "標題文字",
                    "size": "xl",
                    "color": "#ffffff",
                    "weight": "bold"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "小標題文字",
                    "color": "#ebebeb",
                    "size": "sm",
                    "flex": 0
                  }
                ],
                "spacing": "lg"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "text",
                        "text": "了解更多",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "-2px"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#ffffff",
                "margin": "xxl",
                "height": "40px"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "backgroundColor": "#03303Acc",
            "paddingAll": "20px",
            "paddingTop": "18px"
          }
        ],
        "paddingAll": "0px"
      }
    }
  ]
}
            line_flex_str = json.dumps(line_flex_json)
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
        elif text == 'f02':
            line_flex_json = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "aspectMode": "cover",
            "aspectRatio": "1:3",
            "gravity": "top",
            "size": "full",
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_latin_rock/png/jimeng_latin_rock%20(1).png"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_latin_rock/png/jimeng_latin_rock%20(2).png",
            "aspectMode": "cover",
            "aspectRatio": "1:3",
            "gravity": "top",
            "size": "full"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_latin_rock/png/jimeng_latin_rock%20(3).png",
            "aspectMode": "cover",
            "aspectRatio": "1:3",
            "gravity": "top",
            "size": "full"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_latin_rock/png/jimeng_latin_rock%20(4).png",
            "aspectMode": "cover",
            "aspectRatio": "1:3",
            "gravity": "top",
            "size": "full"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_latin_rock/png/jimeng_latin_rock%20(5).png",
            "aspectMode": "cover",
            "aspectRatio": "1:3",
            "gravity": "top",
            "size": "full"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_latin_rock/png/jimeng_latin_rock%20(6).png",
            "aspectMode": "cover",
            "aspectRatio": "1:3",
            "gravity": "top",
            "size": "full"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_latin_rock/png/jimeng_latin_rock%20(7).png",
            "aspectMode": "cover",
            "aspectRatio": "1:3",
            "gravity": "top",
            "size": "full"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_latin_rock/png/jimeng_latin_rock%20(8).png",
            "aspectMode": "cover",
            "aspectRatio": "1:3",
            "gravity": "top",
            "size": "full"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_latin_rock/png/jimeng_latin_rock%20(9).png",
            "aspectMode": "cover",
            "aspectRatio": "1:3",
            "gravity": "top",
            "size": "full"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_latin_rock/png/jimeng_latin_rock%20(10).png",
            "aspectMode": "cover",
            "aspectRatio": "1:3",
            "gravity": "top",
            "size": "full"
          }
        ],
        "paddingAll": "0px"
      }
    }
  ]
}
            line_flex_str = json.dumps(line_flex_json)
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
        elif text == 'f03':
            line_flex_json = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "15:22",
        "aspectMode": "fit",
        "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/product/p%20(1).png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "test test test",
            "wrap": True,
            "weight": "bold",
            "size": "xl",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://www.drhughes.com.tw/products/%E6%9F%91%E8%90%83%E4%BA%BA%E5%8F%83%E8%A4%87%E6%96%B9%E8%86%A0%E5%9B%8A-30%E7%B2%92%E7%BD%90%E8%A3%9D"
            }
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "test test test",
                "wrap": True,
                "weight": "bold",
                "size": "xl",
                "flex": 0
              },
              {
                "type": "text",
                "text": "test test test test ",
                "wrap": True,
                "weight": "bold",
                "size": "sm",
                "flex": 0
              }
            ]
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "15:22",
        "aspectMode": "fit",
        "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/product/p%20(2).png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "test test test",
            "wrap": True,
            "weight": "bold",
            "size": "xl",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://www.drhughes.com.tw/products/%E6%9F%91%E8%90%83%E4%BA%BA%E5%8F%83%E8%A4%87%E6%96%B9%E8%86%A0%E5%9B%8A-30%E7%B2%92%E7%BD%90%E8%A3%9D"
            }
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "test test test",
                "wrap": True,
                "weight": "bold",
                "size": "xl",
                "flex": 0
              },
              {
                "type": "text",
                "text": "test test test test ",
                "wrap": True,
                "weight": "bold",
                "size": "sm",
                "flex": 0
              }
            ]
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "15:22",
        "aspectMode": "fit",
        "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/product/p%20(3).png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "test test test",
            "wrap": True,
            "weight": "bold",
            "size": "xl",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://www.drhughes.com.tw/products/%E6%9F%91%E8%90%83%E4%BA%BA%E5%8F%83%E8%A4%87%E6%96%B9%E8%86%A0%E5%9B%8A-30%E7%B2%92%E7%BD%90%E8%A3%9D"
            }
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "test test test",
                "wrap": True,
                "weight": "bold",
                "size": "xl",
                "flex": 0
              },
              {
                "type": "text",
                "text": "test test test test ",
                "wrap": True,
                "weight": "bold",
                "size": "sm",
                "flex": 0
              }
            ]
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "15:22",
        "aspectMode": "fit",
        "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/product/p%20(4).png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "test test test",
            "wrap": True,
            "weight": "bold",
            "size": "xl",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://www.drhughes.com.tw/products/%E6%9F%91%E8%90%83%E4%BA%BA%E5%8F%83%E8%A4%87%E6%96%B9%E8%86%A0%E5%9B%8A-30%E7%B2%92%E7%BD%90%E8%A3%9D"
            }
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "test test test",
                "wrap": True,
                "weight": "bold",
                "size": "xl",
                "flex": 0
              },
              {
                "type": "text",
                "text": "test test test test ",
                "wrap": True,
                "weight": "bold",
                "size": "sm",
                "flex": 0
              }
            ]
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "15:22",
        "aspectMode": "fit",
        "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/product/p%20(5).png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "test test test",
            "wrap": True,
            "weight": "bold",
            "size": "xl",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://www.drhughes.com.tw/products/%E6%9F%91%E8%90%83%E4%BA%BA%E5%8F%83%E8%A4%87%E6%96%B9%E8%86%A0%E5%9B%8A-30%E7%B2%92%E7%BD%90%E8%A3%9D"
            }
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "test test test",
                "wrap": True,
                "weight": "bold",
                "size": "xl",
                "flex": 0
              },
              {
                "type": "text",
                "text": "test test test test ",
                "wrap": True,
                "weight": "bold",
                "size": "sm",
                "flex": 0
              }
            ]
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "15:22",
        "aspectMode": "fit",
        "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/product/p%20(6).png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "test test test",
            "wrap": True,
            "weight": "bold",
            "size": "xl",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://www.drhughes.com.tw/products/%E6%9F%91%E8%90%83%E4%BA%BA%E5%8F%83%E8%A4%87%E6%96%B9%E8%86%A0%E5%9B%8A-30%E7%B2%92%E7%BD%90%E8%A3%9D"
            }
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "test test test",
                "wrap": True,
                "weight": "bold",
                "size": "xl",
                "flex": 0
              },
              {
                "type": "text",
                "text": "test test test test ",
                "wrap": True,
                "weight": "bold",
                "size": "sm",
                "flex": 0
              }
            ]
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "15:22",
        "aspectMode": "fit",
        "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/product/p%20(7).png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "test test test",
            "wrap": True,
            "weight": "bold",
            "size": "xl",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://www.drhughes.com.tw/products/%E6%9F%91%E8%90%83%E4%BA%BA%E5%8F%83%E8%A4%87%E6%96%B9%E8%86%A0%E5%9B%8A-30%E7%B2%92%E7%BD%90%E8%A3%9D"
            }
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "test test test",
                "wrap": True,
                "weight": "bold",
                "size": "xl",
                "flex": 0
              },
              {
                "type": "text",
                "text": "test test test test ",
                "wrap": True,
                "weight": "bold",
                "size": "sm",
                "flex": 0
              }
            ]
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "15:22",
        "aspectMode": "fit",
        "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/product/p%20(8).png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "test test test",
            "wrap": True,
            "weight": "bold",
            "size": "xl",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://www.drhughes.com.tw/products/%E6%9F%91%E8%90%83%E4%BA%BA%E5%8F%83%E8%A4%87%E6%96%B9%E8%86%A0%E5%9B%8A-30%E7%B2%92%E7%BD%90%E8%A3%9D"
            }
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "test test test",
                "wrap": True,
                "weight": "bold",
                "size": "xl",
                "flex": 0
              },
              {
                "type": "text",
                "text": "test test test test ",
                "wrap": True,
                "weight": "bold",
                "size": "sm",
                "flex": 0
              }
            ]
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "15:22",
        "aspectMode": "fit",
        "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/product/p%20(9).png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "test test test",
            "wrap": True,
            "weight": "bold",
            "size": "xl",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://www.drhughes.com.tw/products/%E6%9F%91%E8%90%83%E4%BA%BA%E5%8F%83%E8%A4%87%E6%96%B9%E8%86%A0%E5%9B%8A-30%E7%B2%92%E7%BD%90%E8%A3%9D"
            }
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "test test test",
                "wrap": True,
                "weight": "bold",
                "size": "xl",
                "flex": 0
              },
              {
                "type": "text",
                "text": "test test test test ",
                "wrap": True,
                "weight": "bold",
                "size": "sm",
                "flex": 0
              }
            ]
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "15:22",
        "aspectMode": "fit",
        "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/product/p%20(10).png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "test test test",
            "wrap": True,
            "weight": "bold",
            "size": "xl",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://www.drhughes.com.tw/products/%E6%9F%91%E8%90%83%E4%BA%BA%E5%8F%83%E8%A4%87%E6%96%B9%E8%86%A0%E5%9B%8A-30%E7%B2%92%E7%BD%90%E8%A3%9D"
            }
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "test test test",
                "wrap": True,
                "weight": "bold",
                "size": "xl",
                "flex": 0
              },
              {
                "type": "text",
                "text": "test test test test ",
                "wrap": True,
                "weight": "bold",
                "size": "sm",
                "flex": 0
              }
            ]
          }
        ]
      }
    }
  ]
}
            line_flex_str = json.dumps(line_flex_json)
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
        elif text == 'f04':
            line_flex_json = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_cowgirl/png/jimeng_cowgirl%20(1).png",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1:3"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Brown Cafe",
            "weight": "bold",
            "size": "sm",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "text",
                "text": "5.0",
                "size": "xs",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "test test ",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_cowgirl/png/jimeng_cowgirl%20(2).png",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1:3"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Brown Cafe",
            "weight": "bold",
            "size": "sm",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "text",
                "text": "5.0",
                "size": "xs",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "test test ",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_cowgirl/png/jimeng_cowgirl%20(3).png",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1:3"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Brown Cafe",
            "weight": "bold",
            "size": "sm",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "text",
                "text": "5.0",
                "size": "xs",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "test test ",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_cowgirl/png/jimeng_cowgirl%20(4).png",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1:3"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Brown Cafe",
            "weight": "bold",
            "size": "sm",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "text",
                "text": "5.0",
                "size": "xs",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "test test ",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_cowgirl/png/jimeng_cowgirl%20(5).png",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1:3"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Brown Cafe",
            "weight": "bold",
            "size": "sm",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "text",
                "text": "5.0",
                "size": "xs",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "test test ",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_cowgirl/png/jimeng_cowgirl%20(6).png",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1:3"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Brown Cafe",
            "weight": "bold",
            "size": "sm",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "text",
                "text": "5.0",
                "size": "xs",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "test test ",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_cowgirl/png/jimeng_cowgirl%20(7).png",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1:3"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Brown Cafe",
            "weight": "bold",
            "size": "sm",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "text",
                "text": "5.0",
                "size": "xs",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "test test ",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_cowgirl/png/jimeng_cowgirl%20(8).png",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1:3"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Brown Cafe",
            "weight": "bold",
            "size": "sm",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "text",
                "text": "5.0",
                "size": "xs",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "test test ",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_cowgirl/png/jimeng_cowgirl%20(9).png",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1:3"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Brown Cafe",
            "weight": "bold",
            "size": "sm",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "text",
                "text": "5.0",
                "size": "xs",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "test test ",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_cowgirl/png/jimeng_cowgirl%20(10).png",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1:3"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Brown Cafe",
            "weight": "bold",
            "size": "sm",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "text",
                "text": "5.0",
                "size": "xs",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "test test ",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    }
  ]
}
            line_flex_str = json.dumps(line_flex_json)
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
        elif text == 'f05':
            line_flex_json = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_age_of_discovery/png/jimeng_age_of_discovery%20(1).png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://linecorp.com/"
            }
          },
          {
            "type": "image",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_age_of_discovery/png/jimeng_age_of_discovery%20(2).png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://linecorp.com/"
            }
          },
          {
            "type": "image",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_age_of_discovery/png/jimeng_age_of_discovery%20(3).png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://linecorp.com/"
            }
          },
          {
            "type": "image",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_age_of_discovery/png/jimeng_age_of_discovery%20(4).png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://linecorp.com/"
            }
          },
          {
            "type": "image",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_age_of_discovery/png/jimeng_age_of_discovery%20(5).png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://linecorp.com/"
            }
          },
          {
            "type": "image",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_age_of_discovery/png/jimeng_age_of_discovery%20(6).png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://linecorp.com/"
            }
          },
          {
            "type": "image",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_age_of_discovery/png/jimeng_age_of_discovery%20(7).png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://linecorp.com/"
            }
          },
          {
            "type": "image",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_age_of_discovery/png/jimeng_age_of_discovery%20(8).png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://linecorp.com/"
            }
          },
          {
            "type": "image",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_age_of_discovery/png/jimeng_age_of_discovery%20(9).png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://linecorp.com/"
            }
          },
          {
            "type": "image",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_age_of_discovery/png/jimeng_age_of_discovery%20(10).png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://linecorp.com/"
            }
          },
          {
            "type": "image",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png"
          }
        ],
        "paddingAll": "0px"
      }
    }
  ]
}
            line_flex_str = json.dumps(line_flex_json)
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[FlexMessage(alt_text='詳細說明', contents=FlexContainer.from_json(line_flex_str))]
                )
            )
            

        else:
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text=event.message.text)]
                )
            )

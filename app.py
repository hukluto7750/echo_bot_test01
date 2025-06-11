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
        if text == 'f01':
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
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_latin_rock/jpg/jimeng_latin_rock%20(1).jpg",
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
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_latin_rock/png/jimeng_latin_rock%20(2).png",
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
                    "text": "類黃酮是什麼？",
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
                    "text": "類黃酮的功效、常見的10種食物一次看",
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
                        "offsetTop": "-2px",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "https://www.drhughes.com.tw/blog/posts/what-is-flavonoids"
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
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_latin_rock/png/jimeng_latin_rock%20(3).png",
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
                    "text": "女性保健食品推薦",
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
                    "text": "一篇文認識各年齡層推薦食品、挑選6重點",
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
                        "offsetTop": "-2px",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "https://www.drhughes.com.tw/blog/posts/how-to-choose-supplement-for-women"
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
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_latin_rock/png/jimeng_latin_rock%20(4).png",
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
                    "text": "提升身心舒緩的雙重利器",
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
                    "text": "GABA 與香蜂草的科學魅力",
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
                        "offsetTop": "-2px",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "https://www.drhughes.com.tw/blog/posts/fibersol-12182403"
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
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_latin_rock/png/jimeng_latin_rock%20(5).png",
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
                    "text": "克菲爾益生菌",
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
                    "text": "腸道健康的天然守護者",
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
                        "offsetTop": "-2px",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "https://www.drhughes.com.tw/blog/posts/fibersol-12182402"
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
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_latin_rock/png/jimeng_latin_rock%20(6).png",
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
                    "text": "瘦身與代謝提升",
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
                    "text": "健康管理的新方向",
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
                        "offsetTop": "-2px",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "https://www.drhughes.com.tw/blog/posts?page=1&sort_by=&order_by=&limit=10"
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
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_latin_rock/png/jimeng_latin_rock%20(7).png",
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
                    "text": "非洲芒果籽",
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
                    "text": "減重與健康管理的新寵",
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
                        "offsetTop": "-2px",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "https://www.drhughes.com.tw/blog/posts/ams-12182401"
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
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_latin_rock/png/jimeng_latin_rock%20(8).png",
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
                    "text": "摩洛血橙",
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
                    "text": "天然健康的紅寶石，你知道它的秘密嗎？",
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
                        "offsetTop": "-2px",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "https://www.drhughes.com.tw/blog/posts/mbo-12182401"
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
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_latin_rock/png/jimeng_latin_rock%20(9).png",
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
                    "text": "膠原蛋白吃再多也沒用？",
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
                    "text": "你得學會鎖住它！",
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
                        "offsetTop": "-2px",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "https://www.drhughes.com.tw/blog/posts/collagen-12022406"
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
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_latin_rock/jpg/jimeng_latin_rock%20(16).jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
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
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_bookroom/jpg/jimeng_bookroom%20(34).jpg",
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
                          "uri": "https://liff.line.me/2007523880-zq4NyMgK"
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
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_bookroom/png/jimeng_bookroom%20(35).png",
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
                    "text": "吃膠原蛋白不等於直接補！",
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
                    "text": "揭開膠原蛋白轉化與生成的秘密",
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
                        "offsetTop": "-2px",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "https://www.drhughes.com.tw/blog/posts/collagen-12022405"
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
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_bookroom/png/jimeng_bookroom%20(36).png",
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
                    "text": "吃膠原蛋白真的有效嗎？",
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
                    "text": "科學揭秘與正確吃法大公開",
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
                        "offsetTop": "-2px",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "https://www.drhughes.com.tw/blog/posts/collagen-12022404"
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
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_bookroom/png/jimeng_bookroom%20(37).png",
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
                    "text": "膠原蛋白與金雀異黃酮",
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
                    "text": "雙重守護青春與健康的完美結合",
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
                        "offsetTop": "-2px",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "https://www.drhughes.com.tw/blog/posts/collagen-12022403"
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
                "contents": [
                  {
                    "type": "text",
                    "text": "膠原蛋白流失速度與生成機制",
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
                    "text": "了解快速老化的根本原因",
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
                        "offsetTop": "-2px",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "https://www.drhughes.com.tw/blog/posts/collagen-12022402"
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
                    "text": "膠原蛋白攝取與生成機制",
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
                    "text": "科學解析與分子大小的重要性",
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
                        "offsetTop": "-2px",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "https://www.drhughes.com.tw/blog/posts/collagen-12022401"
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
                    "text": "天然降低尿酸的科學解方",
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
                    "text": "木犀草素的抗炎與健康功效",
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
                        "offsetTop": "-2px",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "https://www.drhughes.com.tw/blog/posts/luteolin-12022403"
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
                    "text": "專注力不足？",
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
                    "text": "木犀草素幫你找回專注狀態",
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
                        "offsetTop": "-2px",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "https://www.drhughes.com.tw/blog/posts/luteolin-12022404"
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
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_bookroom/png/jimeng_bookroom%20(42).png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
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
            "url": "https://raw.githubusercontent.com/hukluto7750/echo_bot_test01/refs/heads/main/imgs/jimeng_bookroom/jpg/jimeng_bookroom%20(43).jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
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

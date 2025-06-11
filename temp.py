elif text == 'f03':
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
        elif text == 'f04':
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
        elif text == 'f05':
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
      

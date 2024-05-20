from flask import Flask, request, abort
import stock_crawler as sc
from linebot.v3 import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
)
from linebot.v3.webhooks import MessageEvent, TextMessageContent
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from pyngrok import ngrok


app = Flask(__name__)
port = "5000"
public_url = ngrok.connect(port).public_url
print(f' * ngrok tunnel "{public_url}" -> "http://127.0.0.1:{port}" ')

configuration = Configuration(
    access_token="sd9Xz63Sn4wRF3JqThEPonlSKWaAPANWLsCJtKmjCjSyWG32tLF01b2Y8e8xPUlnPSCu8CXdhfF+Kb1r7nss0Ylr4AJzr+SN1AOsPVq99b4akIwSmRYQ1O18LrrW2j7/ragqkMU4XecWc7ujW6YhFQdB04t89/1O/w1cDnyilFU="
)
handler = WebhookHandler("63e67dadabb0bc8dca15e9e2a5b1231c")


@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info(
            "Invalid signature. Please check your channel access token/channel secret."
        )
        abort(400)

    return "OK"


# @handler.add(MessageEvent, message=TextMessageContent)
# def handle_message(event):
#     with ApiClient(configuration) as api_client:
#         line_bot_api = MessagingApi(api_client)
#         line_bot_api.reply_message_with_http_info(
#             ReplyMessageRequest(
#                 reply_token=event.reply_token,
#                 messages=[TextMessage(text=event.message.text)],
#             )
#         )


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    if "股票" in text:
        # 假設你有一個函數叫 get_stock_info(symbol)
        stock_info = sc.get_2330_info("2330")  # 這裡可以根據text內容動態決定股票代碼
        reply_text = f"股票資訊：\n{stock_info}"
    else:
        reply_text = "請輸入股票相關問題。"

    LineBotApi.reply_message(event.reply_token, TextSendMessage(text=reply_text))


if __name__ == "__main__":
    app.run()

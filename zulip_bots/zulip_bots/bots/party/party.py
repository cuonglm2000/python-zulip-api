from typing import Any, Dict
 
from zulip_bots.lib import AbstractBotHandler
import logging
 
class PartyHandler:
    def usage(self) -> str:
        return """
        This bot is made for those that miss
        """
 
    def handle_message(self, message: Dict[str, Any], bot_handler: AbstractBotHandler) -> None:
        self.handle_input(message, bot_handler)
 
    def handle_input(self, message: Dict[str, Any], bot_handler: AbstractBotHandler) -> None:
        original_content = message["content"]
        message_content = original_content.strip().lower()

        if 'quẩy' in message_content.split():
            reply_message = "Quẩy lên!!! [ANH EM ƠI](https://media.giphy.com/media/5jT0jaNDsM6Ik7X9yq/giphy.gif)"
            emoji_name = "tada"
        elif 'thương' in message_content.split():
            reply_message = "Thương thương lại thích thích [TIM TIM](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExemxkZ29pZWZmaGR1cjE1N2p2ajYzcXBkNjR3MnZyMnJwYW94OWxjMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/6p26sp0YT2LAI/giphy.gif)"
            emoji_name = "heart_eyes"
        elif 'cầu' in message_content.split():
            reply_message = "Cầu vồng [Xanh đỏ](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExeWZnYjZwczFsZDB5dnlqZzBydTJ2a3FuZHZsMXlpanZidnF1aGpxbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26gsdnFwRgz36WPhC/giphy.gif)"
            emoji_name = "rainbow"
        elif 'code' in message_content.split():
            reply_message = "Code lên code xuống [CODE](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWo0Z2YxaTJ0NXJ1eTBiZ2xiOGJucDBvZWJxNGNkZnhxd2drM2d2MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/EZr27ZbJwmjE9PGyLN/giphy.gif)"
            emoji_name = "code"
        elif 'nổ' in message_content.split():
            reply_message = "Nổ vừa thôi bạn ơi [BÙM](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExa2hkM2NpYzhpMmhwMzU4c25sOWo5cTMxd3Q1OXk5aDFtaXluZG5scyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qwGcDfEAGdJWmuSnwh/giphy.gif)"
            emoji_name = "bomb"
        elif 'cảm ơn' in message_content.split():
            reply_message = "Nừn ná na na, nừn ná na na,... [CẢM ƠN ANH](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnp0aWMyNDdpajRoMW5hc2o0d3V1d3A2dWp2Z2FqbTdvcjZsaW80ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/f1JaQyF57OgpO/giphy.gif)"
            emoji_name = "heart_eyes"
        else:
            reply_message = "Bạn là điều tuyệt với nhất, điều tuyệt vời mà tôi đánh mất :heart_exclamation: "
            emoji_name = "-1"


        logging.info(f"Reply message: {reply_message}")
        bot_handler.send_reply(message, reply_message)
        bot_handler.react(message, emoji_name)
handler_class = PartyHandler
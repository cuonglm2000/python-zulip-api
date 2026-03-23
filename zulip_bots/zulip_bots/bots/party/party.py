from typing import Any, Dict
 
from zulip_bots.lib import BotHandler
 
 
class PartyHandler:
    def usage(self) -> str:
        return """
        This bot is made for those that miss
        Discord Party-Mode
        """
 
    def handle_message(self, message: Dict[str, Any], bot_handler: BotHandler) -> None:
        self.handle_input(message, bot_handler)
 
    def handle_input(self, message: Dict[str, Any], bot_handler: BotHandler) -> None:
        original_content = message["content"]
        message_content = original_content.strip().lower()
        reply_message = "Party Time!!! [Confetti](https://media.giphy.com/media/5jT0jaNDsM6Ik7X9yq/giphy.gif)"
        emoji_name = "tada"
        if 'party' in message_content.split():
            bot_handler.send_reply(message, reply_message)
            bot_handler.react(message, emoji_name)
        else: 
          bot_handler.send_reply(message, "why don't you like to party??")
          bot_handler.react(message, "-1")
 
handler_class = PartyHandler
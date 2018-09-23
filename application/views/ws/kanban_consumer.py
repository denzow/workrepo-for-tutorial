from channels.generic.websocket import JsonWebsocketConsumer


class KanbanConsumer(JsonWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 自身に一意なIDを付与する
        self.consumer_id = id(self)
        # 後で使う
        self.user = None

    def connect(self):
        print(self.scope['user'])
        # 認証チェック
        if not self.scope['user'].is_authenticated:
            self.close()
            return

        self.user = self.scope['user']
        # 接続を受け入れる
        self.accept()

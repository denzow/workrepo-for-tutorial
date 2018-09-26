from channels.generic.websocket import JsonWebsocketConsumer

from modules.kanban import service as kanban_sv


class KanbanConsumer(JsonWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 自身に一意なIDを付与する
        self.consumer_id = id(self)
        # 後で使う
        self.user = None
        self.board_id = None
        self.namespace = 'board'

    def connect(self):
        # 認証チェック
        if not self.scope['user'].is_authenticated:
            self.close()
            return

        self.user = self.scope['user']
        self.board_id = self.scope['url_route']['kwargs']['board_id']
        # 接続を受け入れる
        self.accept()

        self.send_board_data()

    def send_board_data(self):
        board_data = kanban_sv.get_board_data_by_board_id(self.board_id)
        self.send_json({
            'boardData': board_data,
            'mutation': 'setBoardData',
            'namespace': self.namespace,
        })


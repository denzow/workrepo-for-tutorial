import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import View

from modules.kanban import service as kanban_sv


@method_decorator(csrf_exempt, name='dispatch')
class BoardListApi(View):

    def get(self, request):
        """
        ボードの一覧を戻す
        """
        board_list = []
        for board in kanban_sv.get_board_list_by_owner(request.user):
            board_list.append({
                'id': board.id,
                'name': board.name,
            })
        return JsonResponse({
            'board_list': board_list,
        })

    def post(self, request):
        """
        新しいボードを追加する
        """
        data = json.loads(request.body)
        board_name = data.get('boardName')
        board = kanban_sv.add_board(
            owner=request.user,
            board_name=board_name
        )
        return JsonResponse({
            'board_data': {
                'id': board.id,
                'name': board.name,
            }
        })
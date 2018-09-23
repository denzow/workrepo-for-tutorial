from .models import Board, Card, PipeLine


def get_board_list_by_owner(owner):
    return Board.get_list_by_owner(owner=owner)


def add_board(owner, board_name):
    """
    :param User owner:
    :param str board_name:
    :return:
    """
    board = Board.objects.create(
        owner=owner,
        name=board_name
    )
    return board


def get_board_data_by_board_id(board_id):
    """
    borad and pipeline and card.
    :param int board_id:
    :return:
    :rtype: dict
    """
    # ボード取得
    board = Board.get_by_id(board_id)
    board_data = {
        'board_id': board.id,
        'name': board.name,
        'pipe_line_list': []
    }
    # ボードに紐づく各パイプライン取得
    for pipe_line in PipeLine.get_list_by_board(board):
        pipe_line_data = {
            'pipe_line_id': pipe_line.id,
            'name': pipe_line.name,
            'card_list': []
        }
        # パイプラインに紐づくカードを取得
        for card in Card.get_list_by_pipe_line(pipe_line):
            pipe_line_data['card_list'].append({
                'card_id': card.id,
                'title': card.title,
                'content': card.content,
            })
        board_data['pipe_line_list'].append(pipe_line_data)

    return board_data

from .models import Board


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

from .models import Board


def get_board_list_by_owner(owner):
    return Board.get_list_by_owner(owner=owner)

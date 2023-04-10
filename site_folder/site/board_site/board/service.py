from board.models import *
from common.service import *


def get_all_objects(model):
    return all_objects(model)

"""Этот сервис добаляет в таблиу запись
, которая ссылается на пользователя"""
def user_upload_connect(user, form_data):
    object_ = UserProfileUploads(user=user, product=form_data)
    object_.save()


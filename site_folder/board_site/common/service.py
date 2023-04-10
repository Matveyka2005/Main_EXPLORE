def all_objects(model):
    return model.objects.all()


# def get_object(model, *args):
#     return model.objects.get(args)


def order_objects(model, *args):
    return model.objects.order_by(args)


def filter_objects(model, **kwargs):
    return model.objects.filter(kwargs)

def t():
    try:
        from celery import current_task
        if current_task is not None:
            from celery.contrib import rdb
            rdb.set_trace()
            return
    except ImportError:
        pass
    import pdb
    pdb.set_trace()

t()


class SchoolRouter(object):
    default_db = 'default'
    def allow_syncdb(self, db, model):
        if db == 'default':
            return model._meta.app_label == 'app'
        elif model._meta.app_label == 'school':
            return True
        else:
            return False
        return None
    
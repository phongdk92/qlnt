from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

from objectpermission.models import ObjectPermission

class ObjectPermissionBackend(object):
    supports_object_permissions = True
    supports_anonymous_user = False

    def authenticate(self, username, password):
        return None

    def has_perm(self, user_obj, perm, model=None):
        """ perm parameter must has value like:
        permission_field=value
        Eg: change_level=S
        """
        if value is None:
            return False

        if user_obj.is_superuser:
            return True

        try:
            permission = perm.split('_')[0]
            field_name = "_".join(perm.split('_')[1:]).split('=')[0]
            value = "=".join("_".join(s.split('_')[1:]).split('=')[1:])
        except IndexError:
            return False

        # check for user permission
        user_ct = ContentType.get_for_model(user_obj)
        model_ct = ContentType.get_for_model(model_ct)
        user_perm = ObjectPermission.objects.filter(owner_id=user_obj.id,
                                                    owner_ct=user_ct,
                                                    model_ct=model_ct,
                                                    field_name=field_name,
                                                    allowed_value=value)
        if user_perm.filter(**{'permission': permission}).exists():
            return True

        # check for group permission
        for g in user_obj.groups():
            group_ct = ContentType.get_for_model(g)
            group_perm = ObjectPermission.objects.filter(owner_id=g.id,
                                                    owner_ct=group_ct,
                                                    model_ct=model_ct,
                                                    field_name=field_name,
                                                    allowed_value=value)
            if group_perm.filter(**{'permission': permission}).exists():
                return True

        return False

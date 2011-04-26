from django.contrib import admin
from school.models import School, Class, Teacher, Pupil, Mark, Subject, Term,Year,StartYear,KhenThuong,KiLuat,HanhKiem,TBHocKy,TBNam,DiemDanh,TKDiemDanh,Block,TKMon

class MultiDBModelAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = 'Mark_1'

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'Mark_1' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'Mark_1' database
        obj.delete(using=self.using)

    def queryset(self, request):
        # Tell Django to look for objects on the 'Mark_1' database.
        return super(MultiDBModelAdmin, self).queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'Mark_1' database.
        return super(MultiDBModelAdmin, self).formfield_for_foreignkey(db_field, request=request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'Mark_1' database.
        return super(MultiDBModelAdmin, self).formfield_for_manytomany(db_field, request=request, using=self.using, **kwargs)

admin.site.register(School)
admin.site.register(Block)
admin.site.register(Class)
admin.site.register(Teacher)
admin.site.register(Pupil)
admin.site.register(Mark)
admin.site.register(Subject)
admin.site.register(Term)
admin.site.register(Year)
admin.site.register(StartYear)
admin.site.register(KhenThuong)
admin.site.register(KiLuat)
admin.site.register(HanhKiem)
admin.site.register(TBHocKy)
admin.site.register(TBNam)
admin.site.register(DiemDanh)
admin.site.register(TKDiemDanh)
admin.site.register(TKMon)


from django.conf.urls.defaults import patterns, url 


urlpatterns = patterns('',
	url(r'^$', 'school.views.school_index'),
	url(r'mark_table/(?P<class_id>\w+)','school.views1.mark_table'),
	url(r'markForAStudent/(?P<class_id>\w+)/(?P<student_id>\w+)','school.views1.markForAStudent'),
	# diem cho 1 mon
	url(r'markForASubject/(?P<subject_id>\w+)','school.views1.markForASubject'),
	# xep loai hoc luc theo lop, gom co xep loai k1, k2 va ca nam
	url(r'xepLoaiHlTheoLop/(?P<class_id>\w+)','school.views1.xepLoaiHlTheoLop'),	
	url(r'xlCaNamTheoLop/(?P<class_id>\w+)','school.views1.xlCaNamTheoLop'),	

	# tinh diem tong ket cua hoc ky va tinh hoc luc cua tat ca hoc sinh trong toan truong theo hoc ky
	url(r'finishTerm/(?P<term_id>\w+)','school.views1.finishTerm'),

	# tinh diem tong ket cua hoc ky va tinh hoc luc cuoi nam 
	url(r'finishYear/(?P<year_id>\w+)','school.views1.finishYear'),
	
    url(r'classes$', 'school.views.classes'),
    url(r'teachers$', 'school.views.teachers'),
    url(r'students$', 'school.views.students'),
    url(r'viewClassDetail/(?P<class_id>\w+)', 'school.views.viewClassDetail'),
    url(r'viewTeacherDetail/(?P<teacher_id>\w+)$', 'school.views.viewTeacherDetail'),
    url(r'viewStudentDetail/(?P<student_id>\w+)', 'school.views.viewStudentDetail'),
    url(r'studentPerClass/(?P<class_id>\w+)', 'school.views.studentPerClass'),
    url(r'subjectPerClass/(?P<class_id>\w+)', 'school.views.subjectPerClass'),
	#url(r'viewSubjectDetail/(?P<subject_id>\w+)', 'school.views.viewSubjectDetail'),
    url(r'start_year$','school.views.b1', name = "start_year"),
    url(r'diemdanh/(?P<class_id>\w+)/(?P<day>\w+)/(?P<month>\w+)/(?P<year>\w+)', 'school.views.diem_danh'),
    url(r'diemdanh/(?P<class_id>\w+)', 'school.views.time_select'),
    url(r'diemdanhhs/(?P<student_id>\w+)', 'school.views.diem_danh_hs'),    
    url(r'start_year/import$', 'school.views.nhap_danh_sach_trung_tuyen'),
    url(r'start_year/import/list$', 'school.views.danh_sach_trung_tuyen', name = "imported_list"),
    url(r'start_year/manual$', 'school.views.manual_adding', name = "manual_adding"),
    url(r'deleteTeacher/(?P<teacher_id>\w+)', 'school.views.deleteTeacher'),
    url(r'deleteSubject/(?P<subject_id>\w+)', 'school.views.deleteSubject'),
    url(r'deleteStudentInSchool/(?P<student_id>\w+)', 'school.views.deleteStudentInSchool'),
    url(r'deleteStudentInClass/(?P<student_id>\w+)', 'school.views.deleteStudentInClass'),
    url(r'deleteClass/(?P<class_id>\w+)', 'school.views.deleteClass'),
    #url(r'^school/test$','school.views.test'), 
	
	)

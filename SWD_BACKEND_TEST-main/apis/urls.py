
from django.urls import path
from apis.views import schools

urlpatterns = [

    # ========== API Endpoints ==================================+++++++++++++++=======================================
    path("student_score/", schools.StudentSubjectsScoreAPIView.as_view(), name="student_score"),
    path("student_score/<int:id>/", schools.StudentSubjectsScoreDetailsAPIView.as_view(), name="student_score_details"),

    path("personnel_details/<str:school_title>/", schools.PersonnelDetailsAPIView.as_view(), name="personnel_details"),
    path("school_hierarchy/", schools.SchoolHierarchyAPIView.as_view(), name="school_hierarchy"),
    path("school_structure/", schools.SchoolStructureAPIView.as_view(), name="school_structure"),

]

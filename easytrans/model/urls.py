from django.urls import path

urlpatterns = [
    path('modelcategory', ),  #  支持列表  永远不支持用户新增
    path('model', ),  # 支持列表，暂不支持用户新增
    path('modeldetail/<int:id>/', )  # 只支持查， 暂不支持用户改，删
]


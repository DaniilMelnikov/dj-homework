from django.urls import path
from measurement.views import SensorAdd, SensorUpdate, MeasurementAdd, SensorViewShort, SensorView, SensorUpdate_name, SensorUpdate_description

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensoradd/', SensorAdd.as_view()),
    path('update/<name>/', SensorUpdate_name.as_view()),
    path('update/<description>/', SensorUpdate_description.as_view()),
    path('update/<name>/<description>/', SensorUpdate.as_view()),
    path('measurementadd/', MeasurementAdd.as_view()),
    path('shortview/', SensorViewShort.as_view()),
    path('view/<pk>/', SensorView.as_view())
]

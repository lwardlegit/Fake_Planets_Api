"# Fake_Planets_Api"


    path('planets', views.planets) => Ex: http://localhost:8000/planets
    path('addplanet', views.add_planet)  Ex: http://localhost:8000/addplanet
    path('<str:planet_name>', views.get_planet) Ex: http://localhost:8000/<planet_name>

from django.urls import path, include
from rest_framework import routers

from cinema.views import (MovieViewSet,
                          MoviSessionViewSet,
                          GenreViewSet,
                          ActorViewSet,
                          CinemaHallViewSet)


app_name = "cinema"

router = routers.DefaultRouter()

router.register("movies", MovieViewSet)
router.register("movie_sessions", MoviSessionViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)
urlpatterns = router.urls

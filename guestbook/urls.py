from django.contrib import admin
from django.urls import path, reverse_lazy
from django.views.generic import RedirectView
from django.views.decorators.csrf import csrf_exempt
from entries.views import (
    CreateEntryView,
    LatestEntryView,
    LikeEntryView,
    TopEntriesView,
)

urlpatterns = [
    path("", RedirectView.as_view(url=reverse_lazy("latest_entries"))),
    path("entries/", LatestEntryView.as_view(), name="latest_entries"),
    path("entries/top", TopEntriesView.as_view(), name="top_entries"),
    path("entries/new", CreateEntryView.as_view(), name="create_entry"),
    path(
        "entries/<int:id>/like", csrf_exempt(LikeEntryView.as_view()), name="like_entry"
    ),
    path("admin/", admin.site.urls),
]

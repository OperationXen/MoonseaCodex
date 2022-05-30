from rest_framework.routers import DefaultRouter
from django.views.decorators.csrf import csrf_exempt

from codex.views.data.character import CharacterViewSet
from codex.views.data.items import MagicItemViewSet
from codex.views.data.dungeonmaster import DMLogViewSet

from codex.views.events.dm_rewards import DMRewardViewSet
from codex.views.events.dm_games import DMGamesViewSet


router = DefaultRouter()
router.register(r'character', CharacterViewSet, basename='character')
router.register(r'magicitem', MagicItemViewSet, basename='magicitem')
router.register(r'dm_log', DMLogViewSet, basename='dm_log')
router.register(r'dm_reward', DMRewardViewSet, basename='dm_reward')
router.register(r'dm_game', DMGamesViewSet, basename='dm_game')

urlpatterns = router.urls

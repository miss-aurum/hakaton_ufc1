from rest_framework import routers
from app_ufc.views import * 
from info_futurefees_app.views import *
from shop_ufc_app.views import *




router = routers.SimpleRouter()
router.register('sportman', SportmanViewset)
router.register('trainer', TrainerViewset)
router.register('news', NewsViewset)
router.register('socialMedia', SocialMediaViewset)
router.register('contact', ContactViewset)
router.register('turnir', TurnirViewset)
router.register('peopleTurnir', PeopleTurnirViewset)
router.register('futurefees',FutureFeesViewset)
router.register('pastfees', PastFeesViewset)
router.register('product', ProductViewset)
router.register('order', OrderViewset)







urlpatterns = []
urlpatterns  += router.urls


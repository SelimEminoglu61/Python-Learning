"""

burda modules ten fonk ları cagırıp kullanıcaz.

2 yolu var ilki:
"""
import modules

# ve o fonk için cagırmayı söyle yaparız

modules.whatsup()
print(modules.mutlak(23))

# 2. yol ise # bana göre daha basit ama tehlikesi var
# tehlikesi 2 sayfa ve ikisi de aynı fonka sahipse python hangisinden alacagını sasırır.
# diğeri daha kesin yoldur.
from modules import *  # yıldız butun fonkları al anlamında
# bu yolun avantajı ise 1 dosyadan sadece 1 fonku almamız gerekirse bu yontemle yaparız.
from modules import mutlak # sadece mutlak fonku alındı.

#fonksıyon cagırması ıse
print(mutlak(-34))
whatsup()

# hazır kutuphaneler mevcut mesela import math diyip math kutuphanesine erişim olabilir.
"""

içini gormek için math kutuphanesinin önce cmd veya ıde den python yazıp
sonra import math diyip
en son dir(math) ile içindeki fonkları görebiliriz

"""
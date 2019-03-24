import mlab
from bike import Bike

mlab.connect()

b = Bike(model="honda air blade",daily_fee="60000000",image="https://nhattao.cdnforo.com/attachment-files/2017/12/9663608_4de20a541c32f36caa23.jpg",year="2012")
b .save()

# b_objects = Bike.objects()
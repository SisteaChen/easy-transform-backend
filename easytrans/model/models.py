from django.db import models

# class ModelDeal(models.Model):
#     # 用户 模型，同时有状态 waiting  running  done  fail
#     # 如果执行中报错则记为fail
#     status = models.CharField(max_length=20, choices=, default="waiting")
#     date = models.DateTimeField(auto_now_add=True) # 创建时的时间
#     user =
#     model =
#     data = 需要搭建一个专门的图片和视频服务器
#     result =
#     params = {dict} {json}
#
#     def __str__(self):


class ModelCategory(models.Model):
    type = models.CharField(max_length=10)  # e.g.  image

    def __str__(self):
        return str(self.type)

class Model(models.Model):
    # 算法的名字 如basicVSR、DBPN等
    name = models.CharField(max_length=120)
    # 模型的类别，如视频超分辨
    largecategory = models.ForeignKey(ModelCategory, on_delete=models.CASCADE)
    smallcategory = models.CharField(max_length=50)  # 所属领域，如图像超分辨

    def __str__(self):
        return str(self.largecategory) + "_" + str(self.smallcategory) + "_" + str(self.name)

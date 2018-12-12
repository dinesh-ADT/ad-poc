from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
    	return self.name

class UserToken(models.Model):
	member = models.ForeignKey(Member, on_delete=models.CASCADE)
	access_code = models.CharField(max_length=356)
	access_token = models.CharField(max_length=356)
	refresh_token = models.CharField(max_length=356)
	device_id = models.CharField(max_length=30)

	def __str__(self):
		return self.device_id
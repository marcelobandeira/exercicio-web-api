# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Geo(models.Model):
	lat = models.FloatField()
	lng = models.FloatField()

class Address(models.Model):
	street = models.CharField(max_length=150)
	suite = models.CharField(max_length=150)
	city = models.CharField(max_length=150)
	zipcode = models.CharField(max_length=150)
	geo = models.ForeignKey(Geo, related_name='enderecos')

class User(models.Model):
	username = models.CharField(max_length=150)
	name = models.CharField(max_length=150)
	email = models.CharField(max_length=150)
	address = models.ForeignKey(Address, related_name='users')

class Post(models.Model):
	body = models.CharField(max_length=500)
	title = models.CharField(max_length=300)
	user = models.ForeignKey(User, related_name='posts')

class Comment(models.Model):
	body = models.CharField(max_length=300)
	email = models.CharField(max_length=300)
	name = models.CharField(max_length=300)
	post = models.ForeignKey(Post, related_name='comments')

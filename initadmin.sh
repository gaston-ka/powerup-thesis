#!/usr/bin/env python

from django.contrib.auth.models import User

User.objects.create_superuser('sam@gmail.com', 'Sam', 'Seneza', '0784578965', 'root1213456')

from django.contrib.auth.models import User
from .models import Leaf
from rest_framework import status
from rest_framework.test import APITestCase


class LeafListViewTests(APITestCase):
  def setUp(self):
    User.objects.create_user(username='joe', password='bloggs')

  def test_can_list_leaves(self):
    joe = User.objects.get(username='joe')
    Leaf.objects.create(user=joe, memory='test memory')
    response = self.client.get('/leaves/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_logged_in_user_can_create_leaf(self):
    self.client.login(username='joe', password='bloggs')
    response = self.client.post('/leaves/', {'memory': 'test memory'})
    count = Leaf.objects.count()
    self.assertEqual(count, 1)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
  
  def test_user_not_logged_in_cant_create_leaf(self):
    response = self.client.post('/leaves/', {'memory': 'test memory'})
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class LeafDetailViewTests(APITestCase):
  def setUp(self):
    joe = User.objects.create_user(username='joe', password='bloggs')
    jane = User.objects.create_user(username='jane', password='doe')
    Leaf.objects.create(
        user=joe, memory='joes test memory'
    )
    Leaf.objects.create(
        user=jane, memory='janes test memory'
    )

  def test_can_retrieve_leaf_using_valid_id(self):
    response = self.client.get('/leaves/1/')
    self.assertEqual(response.data['memory'], 'joes test memory')
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_cant_retrieve_leaf_using_invalid_id(self):
    response = self.client.get('/leaves/1234/')
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

  def test_user_can_update_own_leaf(self):
    self.client.login(username='joe', password='bloggs')
    response = self.client.put('/leaves/1/', {'memory': 'a new memory'})
    leaf = Leaf.objects.filter(pk=1).first()
    self.assertEqual(leaf.memory, 'a new memory')
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_user_cant_update_another_users_leaf(self):
    self.client.login(username='joe', password='bloggs')
    response = self.client.put('/leaves/2/', {'memory': 'a new memory'})
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
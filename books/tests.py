
from django.test import TestCase
from django.urls import reverse
from .models import Recipe

class RecipeViewsTestCase(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(title='Recipe 1', year=2023)

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertContains(response, self.recipe.title)

    def test_recipe_detail_view(self):
        response = self.client.get(reverse('recipe_detail', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_detail.html')
        self.assertContains(response, self.recipe.title)

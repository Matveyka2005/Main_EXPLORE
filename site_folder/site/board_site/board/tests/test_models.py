from django.contrib.auth import get_user_model
from django.test import TestCase
from ..models import *
import mock
from django.core.files import File


class ModelsTestCase(TestCase):
    def setUp(self):
        user1 = get_user_model().objects.create_user(
            username="testuser1",
            password="123123qwerty"
        )
        user1.save()
        
      

        rubric = Rubric.objects.create(
            name="test_name",
        )
        rubric.save()

        file_mock = mock.Mock(spec=File)
        file_mock.name = "photo.jpg"

        object1 = Bb.objects.create(
            title="a test1 title",
            photo=file_mock.name,
            slug="a slug",
            content="a content",
            price=1.1,
            rubric=rubric
        )
        object1.save()
        
        # usprof = UserProfileUploads.objects.create(
        #     user=user1,
        #     product=object1,
        # )
        
    def test_models(self):
        bb1 = Bb.objects.get(id=1)
        rubric_1 = Rubric.objects.get(id=1)
        user = get_user_model().objects.get(id=1)

        file_mock = mock.Mock(spec=File)
        file_mock.name = "photo.jpg"

        title = f"{bb1.title}"
        photo = f"{bb1.photo}"
        slug = f"{bb1.slug}"
        content = f"{bb1.content}"
        price = f"{bb1.price}"
        rubric = f"{bb1.rubric.name}"

        username = f"{user.username}"

        
        self.assertEqual(title, "a test1 title")
        self.assertEqual(photo, file_mock.name),
        self.assertEqual(slug, "a slug")
        self.assertEqual(content, "a content")
        self.assertEqual(price, "1.1")
        self.assertEqual(rubric, rubric_1.name)
        # self.assertEqual(username, "testuser1")




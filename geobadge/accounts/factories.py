from django.utils import timezone
from geobadge.accounts.models import User
import factory



class UserFactory(factory.DjangoModelFactory):

    username = factory.Faker('name')
    first_name = factory.Faker('name')
    last_name = factory.Faker('name')
    email = factory.LazyAttribute(lambda o: '%s@example.org' % o.username)
    is_staff = False
    is_active = True
    last_login = factory.LazyFunction(timezone.now)

    class Meta:
        model = User

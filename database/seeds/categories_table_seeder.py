from orator.seeds import Seeder
from app.models.category import Category


class CategoriesTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        categories = [
            "ERP",
            "CRM",
            "Student Informatin System",
         ]

        for category in categories:
            Category.create(title=category)

import json
import os
from django.conf import settings
from .models import Brand, Category


def seed_brands():
    # Path to your JSON file
    file_path = os.path.join(settings.BASE_DIR, "store", "data", "brands.json")

    with open(file_path, "r", encoding="utf-8") as f:
        brands_data = json.load(f)

    created_count = 0
    for brand in brands_data:
        obj, created = Brand.objects.get_or_create(name=brand["name"])
        if created:
            created_count += 1

    print(f"✅ Seeded {created_count} brands successfully!")


def seed_categories():
    # Path to your JSON file
    file_path = os.path.join(settings.BASE_DIR, "store", "data", "categories.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    created_count = 0
    for cat in data:
        obj, created = Category.objects.get_or_create(
            name=cat["name"], slug=cat["slug"], description=cat["description"]
        )
        if created:
            created_count += 1

    print(f"✅ Seeded {created_count} categories successfully!")

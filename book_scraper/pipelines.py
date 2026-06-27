from itemadapter import ItemAdapter


class BookScraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # Strip whitespace from all string fields
        for field in adapter.field_names():
            value = adapter.get(field)
            if isinstance(value, str):
                adapter[field] = value.strip()

        # Drop items with no name or price
        if not adapter.get("Name"):
            raise DropItem(f"Missing name: {item}")

        return item
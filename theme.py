class Theme:
    def __init__(self, name, description, categories, created_date, update_date):
        self.name = name
        self.description = description
        self.categories = categories
        self.created_date = created_date
        self.update_date = update_date

    def toDBCollection(self):
        return {
            'name': self.name,
            'description': self.description,
            'categories': self.categories,
            'created_date': self.created_date,
            'update_date': self.update_date
        }

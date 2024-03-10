class Vacancy:
    vacancy_id = 0

    def __init__(self, title, url, salary_from, salary_to, description, requirements):
        self.title = title
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.description = description
        self.requirements = requirements
        self.validate_salary()
        Vacancy.vacancy_id += 1
        self.vacancy_id = Vacancy.vacancy_id

    def validate_salary(self):
        if not self.salary_to:
            self.salary_to = 0
        if not self.salary_from:
            self.salary_from = 0

    @property
    def salary(self):
        if self.salary_from < self.salary_to:
            return self.salary_to
        return self.salary_from

    def __lt__(self, other):
        return self.salary > other.salary

class Programmer:

    def __init__(self, name: str, language: str, skills: int):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        self.course_name = course_name
        self.skills_earned = skills_earned
        if self.language == language:
            self.skills += skills_earned
            return f"{self.name} watched {self.course_name}"
        else:
            return f"{self.name} does not know {language}"

    def change_language(self, new_language, skills_needed):
        self.new_language = new_language
        self.skills_needed = skills_needed

        if self.skills >= self.skills_needed:
            if self.new_language != self.language:
                self.prev_lang = self.language
                self.language = self.new_language
                return f"{self.name} switched from {self.prev_lang} to {self.language}"
            return f"{self.name} already knows {self.new_language}"
        return f"{self.name} needs {self.skills_needed - self.skills} more skills"


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))

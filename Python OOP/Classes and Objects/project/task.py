class Task:

    def __init__(self,name:str,due_date:str):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False
    def change_name(self,new_name:str):
        if self.name == new_name:
            return 'Name cannot be the same.'
        self.name = new_name
        return self.name

    def change_due_date(self,new_date:str):
        if self.due_date == new_date:
            return 'Date cannot be the same.'
        self.due_date = new_date
        return self.due_date

    def add_comment(self,comment:str):
        self.comments.append(comment)

    def edit_comment(self,comment_number:int,new_comment:str):
        if not 0 <= len(self.comments) > comment_number:
            return "Cannot find comment."
        self.comments[comment_number] = new_comment
        return f"{', '.join(self.comments)}"

    def details(self) -> str:
        return f"Name: {self.name} - Due Date: {self.due_date}"


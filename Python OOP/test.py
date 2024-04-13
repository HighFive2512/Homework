class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        # Split the email into its components (name, mail, domain)
        components = email.split("@")
        if len(components) != 2:
            return False, "Email should contain exactly one '@' character."

        name, rest = components
        mail, domain = rest.split(".", 1)

        # Validate name length
        if not self.__is_name_valid(name):
            return False, f"Name '{name}' is too short."

        # Validate mail and domain
        if not self.__is_mail_valid(mail):
            return False, f"Mail '{mail}' is not valid."

        if not self.__is_domain_valid(domain):
            return False, f"Domain '{domain}' is not valid."

        # If all validations pass, email is valid
        return True, "Email is valid."


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))

# The Email class in the blue print of the email finder.
import csv

class Email:
    def __init__(self, firstName, lastName, domain):
        self.firstName = firstName
        self.lastName = lastName
        self.domain = domain

    def tryEmail(self):

        email_list = [
            self.firstName + "@" + self.domain,
            self.lastName + "@" + self.domain,
            self.firstName + "." + self.lastName + "@" + self.domain,
            self.lastName + "." + self.firstName + "@" + self.domain,
            self.firstName[0] + "." + self.lastName + "@" + self.domain,
            self.firstName[0] + self.lastName + "@" + self.domain,
        ]

        try:
            with open("email_list.csv", "w") as file:
                for email in email_list:
                    file.write(email.lower() + "\n")
        except:
            print("Error")


firstMail = Email("james", "matinde", "matinde.com")
secondMail = Email("Anne", "Leparan", "scout.org")

firstMail.tryEmail()
secondMail.tryEmail()
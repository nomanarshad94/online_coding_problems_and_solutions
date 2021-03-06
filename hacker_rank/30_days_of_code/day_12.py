class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def __init__(self, firstName, lastName, id_, score=[]):
        super().__init__(firstName, lastName, id_)

        # self.firstName = firstName
        # self.lastName = lastName
        # self.id = id_
        self.score = score

    def calculate(self):
        a = sum(self.score) / len(self.score)
        if a >= 90:
            return 'O'
        elif a >= 80:
            return 'E'
        elif a >= 70:
            return 'A'
        elif a >= 55:
            return 'P'
        elif a >= 40:
            return 'D'
        else:
            return 'T'

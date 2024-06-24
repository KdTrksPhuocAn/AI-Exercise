from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):

    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        print(f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}")


class Teacher(Person):

    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self._subject = subject

    def describe(self):
        print(f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}")


class Doctor(Person):

    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name, yob)
        self._specialist = specialist

    def describe(self):
        print(f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}")


class Ward:

    def __init__(self, name: str):
        self.__name = name
        self.__list_people = []

    def add_person(self, person: Person):
        self.__list_people.append(person)

    def describe(self):
        print(f"Ward Name: {self.__name}")
        for p in self.__list_people:
            p.describe()

    def count_doctor(self):
        count = 0
        for p in self.__list_people:
            if isinstance(p, Doctor):
                count += 1
        return count

    def sort_age(self):
        self.__list_people.sort(key=lambda p: p.get_yob())

    def compute_average(self):
        teachers = [p for p in self.__list_people if isinstance(p, Teacher)]
        if not teachers:
            return None
        yobs = [p.get_yob() for p in teachers]
        return sum(yobs) / len(yobs)

from random import randint


class ValueError:
    pass


class Member():
    def __init__(self, id, value=None):
        self.id = id
        self.value = value

    def __str__(self):
        return 'Member id: {}'.format(self.id)


class Divider:
    members = []
    summary_value = 0

    def __init__(self, k, value):
        if value > k:
            raise ValueError()
        self.value = value
        self.k = k

    @classmethod
    def generate_members_list(cls, size):
        members_list = []
        for i in range(size):
            members_list.append(Member(i))
        return members_list

    def get_value_for_member(self, id):
        return [member for member in self.members if member.id == id][0].value

    def append_member(self, member):
        self.members.append(member)

    def calculate_n(self):
        value = self.value
        for member in self.members[:-1]:
            value -= member.value
        return value % self.k

    def generate_members_values(self):
        for member in self.members[:-1]:
            member.value = randint(1, self.k - 1)
        self.members[-1].value = self.calculate_n()

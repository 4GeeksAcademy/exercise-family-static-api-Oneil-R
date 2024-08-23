from random import randint
# initial_family_data = [(
#              {
#                 "id": self._generateId(),
#                 "first_name": "John",
#                 "last_name": "Jackson",
#                 "age": 33,
#                 "lucky_numbers": [7, 13, 22]
#             },
#             {
#                 "id": self._generateId(),
#                 "first_name": "Jane",
#                 "last_name": "Jackson",
#                 "age": 35,
#                 "lucky_numbers": [10, 14, 3]
#             },
#             {
#                 "id": self._generateId(),
#                 "first_name": "Jimmy",
#                 "last_name": "Jackson",
#                 "age": 5,
#                 "lucky_numbers": [1]
#             }
#         )]

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
             {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": "Jackson",
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": "Jackson",
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": "Jackson",
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        self._members.append(member)
        return True

    def delete_member(self, id):
        # fill this method and update the return
        self._members = list(filter(lambda x: x["id"] != id,self._members))
        pass


     
    def get_member(self, id):
        # fill this method and update the return
        members = list(filter(lambda x: x["id"] == id,self._members))
        if len(members) > 0 and members is not None:
            return members[0]
        else:
            return None
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
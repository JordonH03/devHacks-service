import segno


class Attendee:
    def __init__(self, first_name=None, last_name=None, preferred_name=None, email=None,
                 phone_number=None, obj=None, ticket_id=None, school_email=None):
        if obj:
            self.from_obj(obj)
        else:
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.discord_name = None
            self.ticket_id = ticket_id

    def to_obj(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "discord_name": self.discord_name
        }

    def from_obj(self, obj):
        self.first_name = obj.get("first_name")
        self.last_name = obj.get("last_name")
        self.email = obj.get("email")
        self.discord_name = obj.get("discord_name")

    def ticket_qr(self):
        return segno.make_qr(self.ticket_id)

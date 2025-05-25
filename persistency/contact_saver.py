from data_structures.contact import Contact

class ContactSaver:
    def __init__(self):
        self.id_counter = 0
        self.contact_data: dict[int, Contact] = {}

    def save_contact(self, contact):
        self.contact_data[self.id_counter] = contact
        self.id_counter += 1

    def get_preview_of_all_contacts(self) -> dict[int, str]:
        previews: dict[int, str] = {}
        for contact_id, contact in self.contact_data.items():
            previews[contact_id] = contact.get_name()
        return previews

    def get_contact(self, contact_id):
        return self.contact_data.get(contact_id, None)
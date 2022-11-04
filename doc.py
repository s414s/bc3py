
class Bc3doc:

    def __init__(self, file):
        self.file = file
        self.parser_errors = None
        self.file_lines = None
        self.registries = None
        self.concepts = None
        self.section_specifications = None
        self.geographic_scope = None
        self.entities = None
        self.coefficient = None


    def complete_from_bc3(self):
        pass        

    def create_from_json(self):
        pass

    def create_from_xml(self):
        pass

    def set_registries(self):
        pass

    def complete_concepts(self):
        pass

    def set_specification_sections(self, fields):
        pass

    def get_concept_by_nature(self, concept_nature):

        pass

    def get_concept_by_id(self, concept_id):
        pass

    def print_concept(self, concept_id):



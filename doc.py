from registry import Registry_Handler

class Bc3doc:

    def __init__(self, bc3_file):
        self.file = bc3_file
        self.parser_errors = None
        self.file_lines = None
        self.concepts = None
        self.section_specifications = None
        self.geographic_scope = None
        self.entities = None
        self.coefficient = None
        self.bc3_handler = Registry_Handler(self)

    def set_registries(self):
        #to be completed
        pass

    def complete_concepts(self):
        #to be completed
        pass

    def set_specification_sections(self, fields):
        #to be completed
        pass

    def get_concept_by_nature(self, concept_nature):
        #to be completed
        pass

    def get_concept_by_id(self, concept_id):
        #to be completed
        pass

    def print_concept(self, concept_id):
        #to be completed
        pass



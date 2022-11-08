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
        self.bim_files = None
        self.bc3_handler = Registry_Handler(self)

    def add_concept(self, concept_obj):
        if self.concepts == None:
            self.concepts = []

        self.concepts.append(concept_obj)

    def set_specification_sections(self, fields):
        #to be completed
        pass

    def set_bim_files(self, f):
        if self.bim_files:
            self.bim_files.append(f)
        else:
            self.bim_files = []
            self.bim_files.append(f)

    def get_concepts_by_nature(self, concept_nature):
        #to be completed
        pass

    def get_concept_by_code(self, c_code):
        for c in self.concepts:
            if c.code == c_code:
                return c
        #to be completed

    def get_concept_by_id(self, concept_id):
        # if concept_id in Object.concept_id
        #to be completed
        pass

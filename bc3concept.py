class Bc3_Concept:

    def __init__(self, code):
        self.code = code # (1,N) max 20 characters
        self.unit = None # (0,1)
        self.summary = None # (0,1)
        self.descriptive_text = None # (0,1)
        self.price = None # (0,N)
        self.date = None # (0,N)
        self.type = None # (0,1) root-type (-##), chapter-type (-#)
        self.nature = None # own value ROOT/CHAPTER/ITEM
        self.id = None # own id reference
        self.specification = None # set by registry L, LIST OF DICTIONARIES > specification_section_code:specification_section_label
        self.parent = None # (1,1)
        self.child = None # (1,N)
        self.position = None # (0,1)
        self.graphic_information = None
        self.total_measurement = None
        self.measurement = None
        self.position = None
        self.waste_decomposition = None
        self.set_nature(self.code)

    def set_code(self, c_code):
        # to be completed
        pass

    def set_unit(self, unit):
        self.unit = unit
        # to be completed

    def set_summary(self, s):
        self.summary = s
        # to be completed

    def set_descriptive_text(self, dt):
        # to be completed
        pass

    def set_price(self, p):
        self.price = p
        # to be completed

    def set_date(self, d):
        self.date = d
        # to be completed

    def set_type(self, concept_type):
        self.type = concept_type
        # to be completed

    def set_id(self, c_id):
        # to be completed
        pass
        
    def set_specification(self, list_of_data):
        # to be completed
        pass

    def set_parent(self, p):
        # to be completed
        pass

    def set_child(self, c):
        if self.child == None:
            self.child = []

        self.child.append(c)

    def set_graphic_information(self, graphic_information):
        # to be completed
        pass

    def set_total_measurement(self, tm):
        self.total_measurement = tm

    def set_measurement(self, m):
        if self.measurement == None:
            self.measurement = []

        self.measurement.append(m)

    def set_position(self, p):
        # to be completed
        pass

    def set_waste_decomposition(self, wd):
        if self.waste_decomposition == None:
            self.waste_decomposition = []

        self.waste_decomposition.append(wd)

    def set_position(self, p):
        if self.position:
            pass
        else:
            self.position = p

    def set_nature(self, code):
        if '##' in code:
            self.nature = 'root'
        elif '#' in code:
            self.nature = 'chapter'
        else:
            self.nature = 'element'

    def check_coefficients(self, coefficients):
        # will check all the numbers comply with the coefficients.
        pass

    def print_chapters(self):
        pass

    def print_concepts_in(self, c_code):
        pass

    def print_measurement(self, c_code):
        pass

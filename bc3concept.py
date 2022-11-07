class Bc3_Concept:

    def __init__(self, code):
        self.code = code #(1,N) maximum 20 characters. 1 for now
        self.unit = None #(0,1)
        self.summary = None #(0,1)
        self.descriptive_text = None # set by regitry T
        self.price = None #(0,N)
        self.date = None #(0,N)
        self.type = None #(0,1) root-type (-##), chapter-type (-#)
        self.nature = None # internal value ROOT/CHAPTER/ELEMENT
        self.id = None # internal id reference
        self.specification = None # set by registry L, LIST OF DICTIONARIES > specification_section_code:specification_section_label
        self.parent = None # (1,1) set by registry D
        self.child = None # (1,N) set by registry D LIST OF DICTIONARIES
        self.graphic_information = None
        self.measurement = None
        self.set_nature(self.code)

    def set_code(self, concept_code):
        #to be completed
        pass

    def set_unit(self, unit):
        self.unit = unit
        #to be completed

    def set_summary(self, summary):
        self.summary = summary
        #to be completed

    def set_descriptive_text(self, descriptive_text):
        #to be completed
        pass

    def set_price(self, price):
        self.price = price
        #to be completed

    def set_date(self, date):
        self.date = date
        #to be completed

    def set_type(self, concept_type):
        self.type = concept_type
        #to be completed

    def set_id(self, concept_id):
        #to be completed
        pass
        
    def set_specification(self, list_of_data):
        #to be completed
        pass

    def set_parent(self, parent):
        #to be completed
        pass

    def set_child(self, child):
        if self.child == None:
            self.child = []
        self.child.append(child)
        #to be completed

    def set_graphic_information(self, graphic_information):
        #to be completed
        pass

    def set_measurement(self, measurement):
        #to be completed
        pass

    def set_nature(self, code):
        if '##' in code:
            self.nature = 'root'
        elif '#' in code:
            self.nature = 'chapter'
        else:
            self.nature = 'element'

    def check_coefficients(self, coefficients):
        #will check all the numbers comply with the coefficients.
        pass

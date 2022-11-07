from bc3concept import Bc3_Concept

class Registry_Handler:

    def __init__(self, document):
        self.action = {
            'V': self.set_ownership,
            'K': self.set_coefficient,
            'C': self.create_concept,
            'D': self.set_decomposition,
            'Y': self.add_decomposition,
            'R': self.set_waste_decomposition,
            'T': self.set_text,
            'P': self.set_parametric_description,
            'L': self.set_specification,
            'W': self.set_geographic_scope,
            'G': self.set_graphic_information,
            'E': self.set_entity,
            'O': self.set_commercial_relation,
            'X': self.set_technical_information,
            'M': self.set_measurement,
            'N': self.add_measurement,
            'I': self.set_bim_file,
            'A': self.set_key,
            'B': self.set_code_change,
            'F': self.set_attached_file
            }
        self.doc = document
        self.registries = None
        self.get_registries(document.file.replace('\n', ''))
        self.read_registries(self.registries)

    def code_type(self, code):
        #to be completed. returns wether it is the root, chapter or element
        pass

    def simply_code(self, code):
        #to be completed. Returns code without # or ##
        pass

    def group_sufields(self, subfields, num):
        num_groups = len(subfields)%num_elements
        groups = [subfields[(i*num):num+(i*num)] for i in range(num_groups)]    
        return groups  #returns an array with arrays
    
    def get_registries(self, raw_data):
        registries = raw_data.split('~')
        self.registries = []
        for registry in registries:
            line = []
            fields = registry.split('|')
            for field in fields:
                if '\\' in field:
                    subfields = field.split('\\')
                    line.append(subfields)
                else:
                    line.append(field)
            self.registries.append(line)
        
    def set_ownership(self, registry):
        #to be completed
        pass

    def set_coefficient(self, registry):
        fields = self.get_fields(registry)
        default_values1 = {
            'dn': 2, # >=0
            'dd': 2, # >=0
            'ds': 2, # >=0
            'dr': 3, # >=0
            'di': 2, # >=0
            'dp': 2, # >=0
            'dc': 2, # >=0
            'dm': 2, # >=0
            'currency': None,  # >=0
            'ci': None,
            'gg': None,
            'bi': None,
            'reduction': None,
            'vat': None
            }
        default_values2 = {
            'drc': 3,
            'dc': 2,
            'dfs': 3,
            'drs': 3,
            'duo': 2,
            'di': 2,
            'des': 2,
            'dn': 2,
            'dd': 2,
            'ds': 2,
            'dsp': 2,
            'dec': 2,
            'currency': None
            }
        #to be completed
   
    def create_concept(self, registry):
        default_types = {
            '0': 'sin clasificar',
            '1': 'mano de obra',
            '2': 'maquinaria y medios auxiliares',
            '3': 'materiales',
            '4': 'componentes adiciones de residuo',
            '5': 'clasificacion de residuos'
            }
        code = registry[1] # (1,N)
        unit = registry[2] # (0,1)
        summary = registry[3] # (0,1)
        price = registry[4] # (0,N)
        date = registry[5] # (0,N)
        c_type = registry[6] # (0,1)          

        concept = Bc3_Concept(code)

        if unit:
            concept.set_unit(unit)

        if summary:
            concept.set_summary(summary)

        if price:
            concept.set_price(price)

        if date:
            concept.set_date(date)

        if c_type:
            if c_type in default_types.keys():
                concept.set_type(default_types[c_type])
            else:
                concept.set_type(c_type)

        self.doc.add_concept(concept)

    def set_decomposition(self, registry):
        result_to_append = {
            'code': 'code of the element if belongs to',
            'factor': 'rendimiento en los elementos donde forma parte',
            'output': 'output en los elementos donde forma parte'
            }
        #to be completed

    def add_decomposition(self, registry):
        #to be completed. set child and parent
        pass

    def set_waste_decompostion(self, registry):
        #to be completed
        pass

    def set_text(self, registry):
        #to be completed
        pass

    def set_parametric_description(self, registry):
        #to be completed
        pass

    def set_specification(self, registry):
        #to be completed
        pass

    def set_geograhic_scope(self, registry):
        entity_code = registry[1]
        entity_summary = registry[2]
        entity_name = registry[3]
        entity_contact_info = registry[4]
        entity_tax_id = registry[5]
        entity_web = registry[6]
        entity_email = registry[7]
        #target = doc_obj.get_element_by_code(entity_code)
        #to be completed

    def set_graphic_information(self, registry):
        #to be completed
        pass

    def set_entity(self, registry):
        #to be completed
        pass

    def set_commercial_relation(self, registry):
        #to be completed
        pass

    def set_technical_information(self, registry):
        #to be completed
        pass

    def set_measurement(self, registry):
        measurement = {}
        types_measurement = {
            '1': 'Partial Subtotal',
            '2': 'Cumulative Subtotal',
            '3': 'Expression'
            }

        measurement.append({
            'type': 'especificar',
            'comment': 'especificar',
            'units': 'especificar',
            'lenght': 'especificar',
            'latitude': 'especificar',
            'height': 'especificar',
            })
        #to be completed
        
    def add_measurement(self, registry):
        #to be completed
        pass

    def set_bim_file(self, registry):
        #to be completed
        pass

    def set_key(self, registry):
        #to be completed
        pass

    def set_code_change(self, registry):
        #to be completed
        pass

    def set_attached_file(self, registry):
        #to be completed
        pass

    def set_waste_decomposition(self, registry):
        #to be completed
        pass

    def set_parametric_description(self, registry):
        #to be completed
        pass

    def set_geographic_scope(self, registry):
        #to be completed
        pass

    def execute_registry(self, registry):
        if registry[0] in self.action.keys():
            self.action[registry[0]](registry)
            #action.get(key[registry[0], "skip"])
        else:
            pass
        
    def read_registries(self, registries):
        for registry in registries:
            if registry[0] and registry[0]=="C": #change in order to try more options
                self.execute_registry(registry)

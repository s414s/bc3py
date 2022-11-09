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
            'Q': self.set_specification2,
            'J': self.set_specification3,
            'W': self.set_geographic_scope,
            'G': self.set_graphic_information,
            'E': self.set_entity,
            'O': self.set_commercial_relationship,
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
        self.id_count = 1
        self.get_registries(document.file.replace('\n', '')) # TBD respect ASCII-10 (\n) and ASCII-13 (\r)
        self.read_registries(self.registries)

    def code_type(self, code):
        #to be completed. returns wether it is the root, chapter or element
        pass

    def clean_code(self, code):
        #to be completed. Returns code without # or ##
        pass

    def group_subfields(self, subfields, num): #returns an array of groups
        num_groups = int(len(subfields)/num)
        groups = [subfields[(i*num):num+(i*num)] for i in range(num_groups)]    
        return groups

    def check_exists(self, field):
        # check whether an index of an array exists
        try:
            if field:
                return field
        except IndexError:
            field = None
            return field
    
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
        
    def set_ownership(self, r): # discrepancies found
        file_ownership = r[1]
        format_version = r[2]
        date = None # (0,1)
        emission_program = r[3]
        header = r[4]
        identification_label = None # (0, N)
        character_set = r[5]
        comment = r[6]
        information_type = r[7]
        certification_number = r[8]
        certification_date = r[9]
        url_base = r[10]
        
        #to be completed
        pass

    def set_coefficient(self, r):
        default_values1 = { # (0, N)
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
   
    def create_concept(self, r):
        default_types = {
            '0': 'unclassified',
            '1': 'labour',
            '2': 'machinery and auxiliary equipment',
            '3': 'materials',
            '4': 'additional waste components',
            '5': 'waste classification'
            }
        code = r[1] # (1,N)
        unit = self.check_exists(r[2]) # (0,1)
        summary = self.check_exists(r[3]) # (0,1)
        price = self.check_exists(r[4]) # (0,N)
        date = self.check_exists(r[5]) # (0,N)
        c_type = self.check_exists(r[6]) # (0,1)          

        concept = Bc3_Concept(code)

        concept.id = self.id_count
        self.id_count += 1

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

    def set_decomposition(self, r):
        p_code = r[1] # (1)
        dec = r[2] # (1,N)
        dec2 = r[3] # (1,N) Decide which one to be used
        
        children = self.group_subfields(dec, 3)
        pc = self.doc.get_concept_by_code(p_code)
        
        for c in children:
            code = c[0] # (1)
            factor = 1
            if self.check_exists(c[1]): # (0,1)
                factor = c[1]
            output = 1
            if self.check_exists(c[2]): # (0,1)
                output = c[2]
            
            pc.set_child({'code': code,
                          'factor': factor,
                          'output': output})
            
            cc = self.doc.get_concept_by_code(code)
            cc.set_parent({'code': p_code,
                           'factor': factor,
                           'output': output})

    def add_decomposition(self, r):
        self.set_decomposition(r)

    def set_waste_decomposition(self, r):
        # merge with child from decomposition
        p_code = r[1] # (1)
        dec = r[2:] # (0,N)
        def_d_type = {
            '0': 'Placement-component waste',
            '1': 'Demolition-component waste',
            '2': 'Excavation-component waste',
            '3': 'Packaging-component waste'
            }
        tc = self.doc.get_concept_by_code(p_code)

        for line in dec:
            if line:
                p = []
                d_type = line[0]
                if d_type in def_d_type.keys():
                    d_type = def_d_type[line[0]]
                
                c_code = line[1]
                properties = self.group_subfields(line[2:], 3) # (0,N)
                for field in properties:
                    prop = field[0]
                    value = field[1]
                    um = self.check_exists(field[2])
                    p.append([prop, value, um])
                self.doc.set_waste_decomposition([d_type, c_code, p])
                
        #to be completed
        pass

    def set_text(self, r): #respect ASCII-10 (\n) and ASCII-13 (\r)
        c_code = r[1]
        descriptive_text = r[2]
        tc = self.doc.get_concept_by_code(c_code)
        tc.set_descriptive_text(descriptive_text)

    def set_parametric_description(self, r):
        #to be completed
        pass

    def set_specification(self, r):
        #to be completed
        pass

    def set_specification2(self, r):
        #to be completed
        pass

    def set_specification3(self, r):
        #to be completed
        pass

    def set_geograhic_scope(self, r):
        #to be completed
        pass

    def set_graphic_information(self, r):
        c_code = r[1] # (1)
        name_file = self.check_exists(r[2]) # (1,N)
        url_ext = self.check_exists(r[3]) # (0,1)
        tc = self.doc.get_concept_by_code(c_code)
        #to be completed

    def set_entity(self, r):
        e_code = r[1] # (1)
        summary = self.check_exists(r[2]) # (0,1)
        name = self.check_exists(r[3]) # (0,1)
        contact_log = self.check_exists(r[4]) # (0,N)
        tax_id = self.check_exists(r[5]) # (0,1)
        web = self.check_exists(r[6]) # (0,1)
        email = self.check_exists(r[7]) # (0,1)

        def_c_type = {
            'c': 'Central',
            'd': 'Delegation',
            'r': 'Representative'
            }

        if contact_log:
            cl = []
            lines = self.group_subfiles(contact_log, 10)
            for l in lines:
                c_type = self.check_exists(l[0]) # (0,1)
                subname = self.check_exists(l[1]) # (0,1)
                address = self.check_exists(l[2]) # (0,1)
                pc = self.check_exists(l[3]) # (0,1)
                town = self.check_exists(l[4]) # (0,1)
                province = self.check_exists(l[5]) # (0,1)
                country = self.check_exists(l[6]) # (0,1)
                telephone = self.check_exists(l[7]) # (0,N)
                fax = self.check_exists(l[8]) # (0,N)
                contact_person = self.check_exists(l[9]) # (0,N)
        else:
            cl = None

        self.doc.set_entity({
            'code': e_code,
            'summary': summary,
            'name': name,
            'contact_list': cl,
            'tax_id': tax_id,
            'web': web,
            'email': email
            }) #create this method

    def set_commercial_relationship(self, r):
        #to be completed
        pass

    def set_technical_information(self, r):
        #to be completed
        pass

    def set_measurement(self, r):
        codes = r[1] # (1) parent code optional
        position = self.check_exists(r[2]) # (0,N)
        total_meas = r[3] # (1) Must coincide with the output of the corresponding ~D-type registry
        info_meas = self.check_exists(r[4]) # (0,N)
        label = self.check_exists(r[5]) # (0,1)
        
        # ---- Codes ----
        if isinstance(codes, list):
            p_code = codes[0]
            c_code = codes[1]
        else:
            p_code = None
            c_code = codes

        tc = self.doc.get_concept_by_code(c_code)

        # ---- Position ----
        if position and tc: # remove empty fields
            p = []
            for item in position:
                if item:
                    p.append(item)
            tc.set_position(p)
        # TBD

        # ---- Info Meas ----
        tc.set_total_measurement(total_meas)

        if info_meas and tc:
            meas_lines = self.group_subfields(info_meas, 6)
            def_type = {
                '1': 'Partial Subtotal',
                '2': 'Cumulative Subtotal',
                '3': 'Expression'
                }

            for m in meas_lines:
                m_type = self.check_exists(m[0])
                if m_type in def_type.keys():
                    m_type = def_type[m[0]]
                
                com = self.check_exists(m[1])
                u = self.check_exists(m[2])
                l = self.check_exists(m[3])
                lat = self.check_exists(m[4])
                h = self.check_exists(m[5])
                tc.set_measurement({'type': m_type,
                                    'comment': com,
                                    'units': u,
                                    'length': l,
                                    'latitude': lat,
                                    'height': h})
        # compare the total measurememt with the sum of meas
        
    def add_measurement(self, r):
        pass

    def set_bim_file(self, r):
        files = r[1]
        f = []
        for file in files:
            if file:
                f.append(file)
        self.doc.set_bim_files(f)
                
    def set_key(self, r):
        pass

    def set_code_change(self, r):
        pass

    def set_attached_file(self, r):
        c_code = r[1] # (1)
        file_info = self.check_exists(r[2]) # (0,N)
        url_ext = self.check_exists(r[3]) # (0,1)
        tc = self.doc.get_concept_by_code(c_code)
        def_f_type = {
            '0': 'Other',
            '1': 'Technical and manufacturing characteristics',
            '2': 'Installation, use and maintenance manual',
            '3': 'Element(s) and system(s) certificate(s)',
            '4': 'Regulations and bibliography',
            '5': 'Price list',
            '6': 'Sale conditions',
            '7': 'Colour chart',
            '8': 'Scope and selection criteria',
            '9': 'Elements and systems calculation',
            '10': 'Presentation, general data and objectives of the company',
            '11': 'Company certificate/s',
            '12': 'Works completed',
            '13': 'Image'
            }

        lines = self.group_subfields(file_info, 3)

        if file_info:
            f = []
            for l in lines:
                if l[0] in def_f_type.keys():
                    f_type = def_f_type[l[0]]
                else:
                    f_type = l[0]
                    
                f_ext = self.check_exists(l[1]) # (0,N)
                f_des = self.check_exists(l[2]) # (0,1)
                f.append([f_type, f_ext, f_des])

        if file_info and url_ext:
            tc.set_attached_file([f, url_ext])
        elif file_info:
            tc.set_attached_file(f)
        else:
            tc.set_attached_file(url_ext)

    def set_geographic_scope(self, r):
        #to be completed
        pass

    def execute_registry(self, r):
        if r[0] in self.action.keys():
            self.action[r[0]](r)
        else:
            pass
        
    def read_registries(self, rs):
        # include a 'try' to handle errors
        test_ready = ['C']
        for r in rs:
            if r[0] and r[0] in test_ready:
                self.execute_registry(r)

        for r in rs:
            if r[0] and r[0] in ['M', 'D', 'T']: # add registry types ready to test
                self.execute_registry(r)

from random import *

try:
    from Allocation import Allocate
    from database import *

except Exception:
    from .Allocation import Allocate
    from .database import *
    
# NOTE: Algorithum does not hold validation for less than five classes.

class Generator(Allocate):
    def __init__(
        self,
        cls: int,
        faculty: str,
        shift: str,
        sections: int,
        periods: int,
        days: int,
        opt: int,
    ):
        super().__init__(cls, faculty, shift, sections, periods, days, opt)

        self.time_per_subject = {
            next(iter(unit)): None
            for subject in self.subject for unit in DB.fetch(f'"{subject}"', 'specific', 'unit')
            }

        for subject in self.subject:
            for key in self.time_per_subject: 
                for j in DB.fetch(f'"{subject}"', 'quiere', 'tpp', f'unit = "{key}"'): self.time_per_subject[key] = next(iter(j))


        self.sorted_cord = {slot: {section: None
        for j in self.subject_section[slot]
        for section in j}
        for slot in self.subject_section}

        for slot in self.subject_section: 
            for sec in self.subject_section[slot]: self.filter(slot, sec)

    def corr_rows(self, row: int, sec_no):
        unit_row = row - ((self.DAYS + 1) * (sec_no - 1))
        
        return [( (self.DAYS + 1) * i) + unit_row for i in range(self.SECTIONS)]

    def filter(self, slot: str, sections: list):

        def filter_for_corresponding_row(): 
            section_list = []

            for section in sections:
                section_list.append(sample(self.row_col[section], self.time_per_subject[slot]))

            for index in range(len(section_list)):

                sec_no = int(sections[index][1:]) #section no.

                for cord in section_list[index]:
                    corr_row = self.corr_rows(cord[0], sec_no) #taking corresponding rows

                    for index_ in range(len(section_list)):
                        if index != index_ and index_ > index: #index 1 != index 2 and pervious index must not repate

                            for cord_ in section_list[index_]:

                                if cord_[1] == cord[1] and cord_[0] in corr_row: 
                                    # if col of index1 == col of index2 and row of index2 in corr_row
                                    conflict = cord_

                                    while conflict == cord_: #generate cord of non-correspoding rows
                                        
                                        conflict = sample(self.row_col[sections[index_]], self.time_per_subject[slot])[0]
                                        if conflict[0] in corr_row: conflict = cord_ # check if non-correspoding row; else repate

                                        else: # else change the pervious cord with cord with non-corresponding row
                                            k = section_list[index_].index(cord_) 
                                            section_list[index_][k] = conflict

            for i in range(len(sections)):
                self.sorted_cord[slot][sections[i]] = filter_for_same_row(sections[i], section_list[i])
        
        def filter_for_same_row(section, section_list): #Check if row are equal for same section.
            
            sec_no = int(section[1:])
        
            for i in section_list:
                
                conflict_list = {i[0] for i in section_list} # contains unique rows
                
                for j in section_list:
                
                    if i[0] == j[0] and i != j or i == j and section_list.count(i) > 1: 
                    # Check if row_1 == row_2 for different cord | if number of same cord in list > 1

                        conflict = j
                        count = 0

                        while conflict == j :
                            count += 1
                            
                            conflict = sample(self.row_col[section], self.time_per_subject[slot])[0]
                            if conflict[0] in conflict_list: conflict = j 
                            # checks if new row generated is already in the set of unique rows or not
                            # if true: value of conflict remains unchanged

                            if count > 100: #if coordinates are less and no options are left for new generation: try for 100; break loop
                                break

                            else: 
                                section_list[section_list.index(j)] = conflict # value of conflict is moved to the section_list
                                conflict_list.add(conflict[0]) # adds unique row generated to slove conflict to conflict_list
            
            for section_removed in section_list: 

                try:
                    self.row_col[section].pop(
                    self.row_col[section].index(section_removed)
                )

                except ValueError:
                    pass

            return section_list

        filter_for_corresponding_row()

# domy = {'cls': 11, 'faculty': 'Science', 'shift': 'Day', 'sections': 18, 'periods': 7, 'days': 6, 'opt': 7}
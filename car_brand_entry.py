#!/usr/bin/python
# -*- coding: UTF-8 -*-

class BranchCar:

    def __init__(self,branch_name,brand_id,branch_initial,logo):
        self.branch_name=branch_name
        self.branch_initial=branch_initial
        self.logo=logo
        self.brand_id =brand_id
    def print_format_str(self):
        print('\t'.join([self.branch_name, self.brand_id, self.branch_initial, self.logo]))

    def get_format_str(self):
        return '\t'.join([self.branch_name, self.brand_id, self.branch_initial, self.logo])

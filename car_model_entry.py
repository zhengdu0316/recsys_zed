#!/usr/bin/python
# -*- coding: UTF-8 -*-


class model_entry:


    def __init__(self, brand_name,brand_id,prodution_firm,car_model,model_id):
        self.brand_name=brand_name
        self.prodution_firm=prodution_firm
        self.car_model=car_model
        self.brand_id=brand_id
        self.model_id=model_id

    def get_format_data(self):
        return '\t'.join([self.brand_name,self.brand_id,self.prodution_firm,self.car_model,self.model_id])

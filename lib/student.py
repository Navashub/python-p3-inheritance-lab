#!/usr/bin/env python

from user import User

class Student(User):
        
    def __init__(self, first_name, last_name, knowlegde=[]):
            super().__init__(first_name, last_name)
            self.knowledge = knowlegde

    def learn(self,unit):
        self.unit=unit
        self.knowledge.append(unit)    
            
        
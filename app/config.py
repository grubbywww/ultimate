#! /usr/bin/env flask/bin/python
# -*- coding: utf-8 -*-
import yaml
class ReadYaml():
    def __init__(self,yamls):
        self.yamls = yamls
        f = open(self.yamls,'r')
        self.data = yaml.load(f)

    def option(self):
        return self.data['option']
    def task(self):
        return self.data['task']

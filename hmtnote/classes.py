#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import requests
from typing import Union
from vcf.model import _Record


class VarRecord:
    def __init__(self, record):
        self.record = record
        self.variant = f"{self.record.REF}{self.record.POS}{self.record.ALT}"

    def is_variation(self):
        if self.record.ALT != [None]:
            return True
        return False

    @property
    def response(self) -> dict:
        url = f"https://www.hmtvar.uniba.it/api/main/mutation/{self.variant}"
        call = requests.get(url)
        # if call.status_code == 200:
        # TODO this is always 200, unless the variant format is wrong, which should never happen
        # TODO variants not present in HmtVar actually return an empty dictionary
        resp = call.json()
        return resp

    @staticmethod
    def replace_null(element: str) -> Union[str, int, float]:
        if element == "null":
            return "."
        return element

    def annotate_main(self):
        values = {"Locus": self.response.get("locus", ".")}
        # TODO







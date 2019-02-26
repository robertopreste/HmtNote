#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import json
import requests
import vcf


def hmtvar_request(variant: str) -> dict:
    """
    Send a request to HmtVar's API with the given mutation.
    :param str variant: mutation in the format [ref][position][alt]
    :return: dict
    """
    url = f"https://www.hmtvar.uniba.it/api/main/mutation/{variant}"
    resp = requests.get(url)
    r = resp.json()

    return r


def replace_null(element: str) -> str:
    """
    Replace 'null' values from HmtVar's response with a simple '.', as is common for VCF
    annotations.
    :param str element: value returned by HmtVar
    :return: str the actual value returned if it is not null, otherwise .
    """
    if element == "null":
        return "."
    return element


def hmtvar_parse(response: dict) -> dict:
    """
    Parse the response returned by HmtVar's API into a suitable format.
    :param dict response: json dictionary returned by HmtVar
    :return: dict
    """
    annot = {
        "Locus": replace_null(response["locus"]),
        "Aa_Change": replace_null(response["aa_change"]),
        "Pathogenicity": replace_null(response["pathogenicity"]),
        "Disease_Score": replace_null(response["disease_score"])
    }

    return annot


def annotate_vcf(in_vcf, out_vcf):
    in_reader = vcf.Reader(open(in_vcf, "r"))
    out_writer = vcf.Writer(open(out_vcf, "w"), in_reader)
    for rec in in_reader:
        if rec.CHROM == "MT" and rec.ALT != [None]:
            if len(rec.ALT) == 1:
                variant = f"{rec.REF}{rec.POS}{rec.ALT[0]}"
                req = hmtvar_request(variant)
                ann = hmtvar_parse(req)
                rec.add_info("Locus", ann["Locus"])
                rec.add_info("Aa_Change", ann["Aa_Change"])
                rec.add_info("Pathogenicity", ann["Pathogenicity"])
                rec.add_info("Disease_Score", ann["Disease_Score"])
                out_writer.write_record(rec)
    out_writer.close()






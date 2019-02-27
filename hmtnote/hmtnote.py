#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import json
import requests
import vcf


# to update header with new infos:
# pysam.VariantFile.header.info.add(id="TE", number=1, type="String", description="prova")


def annotate_vcf(in_vcf, out_vcf):
    reader = vcf.Reader(open(in_vcf, "r"))



# def annotate_vcf(in_vcf, out_vcf):
#     in_reader = vcf.Reader(open(in_vcf, "r"))
#     out_writer = vcf.Writer(open(out_vcf, "w"), in_reader)
#     for rec in in_reader:
#         if rec.CHROM == "MT" and rec.ALT != [None]:
#             if len(rec.ALT) == 1:
#                 variant = f"{rec.REF}{rec.POS}{rec.ALT[0]}"
#                 req = hmtvar_request(variant)
#                 ann = hmtvar_parse(req)
#                 rec.add_info("Locus", ann["Locus"])
#                 rec.add_info("Aa_Change", ann["Aa_Change"])
#                 rec.add_info("Pathogenicity", ann["Pathogenicity"])
#                 rec.add_info("Disease_Score", ann["Disease_Score"])
#                 out_writer.write_record(rec)
#     out_writer.close()






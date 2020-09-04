import csv
import os
from biothings.utils.dataload import dict_sweep


DISEASE_NAME_ID_MAPPING = {
    "LAML": "MONDO:0018874",
    "ACC": "MONDO:0008734",
    "BLCA": ["MONDO:0004056", "MONDO:0004163"],
    "LGG": "MONDO:0005499",
    "BRCA": "MONDO:0006256",
    "CESC": ["MONDO:0006143", "MONDO:0000554"],
    "CHOL": "MONDO:0019087",
    "LCML": "MONDO:0011996",
    "COAD": "MONDO:0002271",
    "ESCA": ["MONDO:0003093", "MONDO:0005580"],
    "GBM": "MONDO:0018177",
    "HNSC": "MONDO:0010150",
    "KICH": "MONDO:0017885",
    "KIRC":	"MONDO:0005005",
    "KIRP":	"MONDO:0017884",
    "LIHC":	"MONDO:0007256",
    "LUAD":	"MONDO:0005061",
    "LUSC":	"MONDO:0005097",
    "DLBC":	"MONDO:0018905",
    "MESO":	"MONDO:0005065",
    "OV": "MONDO:0006046",
    "PAAD":	"MONDO:0006047",
    "PCPG":	["MONDO:0004974", "MONDO:0000448"],
    "PRAD": "MONDO:0005082",
    "READ":	"MONDO:0002169",
    "SARC":	"MONDO:0005089",
    "SKCM":	"MONDO:0005012",
    "STAD":	"MONDO:0005036",
    "TGCT":	"MONDO:0010108",
    "THYM":	"MONDO:0006456",
    "THCA":	"MONDO:0015075",
    "UCS": "MONDO:0006485",
    "UCEC": "MONDO:0000553",
    "UVM": "MONDO:0006486",
    "ALL": "MONDO:0004967",
    "MM": "MONDO:0005170",
    "NB": "MONDO:0005072",
    "SCLC": "MONDO:0008433"
}

def load_data(data_folder):
    path = os.path.join(data_folder, "data.csv")
    with open(path) as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for row in reader:
            if "-" in row[1]:
                disease_abbr = row[1].split('-')[-1]
            elif "_" in row[1]:
                disease_abbr = row[1].split('_')[-1]
            yield dict_sweep({
                "_id": row[0] + '-' + row[1],
                "subject": {
                    "id": "SYMBOL:" + row[0],
                    "SYMBOL": row[0],
                    "type": "gene"
                },
                "object": {
                    "id": DISEASE_NAME_ID_MAPPING[disease_abbr],
                    "tcga_name": disease_abbr,
                    "MONDO": DISEASE_NAME_ID_MAPPING[disease_abbr],
                    "type": "disease"
                },
                "association": {
                    "edge_label": "gene_has_variant_that_contributes_to_disease_association",
                    "relation_name": "gene_has_variant_that_contributes_to_disease_association",
                    "freq_by_sample": float(row[2]),
                    "freq_by_case": float(row[3]),
                    "no_mut_samples": int(row[4]),
                    "no_mut_cases": int(row[5])
                }
            }, vals=['NA'])
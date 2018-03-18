# Copyright (C) 2018  Ahmad A. A. (https://github.com/bbpgrs/)

import pandas as pd
import common as cmn
import os
import logging
import operator
import math


def col_rank_genes():
    """
    """
    combined_file_path = os.path.join(cmn.DL_DIR, cmn.PTEN_COMB_FNAME)
    if os.path.isfile(combined_file_path):
        logging.info("Found combined PTEN correlation file, generating rankings ...\n")

        df = pd.read_csv(combined_file_path, sep="\t", index_col=0)

        column_ranks_file = os.path.join(cmn.DL_DIR, cmn.COL_RANK_FNAME)
        col_ranks = pd.DataFrame()
        i = 0

        for col in df.columns:
            logging.info("Generating rankings for '%s' ..." % col)

            col_rank_dict = {}
            for row in df.index:
                if not math.isnan(float(df.loc[row][col])):
                    col_rank_dict[row] = abs(float(df.loc[row][col]))
                else:
                    col_rank_dict[row] = 0
            col_rank = sorted(col_rank_dict.items(), key=operator.itemgetter(1), reverse=True)
            col_ranks.insert(i, col, [t[0] for t in col_rank])
            i += 1

            logging.info("Done.\n")

        logging.info("Writing column rankings to file ...")
        col_ranks.to_csv(column_ranks_file, sep="\t")
        logging.info("Done.\n")

    else:
        logging.warning("Combined PTEN correlation file not found.")


def run():
    """
    """
    col_rank_genes()

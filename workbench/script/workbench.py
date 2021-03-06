import aspralign_workbench
import nestedalign_workbench
import rnaforester_workbench
import rnadistance_workbench
import locarna_workbench
import rag2d_workbench
from paths import *

if __name__ == '__main__':
    aspralign_workbench.csv([ARCHAEA_DIR, BACTERIA_DIR, EUKARYOTA_DIR],
                            [ASPRALIGN_ARCHAEA_OUTPUT_FILE, ASPRALIGN_BACTERIA_OUTPUT_FILE,
                             ASPRALIGN_EUKARYOTA_OUTPUT_FILE], ASPRALIGN_WORKBENCH_JAR, ASPRALIGN_CONFIG_FILE)

    nestedalign_workbench.csv([ARCHAEA_DIR, BACTERIA_DIR, EUKARYOTA_DIR],
                              [NESTEDALIGN_ARCHAEA_OUTPUT_FILE, NESTEDALIGN_BACTERIA_OUTPUT_FILE,
                               NESTEDALIGN_EUKARYOTA_OUTPUT_FILE])

    rnaforester_workbench.csv([ARCHAEA_DIR, BACTERIA_DIR, EUKARYOTA_DIR],
                              [RNAFORESTER_ARCHAEA_OUTPUT_FILE, RNAFORESTER_BACTERIA_OUTPUT_FILE,
                               RNAFORESTER_EUKARYOTA_OUTPUT_FILE])

    rnadistance_workbench.csv([ARCHAEA_DIR, BACTERIA_DIR, EUKARYOTA_DIR],
                              [RNADISTANCE_ARCHAEA_OUTPUT_FILE, RNADISTANCE_BACTERIA_OUTPUT_FILE,
                               RNADISTANCE_EUKARYOTA_OUTPUT_FILE])

    locarna_workbench.csv([ARCHAEA_DIR, BACTERIA_DIR, EUKARYOTA_DIR],
                          [LOCARNA_ARCHAEA_OUTPUT_FILE, LOCARNA_BACTERIA_OUTPUT_FILE, LOCARNA_EUKARYOTA_OUTPUT_FILE])

    rag2d_workbench.csv([ARCHAEA_DIR_2D, BACTERIA_DIR_2D, EUKARYOTA_DIR_2D],
                        [RAG2D_ARCHAEA_OUTPUT_FILE, RAG2D_BACTERIA_OUTPUT_FILE, RAG2D_EUKARYOTA_OUTPUT_FILE])

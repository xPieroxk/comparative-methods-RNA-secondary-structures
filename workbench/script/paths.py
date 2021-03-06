import os
import sys

# root directory of the workbench
WORKBENCH_PATH = os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0])))

# molecule directory
ARCHAEA_DIR = os.path.join(WORKBENCH_PATH, 'Molecules-pseudoknotfree', 'db-nH', 'Archaea', '5S')
BACTERIA_DIR = os.path.join(WORKBENCH_PATH, 'Molecules-pseudoknotfree', 'db-nH', 'Bacteria', '5S')
EUKARYOTA_DIR = os.path.join(WORKBENCH_PATH, 'Molecules-pseudoknotfree', 'db-nH', 'Eukaryota', '5S')
# molecule directory for bpseq
ARCHAEA_DIR_2D = os.path.join(WORKBENCH_PATH, 'Molecules-pseudoknotfree', 'bpseq-nH', 'Archaea', '5S')
BACTERIA_DIR_2D = os.path.join(WORKBENCH_PATH, 'Molecules-pseudoknotfree', 'bpseq-nH', 'Bacteria', '5S')
EUKARYOTA_DIR_2D = os.path.join(WORKBENCH_PATH, 'Molecules-pseudoknotfree', 'bpseq-nH', 'Eukaryota', '5S')

# ASPRAlign
ASPRALIGN_WORKBENCH_JAR = os.path.join(os.sep, 'gp', 'aspralign', 'executable-jar', 'ASPRAlignWorkbench.jar')
ASPRALIGN_CONFIG_FILE = os.path.join(os.sep, 'gp', 'aspralign', 'ASPRAlign-config.txt')

# output files
ASPRALIGN_ARCHAEA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'workbench-results', 'Archaea', '5S-aspralign.csv')
ASPRALIGN_BACTERIA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'workbench-results', 'Bacteria', '5S-aspralign.csv')
ASPRALIGN_EUKARYOTA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'workbench-results', 'Eukaryota', '5S-aspralign.csv')

NESTEDALIGN_ARCHAEA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'workbench-results', 'Archaea', '5S-nestedalign.csv')
NESTEDALIGN_BACTERIA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'workbench-results', 'Bacteria', '5S-nestedalign.csv')
NESTEDALIGN_EUKARYOTA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'workbench-results', 'Eukaryota', '5S-nestedalign.csv')

RNAFORESTER_ARCHAEA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'workbench-results', 'Archaea', '5S-rnaforester.csv')
RNAFORESTER_BACTERIA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'workbench-results', 'Bacteria', '5S-rnaforester.csv')
RNAFORESTER_EUKARYOTA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'workbench-results', 'Eukaryota', '5S-rnaforester.csv')

RNADISTANCE_ARCHAEA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'workbench-results', 'Archaea', '5S-rnadistance.csv')
RNADISTANCE_BACTERIA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'workbench-results', 'Bacteria', '5S-rnadistance.csv')
RNADISTANCE_EUKARYOTA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'workbench-results', 'Eukaryota', '5S-rnadistance.csv')

LOCARNA_ARCHAEA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'workbench-results', 'Archaea', '5S-locarna.csv')
LOCARNA_BACTERIA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'workbench-results', 'Bacteria', '5S-locarna.csv')
LOCARNA_EUKARYOTA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'workbench-results', 'Eukaryota', '5S-locarna.csv')

RAG2D_ARCHAEA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'workbench-results', 'Archaea', 'bpseq-rag2d.txt')
RAG2D_BACTERIA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'workbench-results', 'Bacteria', 'bpseq-rag2d.txt')
RAG2D_EUKARYOTA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'workbench-results', 'Eukaryota', 'bpseq-rag2d.txt')

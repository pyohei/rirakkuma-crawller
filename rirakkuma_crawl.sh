#!/bin/sh

# Execute rirakkuma crawller.

PYTHON_EXE=
EXE_FILE=
LOG_FILE=shell.log

echo `date +"%Y%m%d%H%M%S"` start >> ${LOG_FILE}
${PYTHON_EXE} ${EXE_FILE} 2>> ${LOG_FILE}
echo `date +"%Y%m%d%H%M%S"` end >> ${LOG_FILE}

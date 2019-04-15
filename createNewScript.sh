#!/bin/bash
if [ -z "$1" ] ; then
  echo "[ERROR] No name provided !"
  exit 1
fi
# Input, i.e.  10_problemName
_NAME="$1"
# Script Name
SNAME="${_NAME}.py"
# Function Name
FNAME="${_NAME/[0-9]*_/}"
_NUM="${_NAME/_[a-z]*/}"
echo "[INFO ] Script name : \"${SNAME}\"."
if [ ! -f ${SNAME} ] ; then
  cp template.py "${SNAME}"
  sed -i "s/_m_/${FNAME}/g" "${SNAME}"
  sed -i "s/%NUM%/${_NUM}/" "${SNAME}"
fi
vim  "${SNAME}"

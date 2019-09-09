#!/bin/csh

echo

if ($1 == "") then
  echo "Usage: pspdf <file> [letter]  (default: a4)"
  echo
  exit
endif

set target = $2
if ($2 != "letter") then
    set target = "a4"
endif

echo "Converting $1 to PDF ($target) ..."

ps2pdf -dCompatibilityLevel=1.4 -dMaxSubsetPct=100 -dSubsetFonts=true -dEmbedAllFonts=true -sPAPERSIZE=$2 $1

#ps2pdf -dPDFSETTINGS=/printer -dCompatibilityLevel=1.4 -dMaxSubsetPct=100 -dSubsetFonts=true -dEmbedAllFonts=true -sPAPERSIZE=$2 $1

echo

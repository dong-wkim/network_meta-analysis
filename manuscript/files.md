<!-- conversion scripts

$templatedocx = 'G:\My Drive\templates\docx\template.docx

from docx to md: manuscript.docx -> manuscript.md -> chunked files

 pandoc -f docx --reference-doc=$templatedocx -t markdown_strict -o manuscript.md manuscript.docx

-------------------------------------------------

from md to docx: chunked files -> draft.docx -> manuscript

 pandoc -f markdown --reference-doc=$templatedocx -t docx -o manuscript.docx --file-scope=true ./title ./abstract ./introduction/introduction.md ./methods/methods.md ./results/results.md
 ./discussion/discussion.md ./other_information/other_information.md



pandoc ./title/title.md ./abstract/abstract.md ./introduction/introduction.md ./methods/methods.md ./results/results.md
 ./discussion/discussion.md ./other_information/other_information.md metadata.yaml -s -o draft.docx

-->

PRISMA-NMA Checklist

# Title

# Abstract

# Introduction

## Rationale

## Objectives

# Methods

## Eligibility criteria

## Information sources

## Search strategy

## Selection process

## Data collection process

## Data items

## Study risk of bias assessment

## Effect measures

## Synthesis methods

## Reporting bias assessment

## Certainty assessment

# Results

## Study selection

## Study characteristics

## Risk of bias in studies

## Results of individual studies

## Results of syntheses

## Reporting biases

## Certainty of evidence

# Discussion

## Interpretation

## Limitations of evidence

## Limitations of review processes

## Implications

# Other information

## Registration and protocol

### Registration

### Protocol

### Amendments

## Support

## Competing interests

## Availability of data, code, and other materials

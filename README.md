# Internship project : FL-Minifier

## A Tool To Minify and Unify AdBlocker's Filter Lists

## Tasks

## Day 1

- [x] State of the art of AdBlockers
- [x] Research fingerprinting
- [x] Test AmIUnique site
- [x] Read the doc on Filter Lists Syntax
- [x] Overview with Naif

## Day 2

- [x] More Reading on filter lists
- [x] Read Naif's paper + docs
- [x] Technical overview with Naif

## Day 3

- Tasks

- [ ] Understand the code base (Mostly version checking)

- [x] Familiarise with set covers 

- [x] Checked out diff between different versions of easylist and looked into using that to generate set covers

- setbacks
  
  - Overwhelming codebase 
  - Tried to get FL versions from git automaticaly to no avail so far

- Intended for day n+1

- [ ] Download at least a few Versions of easylist

- [ ] Keep looking onto codebase (maybe focus on html generation to try and experiment further down the pipeline)

- [ ] experiment with diffing to create set covers

## Day 4

- Tasks

- [x] Try and run airflow pipeline

- setbacks
  
  - Python version for pandas has deprecated some functions so the container won't build

- Intended for day n+1

- [ ] Figure out python versions

- [ ] Get login on typhon

- [ ] Experiment with pipeline

## Day 5

- Tasks

- [x] Build docker image

- setbacks
  
  

- Intended for day n+1
  - Experiement with pipeline

## Day 6

- Tasks

- [x] Debug flagHTML

- setbacks
  
  - missing folders

- Intended for day n+1
  
  - Keep debugging

## Day 7

- Tasks

- [x] Run flagHTML

- [x] Debug generateUniqueRules

- setbacks
  
  - missing folders

- Intended for day n+1
  
  - Keep debugging

## Day 8

- Tasks

- [x] Continue Debugging genrerateUniqueRules
- [x] Document some code

- setbacks

  - Scheduler died (probably lack of RAM)


- Intended for day n+1
  
  - Continue Documentation
  - ? get workstation for more RAM ?

## Day 9

- Tasks

- [x] Run full arflow pipeline
- [x] Experiment with Chrome extensions
  > Extension appends specified div at the bottom of the page and it does get blocked by uBlockOrigin so this should be usable to incorporate filterlists checking into *AmIUnique* extension 

- setbacks

- Intended for day n+1
  - Continue experimenting with finding out wether the div is blocked or not from the extension itself

## Day 10

- Tasks

- [x] Added temporary way to test visibility
- [x] Run the test on idle tabs on a regular basis

- setbacks
  - After testing on other websites my initial visibility test appears to be flawed so more research needed

- Intended for day n+1
  - Figure out how to incorporate current *AmIUnique* code to the extension so that it actually tests for visibility
  - Figure out how to schedule all tests so that it doesn't negatively affect user experience

## Day 11

- Tasks

- [x] Move check to on_start so that the adblocker can act on it
- [x] Create a small api endpoint to fetch a list of properties for elements to check

- setbacks

- Intended for day n+1
  - Fetch data from the actual dataset
  - Figure out how to schedule all tests so that it doesn't negatively effect user experience



---

# References

[AmIUnique](https://amiunique.org/fp)
[ABP filter syntax](https://help.eyeo.com/en/adblockplus/how-to-write-filters#allowlist)
[uBO extended syntax](https://github.com/gorhill/uBlock/wiki/Static-filter-syntax#extended-syntax)

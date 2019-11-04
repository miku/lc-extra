# Library Carpentry Extra Content

Some additional material for [library carpentry](https://librarycarpentry.org/)
workshop, prepared for [2019-11-04 Workshop](https://ubleipzig.github.io/2019-11-04-leipzig/).

# Introductory slides for 2019-11-04

* [Slides](https://docs.google.com/presentation/d/1ifZE-cZSrZQICVZQWfzcvVdsUhnS0uOgtCdxnpJO3a0/edit#slide=id.p)

# A Microsoft Windows (TM) Virtual Machine

* [https://developer.microsoft.com/en-us/windows/downloads/virtual-machines](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines)

The VirtualBox version:
[https://aka.ms/windev_VM_virtualbox](https://aka.ms/windev_VM_virtualbox) - This VM will expire on 1/12/20.

```
a69ca4063dabf3fae881d891f28221c574eebce3  vm/WinDev1910Eval.ova
```

* Windows 10 1903 and the Windows 10 SDK, version 1903 (10.0.18362.1)
* Visual Studio 2019 with the UWP, .NET desktop, and Azure workflows enabled and also includes the Windows Template Studio extension
* Visual Studio Code
* Windows Template Studio extension
* Windows UWP samples (latest)
* Windows Subsystem for Linux enabled with Ubuntu installed
* Developer mode and bash enabled

# Python versatility

* most of Python functionality is not only in the language, but in the ecosystem, the libraries that are available
* many scientific libraries 
* helpers, data acquisition, data analysis, much more, ...
* niche things: MARC

A few examples that make use of additional libraries. All these libraries are written in Python.

## Fetching ISIL data

I wanted to have an offline version of ISIL database.

Question: Do you know how many ISIL are in ISIL-Verzeichnis?

Manual approach: Copy-and-paste, 28h non-stop-copy-paste (if we need 6s per item)

* https://sigel.staatsbibliothek-berlin.de/suche/
* https://gist.github.com/miku/c73ae7b40a4a18bbf0f751b52d18b082
* [x/fetch](x/fetch)

## Working with MARC

* The software community releases software as *open source*, here: a library called [pymarc](https://github.com/edsu/pymarc)
* [x/mrc](x/mrc)

## MARC and Excel

Reading MARC and writing Excel.

* [x/mrcxml](x/mrcxml)

## Reading and altering Excel

* [x/readxls](x/readxls)

## Notebook exploration

* [Working with CSV](https://github.com/miku/sundaypython/blob/master/notebooks/04%20Working%20with%20CSV.ipynb)

## Notebooks and Python work well together

* https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks

# Git Use Cases in GLAM and elsewhere

## Git Use Cases at Leipzig University Library and SLUB

* Software, [VuFind](https://github.com/vufind-org/vufind)
  ([Contributors](https://github.com/vufind-org/vufind/graphs/contributors)),
  [Kitodo](https://github.com/kitodo/kitodo-presentation), Typo3-Plugins. e.g.
  [Raumbuchung/Typo3 ](https://github.com/ubleipzig/tx-booking), Specifications,
  e.g. [intermediate schema](https://github.com/ubleipzig/intermediateschema),
  Tools, e.g. [solrdump](https://github.com/ubleipzig/solrdump), an [URN
  library](https://github.com/slub/urnlib), Documentation, e.g.
  [Papers](https://github.com/miku/siskin/blob/master/docs/tr-dilmmf/tr-dilmmf.tex)
  (LaTeX) or [presentations](https://github.com/miku/siskin/blob/master/docs/ai-overview/slides.md), Jupyter Notebooks, e.g. [Coding da Vinci Input Session](https://github.com/miku/sundaypython), [CSV example](https://github.com/miku/sundaypython/blob/master/notebooks/04%20Working%20with%20CSV.ipynb), Community, e.g. [BibsOnGitHub](https://github.com/hbunke/BibsOnGitHub), [code4lib](https://github.com/topics/code4lib), ...
* Larger library projects, e.g. [Open Library](https://github.com/internetarchive/openlibrary), [FOLIO](https://github.com/folio-org), ...
* [List of Tools and Project](https://github.com/ubleipzig/awesome-library), [RSE](https://github.com/ubleipzig/awesome-rse), [Scholarly Data Analysis](https://github.com/napsternxg/awesome-scholarly-data-analysis), ...
* Different things: [Gesetze des
  Bundestags](https://github.com/bundestag/gesetze),
  [GCHQ](https://github.com/gchq),
  [NSA](https://github.com/NationalSecurityAgency/enigma-simulator), initiatives
  and protests, e.g. [996.icu](https://github.com/996icu/996.ICU), ...

# Git installation on Windows 10

* Version used: [Git-2.23.0-32-bit.exe](https://github.com/git-for-windows/git/releases/download/v2.23.0.windows.1/Git-2.23.0-32-bit.exe)

For more questions, the default will be fine. As a nice, open source cross platform editor, we recommend

* [Visual Studio Code](https://code.visualstudio.com/)

## Git editor options

![](static/Git01Editor.png)
![](static/Git02Editor.png)

## Git path option

![](static/Git03Path.png)

## Git HTTPS options

![](static/Git04Transport.png)

## Git line endings

![](static/Git05Endings.png)

## Git terminal emulator

![](static/Git06Emulator.png)

## Git extras

![](static/Git07Extra.png)

## Git experimental features

![](static/Git08Experimental.png)

## Git wrap up

![](static/Git09Completing.png)
![](static/Git10Completing.png)

## Git version and config options

![](static/Git11Version.png)


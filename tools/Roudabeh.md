---
layout: page
title: Roudabeh (Rebeca Verifier)
permalink: /alltools/Roudabeh

---

#### Overview
**Roudabeh(Rebeca Verifier)** is a visual tool developed using Java language. In addition to integrating R2SMV tool in a visual environment, Roudabeh can extract component models from closed-world models automatically, verify them and show the results in graphical window. Here is the list of features:
* **Rebeca model editor** For writing, saving and editing Rebeca models.
* **Includes R2SMV** The tool can convert Rebeca models automatically to SMV codes.
* **Automatic topology extraction** The tool can read the Rebeca model, and discover the different rebecs participating in the system, and find out which rebec is bound to which of the other ones.
* **Graphical view of topology** System topology can be viewed graphically as a graph, with the nodes representing rebecs, and edges representing binding between them.
* **Automatic component model generation** After the user selects the rebecs which shall be included in a component, the tool can automatically generate a component Rebeca model for the part of the system chosen by the user. The environment is extracted from the whole system, according to the rebecs in the components. Translation to SMV can be done automatically.
* **Rebeca Property Parser** User can provide the properties of the system to be proved, based on variables in the Rebeca model. Property parser will translate it automatically into NuSMV property specifications.
* **Integration with NuSMV** (to be done) The tool run NuSMV in the background, manage the input/output of the program and use it for model checking Rebeca models which are translated to SMV. The result of verification is displayed in another window in Roudabeh after it is completed.

#### Artifacts
##### Roudabeh
* Version: **1.0**
* Last Updated: **27 December 2006**
* Size: **3.6 MB**
* Download: [ [Jar] ]()
* Related Documents: Help document [ [zip] ](http://ece.ut.ac.ir/fml/Roudabeh_Help.zip)


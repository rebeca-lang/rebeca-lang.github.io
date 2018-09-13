---
layout: page
title: Afra
permalink: /alltools/Afra

---

#### Overview

Afra is an integrated environment for modeling and verifying Rebeca family designs. The tool Afra is developed to integrate Java artifacts of Rebeca related projects. Generally speaking, Afra as an IDE provides development environment for models, property specification facilities, model checking facilities, and counter example visualization. Similar to other Eclipse plugin products, Afra user interface consists three main parts, project browser, model and property editor, and model-checking result view.

A Rebeca family model consists of the definition of _reactive classes_ and the instantiation part which is called _main_. The main part defines instances of reactive classes, called _rebecs_. The definition of reactive classes and the main part are presented in a file, called the _model_ file. Given a model file, properties which have to be satisfied by the model are described in other file, called _property_ file. A Rebeca property file consists of the definition of atomic propositions and a set of formulas. The propositional logics of temporal properties are expressions over the state variables of rebecs. Separating the propositional logic definition and the definition of logics formulas, makes the property models reusable and easy to understand.

#### Artifacts
##### Afra 3
* Version: **3.0.0**
* Last Updated: **September 13, 2018**
* Size: **58 MB**
* Java Version: **10 and 1.8**
* Download: [ [Windows x64] ](https://github.com/rebeca-lang/org.rebecalang.afra/blob/master/org.rebecalang.afra.repository/target/products/org.rebecalang.afra.ideplugins-win32.win32.x86_64.zip?raw=true) [ [Linux x64] ](https://github.com/rebeca-lang/org.rebecalang.afra/blob/master/org.rebecalang.afra.repository/target/products/org.rebecalang.afra.ideplugins-linux.gtk.x86_64.tar.gz?raw=true) [ [Mac OS X] ](https://github.com/rebeca-lang/org.rebecalang.afra/blob/master/org.rebecalang.afra.repository/target/products/org.rebecalang.afra.ideplugins-macosx.cocoa.x86_64.tar.gz?raw=true)
* Demo: How to work with Afra 3 [ [movie] ](http://rebeca.cs.ru.is/files/Movies/Afra/Afra3.0-Demo.mov)

Note that in the case of windows, you have to install [cygwin](http://www.cygwin.com) or [MinGW](http://www.mingw.org) or any other windows port of the g++ compiler before using Afra 3. Make sure that the "bin" directory, which contains "g++.exe", is included in the PATH environment variable. For MAC OS X, g++ compiler comes with Apple's [XCode](https://developer.apple.com/xcode/) tools package. 

##### Afra 2
* Version: **2.0.0**
* Last Updated: **May 5, 2012**
* Size: **52 MB**
* Download: [ [Windows x32] ](http://rebeca.cs.ru.is/files/afra2.zip)
* Related Documents: How to visualize state spaces [ [pdf] ](http://rebeca.cs.ru.is/files/How to visualize the State Space.pdf)

Note that you have to install [cygwin](http://www.cygwin.com) or [MinGW](http://www.mingw.org) or any other windows port of the g++ compiler before using Afra 2. Make sure that the "bin" directory, which contains "g++.exe", is included in the PATH environment variable.

##### Afra 1 (Open Source Edition)
* Version: **1.6.3**
* Last Updated: **February 2, 2009**
* Size: **116 MB**
* Download: [ [Windows x32] ](http://rebeca.cs.ru.is/files/afra-rebeca-only.exe)
* Related Documents: Installation manual [ [pdf] ](afra-installation.pdf)

Note that you have to install [cygwin](http://www.cygwin.com) or [MinGW](http://www.mingw.org) or any other windows port of the g++ compiler before using Afra 2. Make sure that the "bin" directory, which contains "g++.exe", is included in the PATH environment variable.

##### Afra 1 (SystemC Edition)
* Version: **1.6.3**
* Last Updated: **February 2, 2009**
* Size: **116 MB**
* Download: This edition of Afra is only available for academic use. To obtain an academic license, please contact "marjan.sirjani at mdh.se
* Related Documents: Installation manual [ [pdf] ](afra-installation.pdf)

Note that you have to install [cygwin](http://www.cygwin.com) or [MinGW](http://www.mingw.org) or any other windows port of the g++ compiler before using Afra 2. Make sure that the "bin" directory, which contains "g++.exe", is included in the PATH environment variable.

#### Detailed Description
The first release of Afra developed in the context of the project Sysfier. The goal of Sysfier is to develop an integrated environment for modeling and verifying SystemC designs by formalizing SystemC semantics and providing model checking tools. The tool Afra is developed to integrate Sytra, Modere and SyMon in addition to Rebeca and SystemC modeling environments. Afra gets SystemC models and LTL or CTL properties from the designer, and verifies the models. If a property is not satisfied, a counter- example is displayed. For verifying SystemC models, Afra translates SystemC codes to Rebeca using Sytra. It then utilizes the Rebeca verification tool set to verify the given properties. Where applicable, reduction techniques are used to tackle the state explosion problem.

<img align="right" width="100%" src="{{ "/assets/tools/Afra/afra.jpg" | absolute_url }}" alt="Afra Snapshot" />


**Sytra** generates Rebeca models from SystemC models based on the proposed formalism. KaSCPar (not in the context of SysFier) is used to parse the SystemC models. The output of this parser is an XML file representing the SystemC model. The Rebeca model is then generated using this XML file.

**SyMon**(SystemC Model checking Engine) is a verification engine customized for verification of Rebeca models obtained from SystemC codes. The SystemC simulation kernel executes the processes one by one, with a non-preemptive scheduling policy, according to a pre-specified order. SyMon uses this order instead of executing all the possible interleavings of processes and hence gains a significant amount of reduction in the size of the generated state space. This way it gives us a verification based on the semantics of SystemC simulation kernel.

**Modere** is the direct model checker of Rebeca. An important advantage of Modere over the existing verifiers is that since it is designed specifically for Rebeca, many abstraction and reduction techniques can be applied according to the computational model of Rebeca.

<p class="center">
<img align="right" width="50%" src="{{ "/assets/tools/Afra/afra_arch.jpg" | absolute_url }}" alt="Afra Arcitecture" />
</p>

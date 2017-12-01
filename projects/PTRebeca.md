---
layout: page
title: Probabilistic Timed Rebeca
permalink: /allprojects/PTRebeca

---

#### Description
PTRebeca language supports the modeling and verification of real-time systems with
probabilistic behaviors. The syntax of PTRebeca is a combination of pRebeca and TRebeca. We propose the appropriate semantics for PTRebeca to be able to model and verify probabilistic properties. In a probabilistic assignment, a value is assigned to the variable with the specified probability. Notably, by using probabilistic
assignment, the value of the timing constructs (delay, after, and deadline) can also become probabilistic.
We developed a toolset for the analysis of PTRebeca models. In this toolset, RMC package is used as the front-end of the toolset and IMCA is used as the back-end model checking engine. Using RMC, a number of C++ files are generated for a PTRebeca model. These C++ files are compiled and linked by the g++ compiler, which results in an executable file. Running the executable file generates the TMDP of the model (i.e. the state space of the model). In the PTRebeca models, the size of message bags is bounded. So, the state space of a PTRebeca model is finite when the model shows recurrent behavior. We used the time-shift equivalence approach, to make the state space finite.
The TMDP-MA tool is developed to convert the TMDP of the model to the input language of IMCA model checker. To perform the conversion, the generated TMDP and the specification of the "goal states" of the model are input to TMDP-MA and one Markov automaton is generated. The obtained MA is imported to the IMCA for model checking. Using a dedicated time action in TMDP (equivalently in MA) and the ability of assigning rewards to transitions in IMCA, expected-time reachability and probabilistic reachability properties can be computed for the model.

Note that although we developed a model checking toolset for PTRebeca models, they can be transformed to Probabilistic Timed Automata and be analyzed using corresponding toolset, as shown [here](http://rebeca.cs.ru.is/files/Documents/How-to-Model-PTRebeca-by-Parallel-Composition-of-PTA.pdf).

#### Tools
We developed a toolset for the analysis of PTRebeca models. In this toolset, RMC package is used as the front-end of the toolset and IMCA is used as the back-end model checking engine. Using RMC, a number of C++ files are generated for a PTRebeca model. These C++ files are compiled and linked by the g++ compiler, which results in an executable file. Running the executable file generates the TMDP of the model (i.e. the state space of the model). In the PTRebeca models, the size of message bags is bounded. So, the state space of a PTRebeca model is finite when the model shows recurrent behavior. We used the time-shift equivalence approach, to make the state space finite.
The TMDP-MA tool is developed to convert the TMDP of the model to the input language of IMCA model checker. To perform the conversion, the generated TMDP and the specification of the "goal states" of the model are input to TMDP-MA and one Markov automaton is generated. The obtained MA is imported to the IMCA for model checking. Using a dedicated time action in TMDP (equivalently in MA) and the ability of assigning rewards to transitions in IMCA, expected-time reachability and probabilistic reachability properties can be computed for the model.

* Compiler: [Jar]()

#### Case Studies
* [Probabilistic Sensor Network](/allprojects/PTRebecaExamples/ProbabilisticSensorNetwork)
* [Probabilistic Ticket Service](/allprojects/PTRebecaExamples/ProbabilisticTicketService)
* [Fault Tolerant NoC 4x4](/allprojects/PTRebecaExamples/FaultTolerantNoC4x4)

#### Project Members
* **<u>Marjan Sirjani (Principal Investigator)</u>**
* Ali Jafari
* Ehsan Khamespanah
* Holger Hermanns

#### Related Publications
* Ali Jafari, Ehsan Khamespanah, Haukur Kristinsson, Marjan Sirjani, Brynjar Magnusson: Statistical Model Checking of Timed Rebeca, Models Computer Languages, Systems & Structures, 2016 [ [pdf] ](/assets/papers/2016/COMLAN-D-15-00041R1-revised.pdf) [ [bib] ](http://dblp.uni-trier.de/rec/bibtex/journals/cl/JafariKKSM16)

* Ali Jafari, Ehsan Khamespanah, Marjan Sirjani, Holger Hermanns, Matteo Cimini: PTRebeca: Modeling and Analysis of Distributed and Asynchronous Systems, Science of Computer Programming, 2016 [ [pdf] ](/assets/papers/2016/SCICO-D-15-00126R1-revised.pdf) [ [bib] ](http://dblp.uni-trier.de/rec/bibtex/journals/scp/JafariKSHC16)

* Ali Jafari, Ehsan Khamespanah, Marjan Sirjani and Holger Hermanns, Performance Analysis of Distributed and Asynchronous Systems using Probabilistic Timed Actors, In: AVoCS 2014, Netherlands, 2014 [ [pdf] ](/assets/papers/2014/Performance-Analysis-of-Distibuted-and-Asynchronous-Systems-using-Probabilistic-Timed-Actors.pdf) [ [bib] ](http://dblp.uni-trier.de/rec/bibtex/journals/eceasst/JafariKSH14)

* Haukur Kristinsson, Ali Jafari, Ehsan Khamespanah, Marjan Sirjani, and Brynjar Magnusson: Analysing Timed Rebeca Using McErlang, AGERE, 2013 [ [pdf] ](/assets/papers/2013/Analysing-Timed-Rebeca-Using-McErlang.pdf) [ [bib] ](http://dblp.uni-trier.de/rec/bibtex/conf/agere/KristinssonJKMS13)


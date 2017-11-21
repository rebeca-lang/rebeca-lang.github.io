---
layout: page
title: Sysfier
permalink: /allprojects/Sysfier

---

#### Description
The goal of Sysfier is to develop an integrated environment for modeling and verifying SystemC designs by formalizing SystemC semantics and providing model checking tools. The tool Afra is developed to integrate Sytra, Modere and SyMon in addition to Rebeca and SystemC modeling environments. Afra gets SystemC models and LTL or CTL properties from the designer, and verifies the models. If a property is not satisfied, a counter-example is displayed. For verifying SystemC models, Afra translates SystemC codes to Rebeca using Sytra. It then utilizes the Rebeca verification tool set to verify the given properties. Where applicable, reduction techniques are used to tackle the state explosion problem.

#### Tools
* Integrated Development and Analysis Environment [Afra](/alltools/Afra).

#### Case Studies
* [Dining Philosophers](/allprojects/SysfierExamples/DiningPhilosophers)
* [Train Controller](/allprojects/SysfierExamples/TrainController)
* [CSMA-CD](/allprojects/SysfierExamples/CSMACD)
* [Leader Election](/allprojects/SysfierExamples/LeaderElection)
* [Commit Problem](/allprojects/SysfierExamples/CommitProblem)
* [Sender Receiver](/allprojects/SysfierExamples/SenderReceiver)
* [Producer Consumer](/allprojects/SysfierExamples/ProducerConsumer)
* [Spanning Tree Protocol](/allprojects/SysfierExamples/SpanningTreeProtocol)

#### Project Members
* **<u>Marjan Sirjani (Principal Investigator)</u>**
* Niloofar Razavi
* Hamideh Sabouri
* Raziyeh Behjati
* Amin Shali
* Hossein Hojjat
* Ehsan Khamespanah
* Ramtin Khosravi

#### Related Publications
* Niloofar Razavi, Razieh Behjati, Hamideh Sabouri, Ehsan Khamespanah, Amin Shali, Marjan Sirjani: Sysfier: Actor-based formal verification of SystemC. ACM Trans. Embedded Comput. Syst. 10(2): 19 (2010) [ [bib] ](http://dblp.uni-trier.de/rec/bibtex/journals/tecs/RazaviBSKSS10)

* Razieh Behjati, Hamideh Sabouri, Niloofar Razavi, Marjan Sirjani: An effective approach for model checking SystemC designs. ACSD 2008: 56-61 [ [bib] ](http://dblp.uni-trier.de/rec/bibtex/conf/acsd/BehjatiSRS08)

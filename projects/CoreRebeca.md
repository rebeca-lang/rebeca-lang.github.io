---
layout: page
title: Core Rebeca
permalink: /allprojects/CoreRebeca

---

#### Description
Rebeca is an actor-based language for modeling concurrent and reactive systems with asynchronous message passing. The actor model was originally introduced by Hewitt as an agent-based language, and is a mathematical model of concurrent computation that treats as the universal primitives of concurrent computation. A Rebeca model is similar to the actor model as it has reactive objects with no shared variables, asynchronous message passing with no blocking send and no explicit receive, and unbounded buffers for messages. Objects in Rebeca are reactive, self-contained, and each of them is called a _rebec_ (reactive object). Communication takes place by message passing among rebecs. Each rebec has an unbounded buffer, called message _queue_, for its arriving messages. Computation is event-driven, meaning that each rebec takes a message that can be considered as an event from the top of its message queue and execute the corresponding message server (also called a method). The execution of a message server is atomic execution (non-preemptive execution) of its body that is not interleaved with any other method execution.

#### Tools
* Integrated Development and Analysis Environment [Afra](/alltools/Afra).

#### Case Studies
* [Dining Philosophers](/allprojects/CoreRebecaExamples/DiningPhilosophers)
* [Train Controller](/allprojects/CoreRebecaExamples/TrainController)
* [CSMA-CD](/allprojects/CoreRebecaExamples/CSMACD)
* [Leader Election](/allprojects/CoreRebecaExamples/LeaderElection)
* [Commit Problem](/allprojects/CoreRebecaExamples/CommitProblem)
* [Sender Receiver](/allprojects/CoreRebecaExamples/SenderReceiver)
* [Producer Consumer](/allprojects/CoreRebecaExamples/ProducerConsumer)
* [Spanning Tree Protocol](/allprojects/CoreRebecaExamples/SpanningTreeProtocol)

#### Project Members
* **<u>Marjan Sirjani (Principal Investigator)</u>**
* Mahdi Jaghouri
* Hamed Iravanchi
* Amin Shali
* Ehsan Khamespanah

#### Related Publications
* Marjan Sirjani, Ali Movaghar, Hamed Iravanchi, Mohammad Mahdi Jaghoori, Amin Shali: Model Checking in Rebeca. PDPTA 2003: 1819-1822. [ [bib] ](http://dblp.uni-trier.de/rec/bibtex/conf/pdpta/SirjaniMIJS03)

* Marjan Sirjani, Ali Movaghar, Amin Shali, Frank S. de Boer: Modeling and Verification of Reactive Systems using Rebeca. Fundam. Inform. 63(4): 385-410 (2004). [ [pdf] ](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.107.2074&rep=rep1&type=pdf) [ [bib] ](http://dblp.uni-trier.de/rec/bibtex/journals/fuin/SirjaniMSB04)

* Ehsan Khamespanah, Marjan Sirjani, Ramtin Khosravi: Afra: An Eclipse-Based Tool with Extensible Architecture for Modeling and Model Checking of Rebeca Family Models. FSEN 2023: 72-87. [ [pdf] ]("/assets/papers/2023/Afra.pdf)
[ [bib] ](https://dblp.org/rec/conf/fsen/KhamespanahSK23.html?view=bibtex)

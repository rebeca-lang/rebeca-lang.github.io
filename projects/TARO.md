---
layout: page
title: TARO (Timed Rebeca)
permalink: /allprojects/TARO

---

#### Description
Building reliable software systems is a complex but important challenge of modern engineering. A fundamental determiner of software reliability is the methodology used to develop and verify both designs and implementations. Current tools have significant limitations that increase the cost and development time of software systems. There is no question that one of the fundamental tasks in computer and information science is advancing the state of our development methods: We need better techniques and tools for developing correct and predictable software systems.

Current methodologies are proved to be insufficient and ineffective in developing reliable and trustworthy distributed and asynchronous systems, specially when we are concerned about timing constraints. So, a main challenge of software engineering in future is to establish novel ideas, methods, and techniques for developing systems of this category. In the ICT (Information and Communication Technologies) work programme of 2010 of the European Commission, the first challenge is pervasive and trustworthy network and service infrastructures. At the same time formal analysis and verification are inevitable techniques to ensure dependability of systems.

In TARO (Timed Asynchronous Reactive Objects in Distributed Systems) project, we aim at contributing to this research effort. We propose to develop a methodology, techniques and tools, for building fully asynchronous systems, whose behaviour depends crucially on timing constraints, with associated formal analysis and verification support. Our methodology is based on proposing an actor-based modeling language, extended with timing constraints and supported by formal verification tools. The research emphasis in the project places it firmly at the core of the grand challenge of developing reliable networked systems, and at the leading edge of research in software engineering. The real-world case studies will be used as testbeds for establishing the applicability of the proposed methodology and of the associated tools. They will tie together the theoretical and practical aspects of the research, resulting in a substantial synergy.

#### Tools
* The analysis toolset is integrated with [Afra](/alltools/Afra).

#### Case Studies
* ASPIN, a GALS design for Network on Chip 4x4: [ [Rebeca model] ](/assets/projects/TARO/case-studies/ASPIN.rebeca)
* DyAD, Odd-Even, and XY routing algorithms for NoCs [ [zip] ](/assets/projects/TARO/case-studies/Dyad-OE-XY.zip)
* Sensor Network: [ [Rebeca model] ](/assets/projects/TARO/case-studies/sensornetwork.rebeca)
* Carrier Sense Multiple Access (CDMA) protocol with timing specification: [ [Rebeca model] ](/assets/projects/TARO/case-studies/tcsma.rebeca)
* [Ticket Service System](/allprojects/TAROExamples/TicketService)

The following case studies are also developed which include TCTL property specifications.
* ASPIN Network on Chip: [ [zip] ](/assets/projects/TARO/case-studies/noc-prop.zip)
* Ticket Service System: [ [zip] ](/assets/projects/TARO/case-studies/ticket-service-prop.zip)
* WSAN Applications: [ [zip] ](/assets/projects/TARO/case-studies/tinyos-prop.zip)
* Hadoop Yarn Schedule: [ [zip] ](/assets/projects/TARO/case-studies/yarn-prop.zip)

#### Contributers
* **<u>Marjan Sirjani (Principal Investigator)</u>**
* Ehsan Khamespanah
* Ramtin Khosravi
* Javad Izadi
* Zeynab Sabahi-Kaviani
* Arni Hermann Reynisson
* Steinar Hugi Sigurdarson
* Luca Aceto
* Anna Ingólfsdóttir
* Matteo Cimini
* Ali Jafari
* Brynjar Magnusson
* Haukur Kristinsson

#### Related Publications
* Ehsan Khamespanah, Kirill Mechitov, Marjan Sirjani, Gul Agha: Modeling and Analyzing Real-Time Wireless Sensor and Actuator Networks Using Actors and Model Checking, Submitted to Software Tools for Technology Transfer, 2017  [ [pdf] ](/assets/papers/2017/Modeling-and-Analyzing-Real-Time-Wireless-Sensor-and-Actuator-Networks-Using-Actors-and-Model-Checking.pdf)

* Ehsan Khamespanah, Ramtin Khosravi, Marjan Sirjani: An Efficient TCTL Model Checking Algorithm and A Reduction Technique for Verification of Timed Actor Models, Submitted to Science of Computer Programming, 2017  [ [pdf] ](/assets/papers/2017/Efficient-TCTL.pdf)

* Marjan Sirjani, Ehsan Khamespanah, Kirill Mechitov, Gul Agha: A Compositional Approach for  Modeling and Timing Analysis of Wireless Sensor and Actuator Networks, CRTS, 2016  [ [pdf] ](/assets/papers/2016/CompositionalTinyOS.pdf)

* Ehsan Khamespanah, Kirill Mechitov, Marjan Sirjani, Gul Agha: Schedulability Analysis of Distributed Real-Time Sensor Network Applications Using Actor-Based Model Checking, SPIN, 2016  [ [pdf] ](/assets/papers/2016/TinyOS.pdf) [ [bib] ](http://dblp.uni-trier.de/rec/bibtex/conf/spin/KhamespanahMSA16)

* Marjan Sirjani, Ehsan Khamespanah: On Time Actors, LNCS 9660, 2016 [ [pdf] ](/assets/papers/2016/TimedActor.pdf) [ [bib] ](http://dblp.uni-trier.de/rec/bibtex/conf/birthday/SirjaniK16)

* Ehsan Khamespanah, Marjan Sirjani, Zeynab Sabahi Kaviani, Ramtin Khosravi, Mohammad-Javad Izadi: Timed Rebeca Schedulability and Deadlock Freedom Analysis Using Bounded Floating Time Transition System, Science of Computer Programming, 2015 [ [pdf] ](/assets/papers/2014/Timed-Rebeca-Shift-Equivalency-published.pdf) [ [bib] ](http://dblp.uni-trier.de/rec/bibtex/journals/scp/KhamespanahSSKI15) 

* Ehsan Khamespanah, Marjan Sirjani, Mahesh Viswanathan, Ramtin Khosravi: Floating Time Transition System: More Efficient Analysis of Timed Actors, FACS, 2015  [ [pdf] ](/assets/papers/2015/FTTStoTTS.pdf) [ [bib] ](http://dblp.uni-trier.de/rec/bibtex/conf/facs2/KhamespanahSVK15)

* Arni Hermann Reynisson, Marjan Sirjani, Luca Aceto, Matteo Cimini, Ali Jafari, Anna Ingolfsdottir, Steinar Hugi Sigurdarson, Modelling and simulation of asynchronous real-time systems using Timed Rebeca, Science of Computer Programming, 2014 [ [pdf] ](/assets/papers/2014/Modelling and simulation of asynchronous real-time systems using Timed Rebeca.pdf) [ [bib] ](http://dblp.uni-trier.de/rec/bibtex/journals/scp/ReynissonSACJIS14)

* Brynjar Magnusson, Ehsan Khamespanah, Marjan Sirjani, Ramtin Khosravi, Event-based Analysis of Timed Rebeca Models using SQL, AGERE 2014, USA, October 2014 [ [pdf] ](/assets/papers/2014/TeProp.pdf) [ [bib] ](http://dblp.uni-trier.de/rec/bibtex/conf/agere/MagnussonKKS14)

* Ehsan Khamespanah, Marjan Sirjani, Ramtin Khosravi, Efficient TCTL Model Checking Algorithm for Timed Actors, AGERE 2014, USA, October 2014 [ [pdf] ](/assets/papers/2014/TCTL.pdf) [ [bib] ](http://dblp.uni-trier.de/rec/bibtex/conf/agere/KhamespanahKS14)

* Haukur Kristinsson: Event-Based analysis of Read-Time Actor Models - Master Thesis, Reykjavík University, Iceland (2012) [ [pdf] ](/assets/Thesis/EVENT-BASED%20ANALYSIS%20OF%20REAL-TIME%20ACTOR%20MODELS%20-%20Haukur%20Kristinsson.pdf)

* Brynjar Magnusson: Simulation-Based Analysis of Timed Rebeca Using TeProp and SQL - Master Thesis, Reykjavík University, Iceland (2012) [ [pdf] ](/assets/Thesis/SIMULATION-BASED%20ANALYSIS%20OF%20TIMED%20REBECA%20USING%20TEPROP%20AND%20SQL%20-%20Brynjar%20Magnusson.pdf)

* Ehsan Khamespanah, Zeynab Sabahi Kaviani, Ramtin Khosravi, Marjan Sirjani, Mohammad-Javad Izadi: Timed-Rebeca Schedulability and Deadlock-Freedom Analysis Using Floating-Time Transition System, AGERE, 2012 [ [pdf] ](http://apice.unibo.it/xwiki/bin/download/AGERE2012/AcceptedPapers/ageresplash2012submission20.pdf) [ [bib] ](http://dblp.uni-trier.de/rec/bibtex/conf/agere/KhamespanahSKSI12)

* Luca Aceto, Matteo Cimini, Anna Ingólfsdóttir, Arni Hermann Reynisson, Steinar Hugi Sigurdarson, Marjan Sirjani: Modelling and Simulation of Asynchronous Real-Time Systems using Timed Rebeca FOCLASA, 2011 [ [pdf] ](http://www.google.com/url?sa=t&rct=j&q=%20marjan%20sirjani%3A%20%20%20modelling%20and%20simulation%20of%20asynchronous%20real-time%20systems%20using%20timed%20rebeca%20pdf&source=web&cd=1&ved=0CB8QFjAA&url=http%3A%2F%2Farxiv.org%2Fpdf%2F1108.0228&ei=6gV0UNKtAYbWsgamhoHgBA&usg=AFQjCNFltFhVQAQJahHq_oooBOIt8nhfNw) [ [bib] ](http://dblp.uni-trier.de/rec/bibtex/journals/corr/abs-1108-0228)

* Arni Hermann Reynisson: Timed Rebeca Refinement and Simulation - Master Thesis, Reykjavík University, Iceland (2011) [ [pdf] ](/assets/Thesis/TIMED%20REBECA%20REFINEMENT%20AND%20SIMULATION%20-%20Arni%20Hermann%20Reynisson.pdf)
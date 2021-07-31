---
layout: page
title: SEADA&#58; Self-Adaptive Actors
permalink: /allprojects/Seada

---

#### Description
SEADA is a project funded by Rannís, The Icelandic Centre for Research.

In SEADA, we propose a framework for self-adaptive systems with a component-based architecture built in Ptolemy II that forms the feedback loop. Our models@runtime is coded in Timed Rebeca. Supporting tools for customized runtime formal verification of these models are developed. Our focus is on safety assurance while addressing uncertainty and responsiveness of the applications. SEADA benefits from using Ptolemy in various ways. Ptolemy gives us the support for modeling cyber-physical systems; hence interaction with the physical world can be done smoothly. Furthermore, connecting Ptolemy actors and Rebeca actors can be done in a natural way, so, keeping the model@runtime up-to-date using Ptolemy event queues takes the least effort. The distinctive feature of SEADA is its actor-based flavor which will reflect in the design of the components of the architecture, the models in the knowledge-base, and in the V&V and formal verification techniques. In developing SEADA models we focus on the air traffic control and flight network applications. These applications are safety critical, and highly sensitive to changes that can occur in the system and the environment.

##### Predictive Adaptation for Air Traffic Control
We use the well-known MAPE-K (Monitor, Analyze, Plane, Execute – Knowledge) feedback loop to realize self-adaptive systems. By extending the Discrete-Event director of Ptolemy, we develop a director that besides an abstract knowledge about the actor-based model@runtime encapsulates the Analyzed and Plan activities of the MAPE-K loop. We use simulation of Ptolemy for the analysis purpose, and augment the director with several adaption policies, e.g. rerouting algorithm in the case of air traffic control systems, for the adaptation purpose. The director is augmented with construction rules to be applied on the actors. For instance, for the case of air traffic control systems, the director prevents two aircraft (two messages) from traveling across the same sub-track at the same time (to be received by the same actor at the same time). We augment our director with predictive adaptation. Upon occurring a change, the director adapts the model@runtime with every adaptation policy, executes the adapted model to calculates performance metrics, compares the results, and based on some criteria, selects the best policy for adaptation purpose. Resources for the predictive adaptation for an air traffic control system are accessible via these links: <a class="link link_pdf" href="/assets/papers/2018/Self-Adaptive-Coordinated-Actors.pdf">Paper</a> <a class="link link_presentation" href="/assets/projects/Seada/case-studies/ATC-FACS.zip">Source Code</a> 

##### Magnifier: Runtime Compositional Verification of Self-adaptive Traffic Control Systems
We extend the Discrete-Event director of Ptolemy and develop a nondeterministic model of computation. From a set of actors to be triggered at the same time, the director selects one of them non-deterministically. We use this director to generate the state space of the model@runtime under an adaptation policy and check safety properties, e.g. the fuel of an aircraft does not pass a threshold, the model is deadlock-free, the aircraft arrive at their destinations at the pre-specified times, etc. We develop a Magnifier director that knows the details of each component of the system, e.g. it knows that which aircraft have to flight over which control area, what their arrival times at the components are and what their departure times from the components are. By decomposing the model into several components, Magnifier uses an iterative and incremental process to generate the state space of the model and check the safety properties. Resources for verifying an air traffic control system using Magnifier and the classical state space generation algorithm are accessible via this link: <a class="link link_presentation" href="/assets/projects/Seada/case-studies/MagImp-TSE.zip">Source Code</a> 

#### More Resources
* The demo of our model@runtime for air traffic control: [ [video] ](http://rebeca.cs.ru.is/files/Movies/SEADA/ATC5.mov) (by Maryam Bagheri). 
* The demo of our model@runtime for railway systems: [ [video] ](http://rebeca.cs.ru.is/files/Movies/SEADA/TCS1.mov) (by Maryam Bagheri).
<!--* Two examples of the ATC model: [ Model 1 ](/assets/projects/Seada/case-studies/ATC-FACS.zip) [ Model 2 ](/assets/projects/Seada/case-studies/MagImp-TSE.zip)-->
* Platoon of Multi Vehicles: [ [rebeca] ](/assets/projects/Seada/case-studies/PlatoonMultiVehicles.rebeca)

#### Project Members
* **<u>Marjan Sirjani (Principal Investigator)</u>**
* Ehsan Khamespanah
* Maryam Bagheri
* Ali Jafari
* Edward A. Lee
* Narges Khakpour
* Farnaz Yousefi

#### Most Related Publications
- Maryam Bagheri, Edward A. Lee, Eunsuk Kang, Marjan Sirjani, Ehsan Khamespanah, Ali Movaghar: Lightweight Formal Method for Robust Routing in Track-based Traffic Control Systems, MEMCODE, 2020
<a class="link link_pdf" href="/assets/papers/2020/Lightweight-Formal-Method-for-Robust-Routing-in-Track-based-Traffic-Control-Systems.pdf">PDF</a>

- Farnaz Yousefi, Ehsan Khamespanah, Mohammed Gharib, Marjan Sirjani, Ali Movaghar: VeriVANca Framework: Verification of VANETs by Property Based Message Passing of Actors in Rebeca with Inheritance, Software Tools for Technology Transfer, 2020
<a class="link link_pdf" href="/assets/papers/2020/VeriVANca-An-Actor-Based-Framework-for-Formal-Verification-of-VANET-Applications.pdf">PDF</a>

- Maryam Bagheri, Marjan Sirjani, Ehsan Khamespanah, Christel Baier and Ali Movaghar, Magnifier: A Compositional Analysis Approach for Autonomous Traffic Control, IEEE Transactions on Software Engineering, 2021
<a class="link link_pdf" href="/assets/papers/2021/Magnifier-A-Compositional-Analysis-Approach-for-Autonomous-Traffic-Control.pdf">PDF</a>

<!-- - Maryam Bagheri, Marjan Sirjani, Ehsan Khamespanah and Ali Movaghar: Runtime Compositional Verification of Self-adaptive Track-based Traffic Control Systems, Submitted to IEEE Transactions on Software Engineering, Jul 2020 
<a class="link link_pdf" href="/assets/papers/2020/Runtime_Compositional_Verification_of_Self_adaptive_Track_based_Traffic_Control_Systems.pdf">PDF</a>
-->
- Farnaz Yousefi, Ehsan Khamespanah, Mohammed Gharib, Marjan Sirjani, Ali Movaghar: VeriVANca: An Actor-Based Framework for Formal Verification of Warning Message Dissemination Schemes in VANETs, SPIN, 2019
<a class="link link_pdf" href="/assets/papers/2019/VeriVANca-An-Actor-Based-Framework-for-Formal-Verification-of-Warning-Message-Dissemination-Schemes-in-VANETs.pdf">PDF</a>
<a class="link link_bibtex" href="https://dblp.org/rec/bibtex/conf/spin/YousefiKGSM19">BibTeX</a>

- Maryam Bagheri, Marjan Sirjani, Ehsan Khamespanah, Narges Khakpour, Ilge Akkaya, Ali Movaghar and Edward A. Lee: Coordinated Actor Model of Self-adaptive Track-based Traffic Control Systems, Journal of Systems and Software, 2018 
<a class="link link_pdf" href="/assets/papers/2018/Self-Adaptive-Coordinated-Actors.pdf">PDF</a>

- Maryam Bagheri, Ehsan Khamespanah, Marjan Sirjani, Ali Movaghar, Edward A. Lee: Runtime Compositional Analysis of Track-based Traffic Control Systems, CRTS, 2016 
<a class="link link_pdf" href="/assets/papers/2016/RuntimeCompositionalAnalysisofTTCS.pdf">PDF</a>

- Maryam Bagheri, Ilge Akkaya, Ehsan Khamespanah, Narges Khakpour, Marjan Sirjani, Ali Movaghar, Edward A. Lee: Coordinated Actors for Reliable Self-Adaptive Systems, FACS, 2016 
<a class="link link_pdf" href="/assets/papers/2016/CoordinatedActorsforReliableSelfAdaptiveSystems.pdf">PDF</a> <a class="link link_bibtex" href="http://dblp.uni-trier.de/rec/bibtex/conf/facs2/BagheriAKKSML16">PDF</a>

- Maryam Bagheri, Ilge Akkaya, Ehsan Khamespanah, Narges Khakpour, Marjan Sirjani, Ali Movaghar, Edward A. Lee: Modeling and Analyzing Air Traffic Control Systems using Ptolemy, Ptolemy Mini-Conference, 2015 <a class="link link_pdf" href="/assets/papers/2015/ATC-PtolemyPoster-Final.pdf">PDF</a>


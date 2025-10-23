---
layout: page
title: ReLico: Timed Rebeca to Lingua Franca
permalink: /allprojects/ReLico

---
#### ReLico: Timed Rebeca to Lingua Franca
#### Problem Description 
Timed Rebeca and Lingua Franca both target cyber-physical systems but use different execution models. Timed Rebeca allows nondeterminism, where multiple events can occur at the same logical time in any order. This flexibility supports thorough verification but makes it difficult to create executable implementations. Lingua Franca requires deterministic execution through a precedence mechanism, which ensures consistent behavior.​

This difference creates a challenge when converting verified Timed Rebeca models into executable Lingua Franca programs. The goal is to preserve timing semantics, message ordering, and system behavior without introducing nondeterminism or requiring manual re-implementation.

This project solves this problem by defining deterministic subsets of both languages. A formal bisimulation proves that both subsets produce equivalent behavior. This allows verified Timed Rebeca models to be automatically translated into deterministic, executable Lingua Franca code while preserving structure and timing guarantees.​

#### Tool: Relico
* [Relico](https://github.com/sarmadiali98/ReLico) - Timed Rebeca to Lingua Franca Compiler


#### Case Studies 
* [Timed Rebeca to Lingua Franca Examples](https://github.com/sarmadiali98/Timed-Rebeca-to-Lingua-Franca-Examples)


#### Project Members
* Ali Sarmadi
* Mahboubeh Samadi
* Hossein Hojjat
* Marjan Sirjani

